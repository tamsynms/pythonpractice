import csv
import time

with open('csvs/ripper.csv', 'r') as csvfile:
    our_reader = csv.reader(csvfile)
    cases = [row for row in our_reader]

print(cases[0])

dates = [row[3] for row in cases]
print(dates)
