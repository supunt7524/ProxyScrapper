import urllib.request

def scrape_proxies():
    print("Starting proxy scraper...")
    url = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = response.read().decode('utf-8')
            proxies = data.split('\n')
            
            with open("proxies.txt", "w") as f:
                for proxy in proxies:
                    if proxy.strip():
                        f.write(proxy.strip() + "\n")
                        
            print("Scraping completed and saved to proxies.txt!")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    scrape_proxies()
