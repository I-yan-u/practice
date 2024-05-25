import whois
import requests

def check_domain(domain):
    try:
        # Perform WHOIS lookup
        w = whois.whois(domain)
        # If the domain has a creation date, it's registered
        if w.creation_date:
            return True
    except Exception:
        return False
    return False

def is_live(domain):
    try:
        # Perform HTTP GET request
        response = requests.get(f"http://{domain}", timeout=5)
        # Check if the status code indicates a successful response
        if response.status_code == 200:
            return True
    except requests.RequestException:
        return False
    return False

def check_domains(base_domain, extensions):
    results = {}
    for ext in extensions:
        domain = f"{base_domain}.{ext}"
        if check_domain(domain):
            live = is_live(domain)
            results[domain] = 'Live' if live else 'Registered but not live'
        else:
            results[domain] = 'Available'
    return results

# List of extensions to check
extensions = ["com", "net", "org", "info", "biz"]

# Base domain to check
base_domain = "google"  # Change this to your base domain

results = check_domains(base_domain, extensions)
for domain, status in results.items():
    print(f"{domain}: {status}")
