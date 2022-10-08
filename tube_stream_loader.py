from typing import BinaryIO
from pytube import YouTube
from pytube import Playlist
import io


def yt_stream(urls: list) -> (str, BinaryIO):
    if urls[0].find("list=") != -1:
        urls = Playlist(urls[0])
    for url in urls:
        video = YouTube(url)
        audio = video.streams.get_audio_only()
        title = audio.title
        buffer = io.BytesIO()
        audio.stream_to_buffer(buffer=buffer)
        yield title, buffer
