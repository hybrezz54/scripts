"""Look up recycling and holiday trash schedule.

The trash_schedule module will allow the user to retreive
the recycling collection schedule and be notified of any changes 
in the trash collection schedule due to holidays.
"""

import re
import time
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup

# time in seconds in 1 week
WEEK = 604800

# file for saved data
DATA_FILE = "trash_schedule_data.txt"

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

    # try to access saved data
    try:
        with open(DATA_FILE) as f:
            date = datetime.fromtimestamp(f.readline())

    # prompt user for current week
    except IOError:
        with open(DATA_FILE, 'a') as f:
            if input('Will the recycling be picked up this week? ')[0].lower() == 'y':
                date = datetime.now()
                f.write(time.time())
            else:
                date = datetime.fromtimestamp(time.time() + WEEK)
                f.write(time.time() + WEEK)

    # clean dates
    current = datetime.now()
    current = current - timedelta(days=current.weekday())
    date = date - timedelta(days=date.weekday())

    # calculate when next recycling week
    weeks = (current - date).days / 7
    if (weeks % 2) == 0:
        print('The recycling will go this week!')
    else:
        print('The recycling will go next week!')

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