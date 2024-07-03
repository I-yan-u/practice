import asyncio
import whois
from concurrent.futures import ThreadPoolExecutor
import aiohttp
import time
import sys

async def check_domain(domain):
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        try:
            w = await loop.run_in_executor(pool, whois.whois, domain)
            return bool(w.creation_date)
        except Exception as e:
            return False

async def is_live(domain):
    url = f"http://{domain}"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, allow_redirects=True, timeout=5) as response:
                return response.status == 200
    except asyncio.TimeoutError:
        print(f"Timeout occurred for {domain}")
        return False
    except aiohttp.ClientError as e:
        print(f"HTTP error occurred for {domain}: {e}")
        return False

async def check_domain_status(base_domain, extensions):
    tasks = [check_and_get_status(f"{base_domain}.{ext}") for ext in extensions]
    results = await asyncio.gather(*tasks)
    return dict(results)

async def check_and_get_status(domain):
    if await check_domain(domain):
        live = await is_live(domain)
        return (domain, 'Live' if live else 'Registered but not live')
    else:
        return (domain, 'Available')

async def main():
    extensions = ["com", "net", "org", "info", "biz", "io", "co", "us", "ca", "xyz", "co.uk", "com.au"]
    base_domain = sys.argv[1] or 'example'  # Change this to your base domain

    results = await check_domain_status(base_domain, extensions)
    for domain, status in results.items():
        print(f"http://{domain}: {status}")
        if len(sys.argv) > 2 and sys.argv[2] == 'save':
            with open(f'check-{sys.argv[1]}.txt', 'a+') as file:
                file.write(f"http://{domain}: {status}\n")
    if len(sys.argv) > 2 and sys.argv[2] == 'save':
        print(f"Results saved to check-{sys.argv[1]}.txt")


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    print(f"Time taken: {time.perf_counter() - start:.2f} seconds")