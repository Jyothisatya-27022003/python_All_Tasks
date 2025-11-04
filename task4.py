# Task 4: Basic Web Scraper

import requests
from bs4 import BeautifulSoup

def scrape_headlines(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')

        print("\n📰 Top News Headlines:\n" + "-" * 40)
        headlines = soup.find_all('h3')
        if not headlines:
            print("⚠️ No headlines found. The website structure may have changed.")
        else:
            for i, headline in enumerate(headlines[:10], 1):
                text = headline.get_text(strip=True)
                print(f"{i}. {text}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

# --- Main Program ---
print("🌍 Welcome to the Web Scraper Program!")
url = input("Enter a news website URL (e.g., https://www.bbc.com/news): ")

scrape_headlines(url)
