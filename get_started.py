from downloader import Downloader
import sys

def run():
    url = sys.argv[1]
    downloader = Downloader()
    links = downloader.collect_links(url)
    file_ext = 'mp3'
    if file_ext == 'mp3':
        downloader.process_links_mp3(links)
    elif file_ext == 'mp4':
        downloader.process_links_mp4(links)
