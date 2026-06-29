import urllib.request

def scrape_proxies():
    print("Starting proxy scraper...")
    url = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"
    
    try:
        # Fetching a public proxy list
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = response.read().decode('utf-8')
            proxies = data.split('\n')
            
            # Print the first 10 proxies as an example
            print("Found Proxies:")
            for proxy in proxies[:10]:
                if proxy.strip():
                    print(proxy.strip())
                    
            print("Scraping completed successfully!")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    scrape_proxies()
