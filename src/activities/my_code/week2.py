# Section 1: Locating files

from pathlib import Path

paralympics_data_file_csv = Path(__file__).parent.parent.joinpath('data', 'paralympics_raw.csv')

''' #Using importlib
from importlib import resources

from activities import data

paralympics_data_file_csv = resources.files(data).joinpath("paralympics_raw.csv")
'''
''' #This section checks the csv file

import csv

if __name__ == '__main__':
        data_file =  paralympics_data_file_csv

with open(data_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    first_row = next(csv_reader)
    print(first_row)
'''

# Section 2:
