import csv

with open('csvs/basic.csv', 'r') as csvfile:
    our_reader = csv.reader(csvfile)
    names = [row for row in our_reader]

print(names[2][3])

len(names)

for row in names:
    print(len(row[3]))

longest = ""
for row in names:
    if len(row[1]) > len(longest):
        longest = row[1]
print(longest)

last_names = [row[1] for row in names]
last_names.reverse()
print(last_names)

new_row = [2, 'wayne', 'graham', 'meh']
names.append(new_row)
print(names)

new_row = [3, 'Mahoney-Steel', 'Tamsyn', 'freaking awesome']
names.append(new_row)
print(names)

a_row = [4, 'fox', 'eliza', 'SO COOL']
print(names + a_row)

with open('csvs/practice.csv', 'w') as fout:
    csvwriter = csv.writer(fout)
    for i in range(0, 100, 10):
        csvwriter.writerow([i, i + 5, i + 10, i + 15, i + 20, i + 25, i + 30])

with open('csvs/practice1.csv', 'w') as fout:
    csvwriter = csv.writer(fout)
    for i in range(0, 10):
        csvwriter.writerow([i, i + 1, i + 2, i + 3])
