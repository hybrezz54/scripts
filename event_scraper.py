import sys
import requests
from bs4 import BeautifulSoup
# from oauth2client import client
# from googleapiclient import sample_tools

urls = [
    'http://web.carychamber.com/events?oe=true'
]

def main():
    # iterate over urls
    for url in urls:
        # download html
        print(f'Downloading page {url}...')
        resource = requests.get(url)
        resource.raise_for_status()

        # parse html
        soup = BeautifulSoup(resource.text, 'html.parser')

# check if main thread
if __name__ == '__main__':
    main()