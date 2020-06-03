from bs4 import BeautifulSoup
import requests
from pytube import YouTube
import youtube_dl

class Downloader:
    def __init__(self, url):
        super().__init__()
        self.url = url

    def collect_links(self):
        html = requests.get(self.url)
        soup = BeautifulSoup(html.text, 'html.parser')
        links = soup.find_all('a', class_="pl-video-title-link yt-uix-tile-link yt-uix-sessionlink spf-link")
        self.titles = []
        self.video_links = []
        for link in links:
            self.titles.append(link.text.strip())
            href_start = str(link).find('href=')
            href_end = str(link).find(';list=')
            link_fract = str(link)[href_start + 6:href_end]
            valid_link = 'https://www.youtube.com' + link_fract
            self.video_links.append(valid_link)
        print('Collected all Links')
        return self.video_links

    def process_links_mp4(self, links):
        pass

    def process_links_mp3(self, links):
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'quiet': False,
            'restrictfilenames': True,
            'outtmpl' : r'C:\Users\Freddy\Music\Youtube_Playlist_downloads\%(title)s.%(ext)s'
        }      
        print('Start downloads') 
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(links)
            print('\n', 'Downloaded: ', self.titles)


