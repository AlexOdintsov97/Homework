'''Напиши код, который принимает на вход строку, в этой строке чётное кол-во слов, 
разделенных пробелами(2, 4, 6, 8 или больше слов). 
Сформируй словарь таким образом, чтобы нечетное слова были ключами словаря, 
а четные - значениями по этим ключам.

Пример:
    Введите строку: name Petr phone 432 balance 50000
    Программа печатает: {'name': 'Petr', 'phone': 432, 'balance': 50000}

Если кол-во слов нечетное - программа игнорирует последнее слово
'''
user = input('Введите строку: ').split()
users = user
a = []
b = []
count = 0
if len(users) %2 == 1:
    del users[-1]
while count < len(users):
    if count %2 == 0 :
        c = users[count]
        a.append(c)       
        count += 1
    if count %2 == 1:
        e = users[count]
        b.append(e)
        count += 1
distionary = dict(zip(a,b))
distionary['special_key'] = 12
print(distionary)
print(users)
  

   