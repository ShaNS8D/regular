from pprint import pprint
import re

## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

contacts_list_my = []
for x in contacts_list:
    res = " ".join(x[:3])
    pattern = "\w+"
    result = re.findall(pattern, res)
    if len(result) < 3:
        result.append("")
    contacts_list_my.append(result + x[3:])    
    

for x in range(len(contacts_list_my)):
    pattern = r"(\+7|8)?\s*\(*(\d{3})\)*[\s-]*(\d+)[\s-]*(\d{2})[\s-]*(\d{2})\s*\(*(доб\.\s*\d{4}|)\)*"
    subst = r"+7(\2)\3-\4-\5 \6"
    result = re.sub(pattern, subst, contacts_list_my[x][5])
    contacts_list_my[x][5] = result

index_list = []
contacts_my = []
for j in range(len(contacts_list_my)):
    for n in range(len(contacts_list_my)):
        if ((n > j) and (contacts_list_my[j][0] == contacts_list_my[n][0])
            and (contacts_list_my[j][1] == contacts_list_my[n][1])):
            lastname = contacts_list_my[j][0]
            firstname = contacts_list_my[j][1]
            res1 = " ".join(set([contacts_list_my[j][2], contacts_list_my[n][2]]))
            surname = res1.strip()
            res2 = " ".join(set([contacts_list_my[j][3], contacts_list_my[n][3]]))
            organization = res2.strip()
            res3 = " ".join(set([contacts_list_my[j][4], contacts_list_my[n][4]]))
            position = res3.strip()
            res4 = " ".join(set([contacts_list_my[j][5], contacts_list_my[n][5]]))
            phone = res4.strip()
            res5 = " ".join(set([contacts_list_my[j][6], contacts_list_my[n][6]]))
            email = res5.strip()
            contacts_my.append([[j, n],[lastname, firstname, surname, organization, position, phone, email]])

for k in range(len(contacts_list_my)):
    for m in range(len(contacts_my)):
        if k == contacts_my[m][0][0]:
            contacts_list_my[k] = contacts_my[m][1]

rev = list(reversed(contacts_my))

for m in range(len(rev)):
    contacts_list_my.pop(rev[m][0][1])

# 2. Сохраните получившиеся данные в другой файл.
# Код для записи файла в формате CSV:
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  
# Вместо contacts_list подставьте свой список:
  datawriter.writerows(contacts_list_my)