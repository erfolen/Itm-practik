import csv
data_new = []
with open('dataset/bikes.csv') as f:
    data = csv.reader(f)
    for row in data:
        data_new.append(row)
        print(row)

print(data_new)
with open('test.csv', 'a+') as f:
    writer = csv.writer(f)
    writer.writerows(data_new)


with open('test_2.csv', 'a') as f:
    writer = csv.writer(f, delimiter=';')
    for row in data_new:
        writer.writerow(row)
