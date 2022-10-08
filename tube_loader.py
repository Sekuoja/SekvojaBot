from yt_dlp import YoutubeDL
import os


direct = os.path.abspath(os.curdir) + "/temp"

def yt_loader(urls: list) -> None:
    param = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        "paths": {
        "home": direct
        }
    }

    with YoutubeDL(param) as ydl:
        try:
            ydl.download(urls)
        except:
            pass

