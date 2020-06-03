from bs4 import BeautifulSoup
import requests

class Downloader:
    def collect_links(self, url):
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'html.parser')
        links = soup.find_all('a', class_="pl-video-title-link yt-uix-tile-link yt-uix-sessionlink spf-link")
        titles = []
        for link in links:
            titles.append(link.text.strip())
            href_start = str(link).find('href=')
            href_end = str(link).find(';list=')
            link_fract = str(link)[href_start + 6:href_end]
            valid_link = 'youtube.com' + link_fract
            print(valid_link)
