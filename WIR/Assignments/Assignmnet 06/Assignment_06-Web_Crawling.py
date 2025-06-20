import requests
from bs4 import BeautifulSoup
from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse

class SimpleWebCrawler:
    def __init__(self, urls, user_agent="SimpleWebCrawlerBot"):
        self.urls = urls
        self.user_agent = user_agent
        self.robots_parsers = {}

    def crawl(self):
        for url in self.urls:
            if self.can_fetch(url):
                print(f"Crawling {url}....")
                html_content = self.fetch_page(url)
                if html_content:
                    title = self.extract_title(html_content)
                    print(f"Title: {title}")
            else:
                print(f"Access to {url} is disallowed by robots.txt")

    def can_fetch(self, url):
        rp = self.fetch_robots_txt(url)
        if rp is None:
            return True
        return rp.can_fetch(self.user_agent, url)

    def extract_title(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup.title.string if soup.title else "No Title Found"
    
    def fetch_robots_txt(self, url):
        domain = urlparse(url).netloc
        if domain not in self.robots_parsers:
            robots_url = f"http://{domain}/robots.txt"
            rp = RobotFileParser()
            rp.set_url(robots_url)
            try:
                rp.read()
            except Exception:
                rp = None
            self.robots_parsers[domain] = rp
        return self.robots_parsers.get(domain)
    
    def fetch_page(self, url):
        headers = {"User-Agent": self.user_agent}
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return response.text
            else:
                print(f"Failed to fetch {url} with status code: {response.status_code}")
                return None
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None

if __name__ == "__main__":
    urls = [
        "http://example.com",
        "http://example.com/page1",
        "http://example.com/page2"
    ]
    crawler = SimpleWebCrawler(urls)
    crawler.crawl()
