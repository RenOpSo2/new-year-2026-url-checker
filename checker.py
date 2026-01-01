import sys
import time
import requests

def check(url, timeout=5):
    start = time.time()
    try:
        r = requests.get(url, timeout=timeout)
        elapsed = time.time() - start
        print(f"[OK] {url}")
        print(f"Status   : {r.status_code}")
        print(f"Time     : {elapsed:.2f}s")
    except requests.exceptions.Timeout:
        print(f"[TIMEOUT] {url} (> {timeout}s)")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] {url}")
        print(f"Detail   : {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python checker.py <url>")
        sys.exit(1)

    check(sys.argv[1])