from datetime import datetime
from typing import Annotated
import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Query, APIRouter
from sqlmodel import Field, Session, SQLModel, create_engine, select
from config import Config
config = Config()


# 导入并创建数据库模型：SQLModel
class AppData(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    AppName: str = Field(index=True)
    batteryPower: str
    QQ: str = Field(index=True) # 方便后期对接QQ机器人
    time: datetime = Field(default_factory=lambda:datetime.now().replace(microsecond=0)) # 数据库自动添加时间


class UserTable(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    UserName: str = Field(index=True)
    QQ: str = Field(index=True)
    PassWord: str = Field(index=False)
    Secret: str = Field(index=False)


# 创建引擎
"""SQLModel （在下面实际上是 SQLAlchemy ）是保存与数据库的连接的东西。
engine engine你会有单个对象engine的所有代码都连接到同一个数据库。"""
sqlite_file_name = config.sqlite_file_name
sqlite_url = config.sqlite_url
connect_args = {"check_same_thread": False}  # 忽略跨线程限制，从而避免报错。
engine = create_engine(sqlite_url, connect_args=connect_args)
"""创建表
然后，我们添加一个函数，用于为所有表模型创建表。SQLModel.metadata.create_all(engine)"""


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


"""创建会话依赖关系
一个Session是将对象存储在内存中并跟踪数据中所需的任何更改，然后它使用engine与数据库通信。
我们将创建一个 FastAPI 依赖项，它将为每个请求提供一个新的依赖项。这就是确保我们每个请求使用单个会话的原因。🤓yieldSession"""


def get_session():
    with Session(engine) as session:
        yield session


# 然后，我们创建一个依赖项来简化将使用此依赖项的其余代码。AnnotatedSessionDep
SessionDep = Annotated[Session, Depends(get_session)]
# app = FastAPI()

"""启动时创建数据库表¶
我们将在应用程序启动时创建数据库表。"""
userNameRouter = APIRouter(tags=['AppName上传获取'])


# @app.on_event('startup')
@userNameRouter.on_event('startup')
def on_startup():
    create_db_and_tables()



# 向数据库中加入应用信息


@userNameRouter.post("/putappdata/")
# @app.post("/putappdata/")
async def create_hero(appdata: AppData, secret: str, session: SessionDep):
    result = querySecret(appdata.QQ, session)
    if result != False and secret == result:
        if config.isIgnoreSystemTable:
            if appdata.AppName == "系统桌面":
                print("检测到打开了系统桌面，忽略录入数据库")
                return appdata
            else:
                session.add(appdata)
                session.commit()
                session.refresh(appdata)
                return appdata
        else:
            session.add(appdata)
            session.commit()
            session.refresh(appdata)
        return appdata
    else:
        print("秘钥不存在或账户不存在")
        return {"error": "秘钥不存在或账户不存在"}


# 查询数据库指定QQ下最后一个打开的App
# @app.get("/searchAppdata/")
@userNameRouter.get("/searchAppdata/")
async def read_latest_app_name(qq: str, secret: str, session: Session = Depends(get_session)) :
    result = querySecret(qq, session)
    if result != False and secret == querySecret(qq, session):
        result = get_latest_app_name(qq, session)
        return {"AppName": result.AppName,
                "batteryPower":result.batteryPower,
                "time":result.time
                }
    else:
        print("秘钥不存在或账户不存在")
        return {"error": "秘钥不存在或账户不存在"}


from sqlmodel import func


@userNameRouter.get("/top10appnames/")
def get_top_10_appnames(qq:str ,session: SessionDep):
    # 子查询获取最近 1000 条记录
    subquery = (
        select(AppData)
        .where(AppData.QQ == qq)  # 限制在指定 QQ 的记录中查询
        .order_by(AppData.time.desc())
        .limit(1000)
    ).subquery()

    # 在子查询上统计 AppName 出现次数并排序
    query = (
        select(subquery.c.AppName, func.count(subquery.c.AppName).label("count"))
        .group_by(subquery.c.AppName)
        .order_by(func.count(subquery.c.AppName).desc())
        .limit(10)
    )
    results = session.exec(query).all()
    # appname = [row.AppName for row in results]
    # count = [row.count for row in results]


    # 返回结果
    return [{"AppName": row.AppName, "Count": row.count} for row in results]


def get_latest_app_name(qq: str, session: Session) -> AppData:
    # 查询某个 QQ 下 time 最新的一条记录
    query = select(AppData).where(AppData.QQ == qq).order_by(AppData.time.desc()).limit(1)
    result = session.exec(query).first()

    if not result:
        raise HTTPException(status_code=404, detail="No records found for this QQ")
    return result




def querySecret(qq: str, session: Session):
    # 搜索QQ所对应的秘钥 鉴权用
    try:
        query = select(UserTable).where(UserTable.QQ == qq).limit(1)
        result = session.exec(query).first()
        return result.Secret
    except Exception as e:
        print(e)
        return False


