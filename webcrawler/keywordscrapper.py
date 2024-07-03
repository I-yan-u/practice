import requests
from bs4 import BeautifulSoup
from googlesearch import search
import sys
import asyncio
from concurrent.futures import ThreadPoolExecutor
import functools

event = asyncio.Event()

async def fetch_page_content(url):
    await event.wait()
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        try:
            get_request = functools.partial(requests.get, url, allow_redirects=True, timeout=10)
            response = await loop.run_in_executor(pool, get_request)
            response.raise_for_status()
            return response.text, url
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None, url

def search_for_keyword_sync(html_content, keyword):
    keyword = keyword.split()
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text().lower()
    for word in keyword:
        if word.lower() in text:
            return True
    return False

async def search_for_keyword(html_content, keyword, loop):
    with ThreadPoolExecutor() as pool:
        return await loop.run_in_executor(pool, search_for_keyword_sync, html_content, keyword)

async def searchG(kw, num):
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool2:
        try:
            urls = await loop.run_in_executor(pool2, search, kw, num)
            event.set()  # Set the event after URLs are fetched
            return urls
        except Exception as e:
            print(f"Error during Google search: {e}")
            return []

async def scrape_for_keyword(keyword, num_results=10):
    query = f"landing page {keyword}"
    found_pages = []

    urls = await searchG(keyword, num_results)  # Properly await the searchG function

    html_content_tasks = [fetch_page_content(url) for url in urls]
    html_contents = await asyncio.gather(*html_content_tasks)  # Properly await the fetch tasks

    loop = asyncio.get_event_loop()
    for html_content, url in html_contents:
        if html_content:
            keyword_found = await search_for_keyword(html_content, keyword, loop)
            if keyword_found:
                found_pages.append(url)  # Append the URL instead of a snippet of the page content

    return found_pages

if __name__ == '__main__':
    import time

    start = time.perf_counter()
    # Specify the keyword to search for
    keyword = sys.argv[1]

    # Specify the number of Google search results to check
    num_results = int(sys.argv[2]) if len(sys.argv) > 2 else 10

    landing_pages = asyncio.run(scrape_for_keyword(keyword, num_results))

    print(f"Found {len(landing_pages)} landing pages containing the keyword '{keyword}':")
    for page in landing_pages:
        print(page)
    print(f'{time.perf_counter() - start:.5f}s')
