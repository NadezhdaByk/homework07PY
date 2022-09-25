import re

# data='Петров Петр'
def find_data(data):
    count = 0
    f=open('phone.txt', 'r', encoding='UTF-8')
    all_data=f.read().split('\n')
    for unic in all_data:
        if data in unic:
            num=re.findall(r'\d+', unic)
            return num
            exit()
            count=1
    if count == 0:
        return "Такого контакта нет в вашем справочнике"

    f.close()


# find_data()