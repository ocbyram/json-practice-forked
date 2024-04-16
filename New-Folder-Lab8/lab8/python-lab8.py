#!/usr/bin

import json

with open('data/schacon.repos.json', 'r') as file:
    data = json.load(file)


for r in data[0:5]:
    data2 = (r['name'], r['html_url'], r['updated_at'], r['visibility'])
    data4 = ','.join(data2)
    file1 = open("chacon.csv", "a")
    file1.write(data4 + '\n')
    file1.close()

final_csv = open("chacon.csv", "r")
print(final_csv.read())