import requests
from bs4 import BeautifulSoup

class SimpleWebCrawler:
    def __init__(self, urls):
        self.url = urls

    def fetch_page(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
            else:
                print(f"Failed to fetch {url} with status code: {response.status_code}")
                return None
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None

    def extract_title(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup.title.string if soup.title else "No Title Found"

    def crawl(self):
        for url in self.url:
            print(f"Crawling {url}....")
            html_content = self.fetch_page(url)
            if html_content:
                title = self.extract_title(html_content)
                print(f"Title: {title}")

if __name__ == "__main__":
    urls = [
        "http://example.com",
        "http://example.com/page1",
        "http://example.com/page2"
    ]
    crawler = SimpleWebCrawler(urls)
    crawler.crawl()