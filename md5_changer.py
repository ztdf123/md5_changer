import os

def isVideo(filename):
    if filename.endswith('.mp4') or filename.endswith('.mkv') \
            or filename.endswith('.avi') or filename.endswith(".mwv") \
            or filename.endswith('.rm') or filename.endswith('.rmvb') \
            or filename.endswith('.flv') or filename.endswith('.mov') \
            or filename.endswith('.vob') or filename.endswith('.mpg') \
            or filename.endswith('.qt') or filename.endswith('.mpeg') \
            or filename.endswith('.ogg') or filename.endswith('.3gp'):
        return True
    return False

def bfs(rootDir):
    for root, dirs, files in os.walk(rootDir):
        for file in files:
            if isVideo(file):
                with open(os.path.join(root, file), 'a') as f:
                    f.write('bad md5')
                    f.close()
                    print(file + "  Video Detected, md5 has been changed.")
                    global total_video_num
                    total_video_num = total_video_num + 1
        for dir in dirs:
            print(os.path.join(root,dir))


total_video_num = 0

print("欢迎使用视频MD5批量修改助手!")
print("本软件仅供学习交流使用，一切使用软件可能造成的不良后果由使用者个人承担")
while(1):
    total_video_num = 0
    print("请输入要批量修改的文件夹路径，请直接从资源管理器地址栏复制：")
    DIRPATH = input()
    print(DIRPATH)
    bfs(DIRPATH)

    print("Task Done!\n")
    print('Successfully modified the md5 value of a total of ' + str(total_video_num) + ' videos')
    
