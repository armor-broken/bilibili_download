import requests
import re
import json


class Download:
    def __init__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
            'referer': 'https://www.bilibili.com'
        }

    def get_va_url(self, url):
        '''
        获取视频和音频地址
        :param url: B站视频地址
        :return: 要下载视频和音频的地址
        '''
        # 获取网页源代码
        html_data = requests.get(url, headers=self.headers).text
        # 正则解析视频和音频数据，并转化为json格式
        video_data = json.loads(re.findall('<script>window\.__playinfo__=(.*?)</script>', html_data)[0])
        # 从为json格式数据中获取视频和音频地址
        video_url = video_data['data']['dash']['video'][0]['backupUrl'][0]
        audio_url = video_data['data']['dash']['audio'][0]['backupUrl'][0]
        return {'video_url': video_url, 'audio_url': audio_url}

    def generate_va(self, va):
        '''
        根据视频和音频地址下载视频和音频
        :param va:
        :return: 视频是否下载成功
        '''
        try:
            video_url = va['video_url']
            audio_url = va['audio_url']
            # 根据视频和音频地址，请求视频和音频二进制流数据
            video_file = requests.get(video_url, headers=self.headers).content
            audio_file = requests.get(audio_url, headers=self.headers).content
            # 将视频和音频二进制流数据，写入本地
            with open('./files/video.mp4', 'wb') as fp:
                fp.write(video_file)
            with open('./files/audio.mp3', 'wb') as fp:
                fp.write(audio_file)
            print('视频和音频下载成功')
            return True
        except Exception as e:
            return False
