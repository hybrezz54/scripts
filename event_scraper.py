import urllib3
from bs4 import BeautifulSoup

# define variables
http = urllib3.PoolManager()

def http_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None
    """
    r = http.request('GET', url)
    data = r.data

    if r.status == 200 and data is not None and data.find('html') > -1:
        return data
    else:
        return None