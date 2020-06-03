from pytube import YouTube
from downloader import Downloader
import sys

def run():
    url = sys.argv[1]
    downloader = Downloader()
    downloader.collect_links(url)