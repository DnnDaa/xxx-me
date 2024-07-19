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
yt-dlp.exe|视频及音频下载依赖，可以单独使用也可以基于三方脚本使用
油猴脚本|主要实现在网页通过一个功能按钮，点击后可以直接复制网页的url并调用本地的服务程序进行下载
本地程序调用脚本|一个本地服务器运行在http://localhost:5000/run-program，当接收到POST请求时会执行相应的Windows程序
PY调用脚本|基于主程序进行下载

