from web_scraper import CoinMarketCapScraper
import time

def main():
    scraper = CoinMarketCapScraper(pages=1)  # Scrape first 2 pages
    data = scraper.scrape()
    print(data)
    print("Scraping complete!")
    time.sleep(3)
    print("Saving scraped data")

if __name__ == "__main__":
    main()


"""
data looks as follows
"name":"BTC","price":7.73047897e-10,
"volume24h":887.5082495477241,"volume7d":6682.982307702676,
"volume30d":26819.316485477833,"marketCap":7441.478729341666,
"selfReportedMarketCap":7202.967888891104,"percentChange1h":-0.319568,
"percentChange24h":-0.849965,"percentChange7d":3.700368,
"lastUpdated":"2025-03-26T00:43:00.000Z",
"percentChange30d":-20.786968,"percentChange60d":-40.02053,
"percentChange90d":-56.930991,"fullyDilluttedMarketCap":655692932.1,
"marketCapByTotalSupply":7469.4077511842725,"dominance":0.0227,
"turnover":0.11926504,"ytdPriceChangePercentage":-61.7962,
"percentChange1y":-72.17571148', ',']
"""