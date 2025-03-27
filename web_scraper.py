import requests
import time, random
import re

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

    def __fetch_page(self, page):
        """Fetch the HTML content of a CoinMarketCap page."""
        url = f"{self.base_url}?page={page}"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching page {page}: {e}")
            return None

    def __cut_down_html(self,html):
        cut_data = html.split('{')
        furth_cut_dt = []
        actual_dta = []

        for data in cut_data:
            furth_cut_dt.append(data.split('}'))
        
        for data in furth_cut_dt:
            try:    
                if f"{data[0][0]}{data[0][1]}{data[0][2]}{data[0][3]}{data[0][4]}{data[0][5]}{data[0][6]}" == '"name":':
                    actual_dta.append(str(data))
            except Exception as e:
                print(f"Error found: {e}")
        
        #for data in actual_dta:
        #    print(f"{data}\n")

        return actual_dta

    def __remove_redundant_data(self,data):
        for i in range(len(data)):
            data[i] = data[i].strip('[')
            data[i] = data[i].strip(']')
            
        unique_entries = {}

        for entry in data:
            match = re.search(r'"name":"(.*?)"', entry)  # Extracts name value
            if match:
                name = match.group(1)  # BTC, ETH, etc.
                unique_entries[name] = entry  # Keep latest entry

        # Convert back to list
        cleaned_data = list(unique_entries.values())

        return cleaned_data
        # for n_data in cleaned_data:
            # print(f"{n_data}\n")

    def __remove_given_fields(self,nested_list):
        sanitized_list = []
        
        for sublist in nested_list:
            sanitized_sublist = []
            for field in sublist:
                parts = field.split(":", 1)  # Split only once to avoid issues with colons in data
                if len(parts) == 2:  # Ensure there are two parts (identifier and data)
                    sanitized_sublist.append(parts[1].strip('"'))  # Remove quotes around data
                else:
                    sanitized_sublist.append("")  # Handle malformed data by adding an empty string
            sanitized_list.append(sanitized_sublist)
        
        return sanitized_list

    def __parse_page(self, html):
        data = self.__cut_down_html(html)
        data = self.__remove_redundant_data(data)
        new_set_data = []

        for dta in data:
            new_set_data.append(dta.split(","))
        
        # for set in new_set_data:
        #     for field in set:
        #         print(field)

        return self.__remove_given_fields(new_set_data)

    def scrape(self):
        """Run the scraping process for multiple pages."""
        for page in range(1, self.pages + 1):
            print(f"Scraping page {page}...")
            html = self.__fetch_page(page)
            #print(html)
            if html:
                self.coins = self.__parse_page(html)
            
            time.sleep(random.uniform(3, 6))  # Avoid getting blocked

        return self.coins