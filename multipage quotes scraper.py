import os
import csv
import requests
from bs4 import BeautifulSoup

def scrape_multipage_quotes():
    print("=== KUMBH AI: ADVANCED MULTI-PAGE SCRAPER ===\n")
    print("--- Starting Multi-Page Extraction ---")
    
    base_url = "http://quotes.toscrape.com/page/{}/"
    all_quotes = []
    
    for page in range(1, 11):
        url = base_url.format(page)
        print(f"Fetching Page {page} from {url} ...")
        
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            quotes = soup.find_all('div', class_='quote')
            
            for item in quotes:
                text = item.find('span', class_='text').text.strip()
                author = item.find('small', class_='author').text.strip()
                all_quotes.append([text, author])
        else:
            print(f"Failed to fetch page {page}")
            
    print("\n>>> Reached last page. Scraping finished.")
    print(f"\n--- SUCCESS: Total {len(all_quotes)} Quotes Extracted across 10 pages ---")
    
    download_folder = "/sdcard/Download"
    csv_filename = os.path.join(download_folder, "kumbh_multipage_quotes.csv")
    
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Quote Text', 'Author Name'])
        writer.writerows(all_quotes)
        
    print(f"Data saved to: {csv_filename}")

if __name__ == "__main__":
    scrape_multipage_quotes()
