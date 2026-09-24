import os
import csv
import requests
from bs4 import BeautifulSoup

def scrape_ecommerce_books():
    print("=== KUMBH AI: E-COMMERCE SCRAPER BOT ===\n")
    url = "http://books.toscrape.com/"
    print(f"Fetching product data from {url} ...")
    
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        products = soup.find_all('article', class_='product_pod')
        
        books_data = []
        for item in products:
            title = item.h3.a['title']
            price = item.find('p', class_='price_color').text.strip()
            stock = item.find('p', class_='instock availability').text.strip()
            books_data.append([title, price, stock])
            
        download_folder = "/sdcard/Download"
        csv_filename = os.path.join(download_folder, "kumbh_ecommerce_books.csv")
        
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Book Title', 'Price', 'Stock Status'])
            writer.writerows(books_data)
            
        print(f"\nSUCCESS! Scraped {len(books_data)} products.")
        print(f"File saved directly to: {csv_filename}")
    else:
        print(f"Failed to connect. Status code: {response.status_code}")

if __name__ == "__main__":
    scrape_ecommerce_books()
