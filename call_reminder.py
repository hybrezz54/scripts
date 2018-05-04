import os.path
import sys
import pandas as pd

def process_file(file):
    """
    Reads in the csv file and processes it by appending a column to indicate
    whether a fasting call message should be sent to the patient
    """
    # read in csv file
    df = pd.read_csv(file)

    # iterate over rows
    for idx, row in df.iterrows():
        appt_type = row['Appt Type'].lower*()
        comment = row['Comments'].lower()

        # search appropriate columns and append new column
        if 'fbw' in appt_type or 'fbw' in comment or 'fasting' in comment:
            row['Message #'] = 2
        else:
            row['Message #'] = 1

    df.to_csv(file)

# check if main thread
if __name__ == '__main__':
    # try processing file
    try:
        # get the filename
        file = sys.argv[1]

        # exit if doesn't exist
        if not os.path.exists(file):
            print('File does not exist!')
            return

        # exit if not confirmed
        if input('Confirm processing file')[0].lower() != 'y':
            return
        
        # continue processing
        print('Processing ' + file)
        process_file(file)
        print('Done!')

    except IndexError:
        print('Usage: call_reminder.py [file.csv]')