"""Look up recycling and holiday trash schedule.

The trash_schedule module will allow the user to retreive
the recycling collection schedule and be notified of any changes 
in the trash collection schedule due to holidays.
"""

import re
from datetime import datetime
import requests
import io
from bs4 import BeautifulSoup
import PyPDF2

# URL for main site of schedule
BASE_URL = "http://www.townofcary.org"

# URL for the recycling schedule
RECYCLING_URL = "http://www.townofcary.org/services-publications/garbage-recycling-yard-waste/recycling"

# URL for the holiday schedule
HOLIDAY_URL = "http://www.townofcary.org/services-publications/garbage-recycling-yard-waste/garbage-collection/holiday-schedule"

# the current date
today = datetime.now()

def main():
    """Executes the main logic of the script."""

    # Process recycling results
    process_recycling()

    # Process holiday results
    process_holiday()

def process_recycling():
    """Obtains the results for the correct recycling schedule."""

    # download html for recycling schedule
    print(f'Downloading page {RECYCLING_URL}...')
    resource = requests.get(RECYCLING_URL)
    resource.raise_for_status()

    # parse html
    soup = BeautifulSoup(resource.text, 'html.parser')

    # get correct schedule from user
    week = input("Type 'b' for Blue Week and 'y' for Yellow Week: ")[0].lower()

    # parse input
    if week == 'b':
        week = 'Blue'
    elif week == 'y':
        week = 'Yellow'
    else:
        raise ValueError("Input must be 'b' or 'y'!")

    # iterate over matched links
    for link in soup.find_all('a', text=re.compile(f'({week})+')):
        # check if contains appropriate year
        if str(today.year) in link.text:
            # process pdf
            resource = requests.get(BASE_URL + link.get('href'))
            stream = io.BytesIO(resource.content)
            pdf = PyPDF2.PdfFileReader(stream)
            # TODO parse PDF
            print(pdf.getPage(0).extractText())
            

def process_holiday():
    """Obtains the results for the holiday schedule."""

    # download html for holiday schedule
    print(f'Downloading page {HOLIDAY_URL}...')
    resource = requests.get(HOLIDAY_URL)
    resource.raise_for_status()

    # parse html
    soup = BeautifulSoup(resource.text, 'html.parser')

    # iterate over holiday changes
    for item in soup.find_all('li', text=re.compile('(Monday|Tuesday|Wednesday|Thursday|Friday)+')):
        # check if contains appropriate month
        if str(today.month) in item.text:
            print(item.text.strip(' ;'))

# check if main thread
if __name__ == '__main__':
    main()