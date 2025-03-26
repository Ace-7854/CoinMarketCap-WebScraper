import requests
from bs4 import BeautifulSoup
import time
import random

class CoinMarketCapScraper:
    def __init__(self, pages):
        self.base_url = "https://coinmarketcap.com/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://www.google.com/",
        }
        self.pages = pages
        self.coins = []

    def fetch_page(self, page):
        """Fetch the HTML content of a CoinMarketCap page."""
        url = f"{self.base_url}?page={page}"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching page {page}: {e}")
            return None

    def parse_page(self, html):
        cut_data = html.split('{')
        furth_cut_dt = []
        actual_dta = []

        for data in cut_data:
            furth_cut_dt.append(data.split('}'))
        
        for data in furth_cut_dt:
            try:    
                if f"{data[0][0]}{data[0][1]}{data[0][2]}{data[0][3]}{data[0][4]}{data[0][5]}{data[0][6]}" == '"name":':
                    actual_dta.append(data[0])
            except Exception as e:
                print(f"Error found: {e}")

        for data in actual_dta:
            
            print(f"{data}\n")


    def scrape(self):
        """Run the scraping process for multiple pages."""
        for page in range(1, self.pages + 1):
            print(f"Scraping page {page}...")
            html = self.fetch_page(page)
            #print(html)
            if html:
                self.parse_page(html)
            
            time.sleep(random.uniform(3, 6))  # Avoid getting blocked

        return self.coins

    def save_to_csv(self, filename="coinmarketcap_data.csv"):
        """Save scraped data to a CSV file."""
        # df = pd.DataFrame(self.coins)
        # df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
