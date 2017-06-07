import csv

with open('csvs/ripper2.csv', 'r') as csvfile:
    our_reader = csv.reader(csvfile)
    cases = [row for row in our_reader]

case_files = [row[4] for row in cases]
print(case_files)

for case_files in cases:
    str.lower(case_files)
print(case_files)


#for case in cases[4]:
#    case.lower()

#print(cases[4])
