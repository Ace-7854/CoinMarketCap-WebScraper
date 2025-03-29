from web_scraper import CoinMarketCapScraper
import time
from csv_module import csv_module

def display_data(current_data):
    """Quick method to display data"""
    for data in current_data:
                print(f"{data}\n")

def get_pages():
    scraper = CoinMarketCapScraper(pages=1) # Scrape first page
    data = scraper.scrape()
    #display_data(data)
    print("Scraping complete!")

    return data

def update_data():
    data = get_pages()

    csv_file = csv_module("CoinMarketCap.csv")
    csv_file.write_to_file(data)


def main():
    """Demo as to how web_Scraper works"""
    update_data()

    print("Data collected and saved into CSV, retrieving now!")

    csv_f = csv_module("CoinMarketCap.csv")
    csv_f.read_from_file()
    print()
    print("DATA RETRIEVED")


if __name__ == "__main__":
    main()