from pytube3 import Youtube
from downloader import downloader


def run():
    downloader = downloader()
    downloader.collect_links