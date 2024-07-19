import os
import subprocess
import time
import threading
import pyperclip

def print_menu():
    print("                                yt-dlp 助手v3  快乐男孩love你  20240711")
    print("                         查询支持下载的视频格式 记录一下视频流ID和音频流ID  并下载")
    print("\n提示：Youtube下载请输入视频分享的地址或视频id")

def get_user_input(prompt, default_value, timeout=5):
    print(prompt, end='', flush=True)
    
    # 创建一个线程来读取用户输入
    user_input = [None]
    
    def input_thread():
        user_input[0] = input()
    
    thread = threading.Thread(target=input_thread)
    thread.start()
    thread.join(timeout)
    
    # 如果超时，则返回默认值
    if thread.is_alive():
        print(f"\n*****超时! 默认选择 {default_value}")
        return default_value
    else:
        return user_input[0].strip()

def download_video(url, choice, video_path):
    if choice == "1":
        if not os.path.exists(video_path):
            os.makedirs(video_path)
            print(f"*****已经为您创建了 {video_path} 的文件夹")
        
        print("*****正在进行全高画质下载.......")
        subprocess.run(["yt-dlp", "--merge-output-format", "mp4", "-f", "bestvideo*+bestaudio/best", "--merge-output-format", "mp4", url])
        print(f"*****下载完成，视频默认储存在{video_path}文件夹")
        print(f"*****程序将在5秒后退出并打开视频存储文件夹！")
    
    elif choice == "2":
        if not os.path.exists(video_path):
            os.makedirs(video_path)
            print(f"*****已经为您创建了 {video_path} 的文件夹")

        video_id = input("*****请输入需要输出的视频 video和video格式ID号：").strip()
        audio_id = input("*****请输入audioid：").strip()
        print(f"*****你选择的音视频组合ID是  {video_id}  X  {audio_id}")
        
        print("*****下载中.........")
        subprocess.run(["yt-dlp", "--merge-output-format", "mp4", url, "-f", f"{video_id}+{audio_id}"])
        print(f"*****下载完成，视频默认储存在{video_path}文件夹")
        print(f"*****程序将在5秒后退出并打开视频存储文件夹！")
    else:
        print(f"*****当前输入字符{choice}没有相关指令，程序将在5秒后退出!")


def main():
    clipboard_url = pyperclip.paste().strip()
    if clipboard_url and "https" in clipboard_url or "http" in clipboard_url:
        print(f"从剪贴板获取的URL: {clipboard_url}")
        url = clipboard_url
    else:
        print("视频地址不正确，请手动输入！")
        # 如果剪贴板没有内容，则要求用户输入
        url = input("******请输入视频地址：").strip()
     # 验证用户输入的内容
        while not (url and "https" in url or "http" in url):
            print("不合法的视频地址，请重新输入")
            url = input("请输入视频地址或视频id：").strip()
    # 显示支持下载的格式列表
    print("*****正在查询支持下载的格式列表.......")
    subprocess.run(["yt-dlp", "-F", url])

    default_choice = "1"
    choice = get_user_input("选择视频全高画质输出请输入：1，自行选择画质请输入：2\n请输入 (默认选择1): ", default_value=default_choice, timeout=5)
    
    video_path = "F:\\VideoDownload"
    
    # 执行下载操作
    download_video(url, choice, video_path)


    os.startfile(video_path)
    os._exit(0)



if __name__ == "__main__":
    main()
