<p align="center">
<h1 align="center">MyStatus(似sǐ😢了吗?)</h1>
</p>
<p align="center">
    这样女朋友就知道我不是故意不回复她了😎
    <br/>
    <br/>
    <a href="https://github.com/Van-Kai/MyStatus/issues/new" target="_blank">🐛上报 Bug、🤔问题反馈、📄需求提报！</a>
</p>
<p align="center">
    <img alt="Gitea Stars" src="https://img.shields.io/github/stars/Van-Kai/MyStatus?style=flat-square&logo=GitHub">
    <img alt="GitHub forks" src="https://img.shields.io/github/forks/Van-Kai/MyStatus?style=flat-square&logo=GitHub">
    <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/t/Van-Kai/MyStatus?style=flat-square&logo=GitHub">
    <img alt="GitHub Issues or Pull Requests" src="https://img.shields.io/github/issues-closed-raw/Van-Kai/MyStatus?style=flat-square&logo=GitHub">
    <img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/Van-Kai/MyStatus?style=flat-square&logo=GitHub">
    <img alt="GitHub License" src="https://img.shields.io/github/license/Van-Kai/MyStatus?style=flat-square">
</p>

## 🎉简介
**MyStatus**能够记录手机等设备的状态，它基于[FastAPI](https://fastapi.tiangolo.com/)框架，能够给你带来良好的使用体验。

## 💡即刻开始
**部署需求：Python环境、善用思考的大脑、会用百度**

1、先将本项目Clone到本地或者服务器

2、在项目目录下执行`pip install -r requirements.txt`

3、打开项目根目录 中的*config.py* 文件(有代码编辑器更好，没有的话可以使用记事本打开)

4、在图示位置输入您的QQ以及SECRET 这个配置至关重要 后续会用到 **请牢记** 

(<img src="https://github.com/Van-Kai/MyStatus/blob/master/ReadmeSrc/help/1.png?raw=true" width="210px">

5、运行main文件即可

`python main.py`

6、这时候浏览器访问`127.0.0.1:8000 `亦或是局域网地址即可看到界面

**注意：如果您要部署在服务器默认您有一定基础，请自行摸索。**

***至此 服务端配置完成***

***接下来配置手机客户端***

7、客户端使用到了安卓自动化神器 MacroDroid 

​	iOS请自行使用快捷指令配置也可以到达目的

8、安装MacroDroid 可自行百度 亦或者安装包放在了**项目中的MacroDroid 目录** 自行选择安装方法

8、您可以看到在MacroDroid 目录还有两个.macro结尾的配置文件 请一并下载

9、接下来您需要设法将文件传入到您的安卓手机

10、安装 MacroDroid 并将两个配置文件导入到MacroDroid 

11、点击箭头示例

<img src="https://github.com/Van-Kai/MyStatus/blob/master/ReadmeSrc/help/2.jpeg?raw=true" width="210px">

点击配置

<img src="https://github.com/Van-Kai/MyStatus/blob/master/ReadmeSrc/help/3.jpeg?raw=true" width="210px">
<img src="https://github.com/Van-Kai/MyStatus/blob/master/ReadmeSrc/help/4.jpeg?raw=true" width="210px">

接下来是重中之重

> 修改 `https://status.12131213.xyz/api/putappdata?secret=randomSecret` 这个链接里面的secret为你第四步设置的secret `https://status.12131213.xyz/` 这一部分请修改为你的公网地址，亦或是局域网地址 注意是**https还是http**

你会发现还有一个**息屏**配置项没有更改，重复以上操作即可

👩‍🎨最后访问浏览器访问`127.0.0.1:8000 `亦或是局域网地址即可 大功告成 

## 🥰ToDo

- [ ] 完善项目结构(长期)
- [ ] 增加用户系统
- [ ] 完善前端界面
- [x] 待补充

## ✌️界面图片
<img src="https://github.com/Van-Kai/MyStatus/blob/master/ReadmeSrc/ui1.jpg?raw=true" width="800px">
<img src="https://github.com/Van-Kai/MyStatus/blob/master/ReadmeSrc/ui2.jpg?raw=true" width="300px">

## 😽灵感来源
[哔哩哔哩：改了个能让各位实时视奸我的网站](https://www.bilibili.com/video/BV1LjB9YjEi3/?spm_id_from=333.1007.top_right_bar_window_default_collection.content.click&vd_source=b47e4ea7324766cf337912907843ffc9)

[哔哩哔哩：写了一个能让各位知道我睡没睡着的网页](https://www.bilibili.com/video/BV1fE421A7PE/?spm_id_from=333.1387.homepage.video_card.click)

在此特别感谢