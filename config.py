
import pathlib

path = pathlib.Path(__file__).parent.absolute()


class Config:
    QQ = "2027514529"
    SECRET_KEY = "randomSecret"
    PATH = path
    sqlite_file_name = "database.db"
    DATABASE_PATH = path / "database"  # 在 BASE_PATH 下的 database 目录
    sqlite_url = f"sqlite:///{DATABASE_PATH / sqlite_file_name}"
    isIgnoreSystemTable = False  # 是否忽略系统桌面忽略录入数据库


if __name__ == "__main__":
    print(path)
