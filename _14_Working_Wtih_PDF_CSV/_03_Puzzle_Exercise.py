import csv

data = open("find_the_links.csv", encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)

index = 0
word = ""
for line in data_lines:
    word += line[index]
    index += 1


print(word)

"""
link_list = []
for row_num,data in enumerate(data_lines):
    link_list.append(data[row_num])
"""
