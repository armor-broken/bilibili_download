from download.download import Download
from composite.composite import composite_video

if __name__ == '__main__':
    base_url = 'https://www.bilibili.com/video/BV1jN41197FS'

    download = Download()

    res_va = download.get_va_url(base_url)
    res_download = download.generate_va(res_va)

    if res_download:
        composite_video('./files/video.mp4', './files/audio.mp3', './files/video_final.mp4')

