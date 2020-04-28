import youtube_dl

from app.models import Song


class YoutubeDL:

    def __init__(self, path):
        self.ydl_opts = {
            'format': 'bestaudio/best',
            'nocheckcertificate': True,
            'outtmpl': f'{path}/%(id)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

    def __createSongModel(self, url, metadata):
        song = Song()
        song.url = url
        id = metadata.get('id')
        song.media_id = f'{id}.mp3'
        song.title = metadata.get('title')
        song.alt_title = metadata.get('alt_title')
        song.artist = metadata.get('artist')
        song.album = metadata.get('album')
        return song

    def convert_url_to_mp3(self, url):
        with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
            ydl.download([url])
            info_dict = ydl.extract_info(url, download=False)
            return self.__createSongModel(url=url, metadata=info_dict)
        raise Exception(f'Unable to convert video: "{url}".')
