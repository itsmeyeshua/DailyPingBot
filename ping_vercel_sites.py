import requests
import datetime
import time

SITES = [
    "https://pomodorfocustimer.vercel.app/",
    "https://quote-generatorfront.vercel.app/",
    "https://alarm-buzzer.vercel.app/",
]

def ping_site(url):
    try:
        response = requests.get(url, timeout=30)
        status = "✓ OK" if response.status_code == 200 else f"⚠ Status {response.status_code}"
        return {
            "url": url,
            "status": status,
            "status_code": response.status_code,
            "response_time": response.elapsed.total_seconds()
        }
    except requests.exceptions.RequestException as e:
        return {
            "url": url,
            "status": f"✗ ERROR",
            "error": str(e),
            "response_time": None
        }

def main():
    print(f"\n{'='*60}")
    print(f"Site Health Check - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}\n")
    
    results = []
    for site in SITES:
        print(f"Pinging {site}...", end=" ")
        result = ping_site(site)
        results.append(result)
        
        if "error" in result:
            print(f"{result['status']}: {result['error']}")
        else:
            print(f"{result['status']} ({result['response_time']:.2f}s)")
        
        time.sleep(1)
    
    print(f"\n{'='*60}")
    successful = sum(1 for r in results if r.get('status_code') == 200)
    print(f"Summary: {successful}/{len(SITES)} sites responding correctly")
    print(f"{'='*60}\n")
    
    return results

if __name__ == "__main__":
    main()