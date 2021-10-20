import csv
import re
with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pattern = r"([а-яёА-ЯЁ]+)[,' ']*([а-яёА-ЯЁ]+)[,' ']*([а-яёА-ЯЁ]*)[,' ']*([а-яёА-ЯЁ]*)[,' ']*(\D*),"
pattern2 = r"(\+7|8)?\s*\(?(\d{3})\)?\s*(\d{3})\-*(\d{2})\-*(\d*)[\s\(]*([\w\.]*)\s*(\d*)\)?"
subst = r"\1, \2, \3, \4, \5, "
subst2 = r"+7(\2)\3-\4-\5 \6\7"
result_list1 = []
result_list = []
dict = {}

for i in contacts_list:
  str = ",".join(i)
  result =re.sub(pattern, subst, str)
  result2 = re.sub(pattern2, subst2, result)
  date = result2.split(",")
  result_list1.append(date)

for i in result_list1:
  name = i[0] + i[1]
  if name  not in dict:
    dict[name] =i[2:len(i)]
  else:
    list = dict[name] + i[2:len(i)]
    dict[name]=list

for key in dict:
  person_list = key.split(" ")
  for value in dict[key]:
    if value not in person_list and  value != ' ' and value != '':
      person_list.append(value)
  i = ",".join(person_list)
  res = re.sub(pattern, subst, i)
  res_list = res.split(",")
  result_list.append(res_list)#

with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(result_list)