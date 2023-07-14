import csv

total_line = []

with open('string.txt') as new_file:
    for line in new_file:
        obj = line.split()
        total_line.append(obj)

with open('dictionary.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    for line in total_line:
        writer.writerow(line)
