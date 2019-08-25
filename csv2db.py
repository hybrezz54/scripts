#!/usr.bin/python
# script to import csv data into a database (e.g. Postgres)

import configparser
import argparse, sys, os
from sqlalchemy import create_engine
import pandas as pd

CHUNKSIZE = 100000
HEADERS = ['id', 'time', 'data'] # example headers; need to allow user to specify

def main():
    # init parser
    parser = argparse.ArgumentParser(description='Parses and stores csv files in a SQL database')
    parser.add_argument('input', metavar='input', type=str, nargs=1, help='csv file or directory containing csv files')
    parser.add_argument('-c', '--cred', nargs=1, help='credentials file for db; will use db_creds.ini by default')

    # read args from cmdline
    args = parser.parse_args()
    inpt = os.path.abspath(args.input[0])

    # process credentials file
    cred = os.path.abspath(args.cred[0]) if args.cred \
        else os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db_creds.ini')
    config = configparser.ConfigParser()
    config.read(cred)

    # create engine
    url = f"{config['CREDS']['TYPE']}://{config['CREDS']['USER']}:{config['CREDS']['PW']}@{config['CREDS']['HOST']} \
        :{config['CREDS']['PORT']}/{config['CREDS']['DB']}"
    url = url.replace(' ', '')
    engine = create_engine(url)

    # reade and store csv file(s)
    if inpt.endswith('.csv'):
        read_store(input, HEADERS, engine)
    else:
        dir = os.fsencode(inpt)
        for file in os.listdir(dir):
            filename = os.fsdecode(file)
            if filename.endswith('.csv'): read_store(os.path.join(inpt, filename), HEADERS, engine)

def read_store(file, headers, conn):
    # read csv file in chunks
    for chunk in pd.read_csv(file, chunksize=CHUNKSIZE, names=headers):
        chunk = chunk.rename(columns={c: c.replace(' ', '') for c in chunk.columns})
        chunk.to_sql('raw_sensor_data', conn, if_exists='append')

if __name__ == '__main__':
    main()