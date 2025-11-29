import urllib.request
import xml.etree.ElementTree as ET
import sys

# --- CONFIG ---
# Default to your local server for testing
DEFAULT_URL = "http://127.0.0.1:4000/sitemap.xml"

# ANSI Colors for the "Hacker" aesthetic
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def check_sitemap(url):
    print(f"{Colors.HEADER}--- CARDSNARK SITEMAP AUDIT ---{Colors.ENDC}")
    print(f"Target: {url}\n")

    try:
        response = urllib.request.urlopen(url)
        data = response.read()
        text = data.decode('utf-8')
    except Exception as e:
        print(f"{Colors.FAIL}CRITICAL ERROR: Could not fetch sitemap.{Colors.ENDC}")
        print(f"Error details: {e}")
        print("Make sure your Jekyll server is running! (bundle exec jekyll serve)")
        return

    # Parse XML
    try:
        root = ET.fromstring(text)
        # Namespace handling (Sitemaps usually have a namespace)
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    except ET.ParseError:
        print(f"{Colors.FAIL}Error: File is not valid XML.{Colors.ENDC}")
        return

    urls = root.findall('ns:url', namespace)
    
    print(f"{Colors.OKCYAN}Found {len(urls)} pages submitted to Google.{Colors.ENDC}\n")

    print(f"{'LAST MODIFIED':<15} | {'URL'}")
    print("-" * 60)

    post_count = 0
    page_count = 0

    for url in urls:
        loc = url.find('ns:loc', namespace).text
        lastmod = url.find('ns:lastmod', namespace)
        
        mod_date = lastmod.text if lastmod is not None else "NO DATE"
        
        # Color coding
        if "NO DATE" in mod_date:
            date_display = f"{Colors.FAIL}{mod_date}{Colors.ENDC}"
        else:
            date_display = f"{Colors.OKGREEN}{mod_date[:10]}{Colors.ENDC}"

        print(f"{date_display:<24} | {loc}")

        if "/reviews/" in loc or "/posts/" in loc:
            post_count += 1
        else:
            page_count += 1

    print("-" * 60)
    print(f"\n{Colors.BOLD}SUMMARY:{Colors.ENDC}")
    print(f"Reviews/Posts: {post_count}")
    print(f"Core Pages:    {page_count}")
    print(f"Total:         {len(urls)}")

    if len(urls) < 3:
         print(f"\n{Colors.WARNING}⚠️  WARNING: Your sitemap looks empty. Did you build the site?{Colors.ENDC}")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_URL
    check_sitemap(target)
             
