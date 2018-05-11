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
        appt_type = str(row['Appt Type']).lower()
        comment = str(row['Comments']).lower()

        # search appropriate columns and append new column
        if 'fbw' in appt_type or 'fbw' in comment or 'fasting' in comment:
            df.loc[idx, 'Message #'] = 2
        else:
            df.loc[idx, 'Message #'] = 1

    # reformat appt time
    df['Appt DateTime'] = pd.to_datetime(df['Appt DateTime'])
    df['Appt DateTime'] = df['Appt DateTime'].apply(lambda x: x.strftime('%m/%d/%Y %H:%M').lstrip("0").replace(" 0", " "))

    # write to csv file
    df.to_csv(file, index=False, date_format='')

def main():
    # try processing file
    try:
        # get the filename
        file = sys.argv[1]

        # exit if doesn't exist
        if not os.path.exists(file):
            print('File does not exist!')
            return

        # exit if not confirmed
        if input('Confirm processing file? ')[0].lower() != 'y':
            return
        
        # continue processing
        print('Processing ' + file)
        process_file(file)
        print('Done!')

    except IndexError:
        print('Usage: call_reminder.py [file.csv]')

# check if main thread
if __name__ == '__main__':
    main()