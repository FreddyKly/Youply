from downloader import Downloader
import sys

def run():
    url = sys.argv[1]
    downloader_obj = Downloader(url)
    links = downloader_obj.collect_links()
    file_ext = 'mp3'
    if file_ext == 'mp3':
        downloader_obj.process_links_mp3(links)
    elif file_ext == 'mp4':
        downloader_obj.process_links_mp4(links)
