import os
import subprocess


def composite_video(video, audio, to):
    cmd = 'ffmpeg -y -i %s -i %s -c:v copy -c:a aac -strict experimental %s' % (
        os.path.abspath(video), os.path.abspath(audio), os.path.abspath(to))
    subprocess.Popen(cmd, shell=True).communicate()
    print('视频合成成功')
