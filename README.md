# CoinMarketCap Web Scraper

This project is a web scraper designed to extract cryptocurrency data from [CoinMarketCap](https://coinmarketcap.com/). The scraper fetches, processes, and stores data in a CSV file for further analysis.

## Features
- Scrapes cryptocurrency data from CoinMarketCap.
- Removes redundant data and extracts relevant fields.
- Stores the cleaned data in a CSV file.
- Implements request headers to mimic a real browser and reduce blocking.
- Introduces random delays between requests to avoid detection.

## File Structure
- **`web_scraper.py`** - Contains the `CoinMarketCapScraper` class that handles the scraping logic.
- **`csv_module.py`** - Handles CSV file creation and writing of scraped data.
- **`main.py`** - Orchestrates the scraping process and saves the data.

## Installation & Setup
1. Ensure you have Python installed (3.x recommended).
2. Install the required dependencies:
   ```bash
   pip install requests
   ```
3. Clone this repository and navigate to the project directory.

## Usage
Run the scraper using:
```bash
python main.py
```
This will:
1. Scrape the first page of CoinMarketCap.
2. Extract and clean the data.
3. Save it to `CoinMarketCap.csv`.

## Example Output (CSV)
The extracted data is formatted as follows:

| Name  | Abbreviation | Price | Volume (24h) | Market Cap | ... |
|-------|-------------|--------|-------------|------------|-----|
| Bitcoin | BTC | 73000 | 887.5M | 1.4T | ... |
| Ethereum | ETH | 3700 | 560M | 430B | ... |

## Potential Improvements
- Support for scraping multiple pages dynamically.
- Data visualization and trend analysis.
- Error handling enhancements for better reliability.

---

**Note:** This scraper follows ethical web scraping practices and respects the target site's `robots.txt`. Ensure you comply with CoinMarketCap's terms of service when using this script.
```
