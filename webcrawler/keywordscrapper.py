import requests
from bs4 import BeautifulSoup
from googlesearch import search
import sys

def fetch_page_content(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def search_for_keyword(html_content, keyword):
    ret = False
    keyword = keyword.split()
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text().lower()
    for word in keyword:
        if word.lower() in text:
            ret = True
    return ret
    #return keyword.lower() in text

def scrape_for_keyword(keyword, num_results=10):
    query = f"landing page {keyword}"
    found_pages = []

    for url in search(query, num_results=num_results):
        print(f"Checking {url}...")
        html_content = fetch_page_content(url)
        if html_content and search_for_keyword(html_content, keyword):
            found_pages.append(url)

    return found_pages

# Specify the keyword to search for
keyword = sys.argv[1]

# Specify the number of Google search results to check
num_results = int(sys.argv[2])

landing_pages = scrape_for_keyword(keyword, num_results)

print(f"Found {len(landing_pages)} landing pages containing the keyword '{keyword}':")
for page in landing_pages:
    print(page)
