import argparse
import time
import os
from urllib.parse import urlparse
import requests
from docx import Document
from zapv2 import ZAPv2

def is_zap_running(zap_api_url):
    try:
        print("Checking if Zaproxy is reachable")
        response = requests.get(zap_api_url, timeout=1)
        if response.status_code == 200:
            print(f"Zaproxy is running, starting spider")
            return True
        else:
            print(f"Zaproxy is not reachable, unexpected response code: {response.status_code}")
            return False
    except requests.RequestException:
        print(f"Zaproxy is not reachable, is zaproxy running? Check the connection to {zap_api_url}")
        return False


def parse_args():
    parser = argparse.ArgumentParser(description="ZAP Scanner Script")
    parser.add_argument('target_url', help="Target URL to scan")
    parser.add_argument('-o', '--output', help="Output HTML file")
    parser.add_argument('-t', '--theme', help="console","construction","corporate","marketing","mountain","nature","ocean","plutonium","skyline","technology"
    return parser.parse_args()


def main():
    args = parse_args()

    # Set your ZAP API key
    api_key = 'qgcj67di7jptu64od9h6j4ocba'

    # Set ZAP API URL
    zap_api_url = 'http://localhost:8080'

    # Set current dir

    cwd = os.getcwd()

    # Check if ZAP is running
    if not is_zap_running(zap_api_url):
        return


    # Instantiate ZAP object
    zap = ZAPv2(apikey=api_key, proxies={'http': zap_api_url, 'https': zap_api_url})

    # Start a new ZAP session
    zap.core.new_session('example_session', overwrite=True)

    # Set the target URL from the command-line argument
    target_url = args.target_url

    parsed_url = urlparse(target_url)

    # Start spidering
    zap.spider.scan(target_url)

    # Wait for spider to finish
    while True:
        spider_status = zap.spider.status(target_url)
        print(f"Spider status: {spider_status}%")
        if spider_status == '100':
            break
        time.sleep(1)

    # Start active scanning
    zap.ascan.scan(target_url)

    # Wait for active scan to finish
    while True:
        ascan_status = zap.ascan.status(target_url)
        print(f"Active Scan status: {ascan_status}%")
        if ascan_status == '100':
            break
        time.sleep(1)


    # Fetch vulnerabilities using zaproxy api
    requests.get(f'{zap_api_url}/JSON/reports/action/generate/?apikey={api_key}&title={parsed_url.netloc} Scan Report&template=modern&theme=nature&description=&contexts=&sites=&sections=chart%7Calertcount%7Cinstancecount%7Calertdetails%7Cstatistics%7Cparams&includedConfidences=Low%7CMedium%7CHigh%7CConfirmed&includedRisks=Low%7CMedium%7CHigh&reportFileName={parsed_url.netloc}.html&reportFileNamePattern=&reportDir={cwd}&display=false')
    print(f"The report has been saved to {parsed_url.netloc}.html")

if __name__ == "__main__":
    main()
