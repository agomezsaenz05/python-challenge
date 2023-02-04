import os
import csv

# full path
    # C:\Users\agomez1\Desktop\SMU Bootcamp\python-challenge\PyBank\Resources\budget_data.csv
# Relative path
    #PyBank\Resources\budget_data.csv

absolute_path = os.path.dirname(__file__)
csv_path = os.path.join(absolute_path,'Resources', 'budget_data.csv')

# Read csv

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f'CSV Header: {csv_header}')

    for row in csvreader:
        print(row)

# Convert Date column to datetime object
csvfile['Date']=pd.to_datetime(csvfile['Date'])

# Extract year and month from Date column
csvfile['Year']
csvfile['Date'].dt.year
csvfile['Month']= csvfile['Date'].dt.month



