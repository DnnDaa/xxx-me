# 【Youtube下载程序】
基于YT-DLP的Youtube下载程序，方便、快捷 <br>
***
<!-- MANPAGE: BEGIN EXCLUDED SECTION -->
[![Windows](https://img.shields.io/badge/-Windows_x64-blue.svg?style=for-the-badge&logo=windows)](https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe)
<!-- MANPAGE: END EXCLUDED SECTION -->
# 包含:<br>
* YT-DLP主程序<br>
* 油猴脚本--主要用来提取网页URL并自动复制剪切板<br>
* 本地程序调用脚本server.py<br>
#### 目录

文件|详情
:---|:---
yt-dlp|视频及音频下载依赖，可以单独使用也可以基于三方脚本使用，主要包含yt-dlp主程序和ffmpeg，需配置环境变量，
aria2|一个多线程下载程序，本程序可以单独使用也可以调用aria2，详情看yt-dlp官方文档，如需调用需配置环境变量
网页自动复制URL-1.0.user.js|是一个油猴脚本，主要实现在网页通过一个功能按钮，点击后可以直接复制网页的url并调用本地的服务程序进行下载，需结合实际更改本地程序入口youtube.bat路径
server.py|一个本地服务器运行在http://localhost:5000/run-program，当接收到POST请求时会执行相应的Windows程序
youtube2.py|基于主程序进行命令行拆解下载，可选择最高画质也可自行选择，需要pyhon环境且安装相关插件，根据实际更改视频储存目录（video_path）需与yt-dlp.conf中存储目录一致
K.vbs|主要将serve.py开机自行启动，隐藏命令行，win+R 输入：shell:startup放进去，需结合实际更改server.py路径
youtube.bat|提供调用本地程序入口，需结合实际更改本地程序youtube2.py路径

