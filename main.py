import json
from fastapi import FastAPI
import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request
import httpx
# 导入路由
from database.database import userNameRouter
from config import Config
config = Config()
app = FastAPI()

# create router

# 设置模板目录
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    async with httpx.AsyncClient() as client:
        # 调用 /get_data 接口获取数据
        response = await client.get(f"http://127.0.0.1:8000/api/searchAppdata/?qq={config.QQ}&secret={config.SECRET_KEY}")
        reschart = await client.get(f"http://127.0.0.1:8000/api/top10appnames/?qq={config.QQ}")
        reschart = reschart.text
        reschart = json.loads(reschart)

        appname = [row["AppName"] for row in reschart]
        count = [row["Count"] for row in reschart]

        print(appname)
        print(count)

        data = response.text  # 获取返回的 JSON 数据
        data = json.loads(data)
        print(data)
    app_name = data.get('AppName', 'Unknown App')
    battery_power = data.get('batteryPower', 'Unknown Power')
    updateTime = data.get('time', 'Unknown time').replace("T"," ")
    # 统计表数据获取

    return templates.TemplateResponse("index.html", {
        "request": request,
        "name": "凯凯",
        "appname": app_name,
        "batteryPower": battery_power,
        "updateTime": updateTime,
        "appName": appname,
        "appcount": count,
    })


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


app.include_router(userNameRouter, prefix="/api", tags=["AppName上传获取"])
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
