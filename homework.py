'''name = input("Введите свое имя: ")
def inp_name(name : str): 
    """эта функция выводит имя которое вводит пользователь. В структуре функции
находится еще одна функция которая приветсвтует пользователя
"""
    print(name)
    def say_my_name(name):
        print(f"Привет, {name}")
    say_my_name(name)
    
inp_name(name)'''



#task2
'''user_car = input("введите машину: ")
cars = ['BMW', "Lada", 'Mercedes']
def get_car(car = "BMW"):
    if user_car in cars:
        print("К вам приедет: ", user_car)
    else:
        print("Такой машины у нас нету к Вам приедет:", car)
        
get_car()'''

#task3
'''Напиши функцию get_next_number, которая принимает на вход целое положительное число и 
возвращает первое четное число, большее заданного, и функцию is_even_number, которая проверяет, 
является ли переданное ей число четным.'''
'''num = int(input("Введите число: "))
def get_next_number(num):
    """эта функция принимает число и делает проверку положительное ли число,если нет тогда меняет
    знак на положительный, если да тогда проходит проверку нечетное ли число, если нечетное тогда 
    к числу добавляется +1, если число четное к нему прибавляется +2. Эта функция выводит первое 
    положительное четное число после заданного"""
    if num < 0:
        num = -num
    if num > 0:
        if num %2 == 1:
            num += 1
            
        elif num %2 == 0:
            num += 2

    return num
print("введенное пользователем число",num)
print("Число после функции :", get_next_number(num))
def is_even_number(num):
    """эта функция проверяет правильно ли работает первая функция: если на вход приходит положительное
    число выводится True если же  первая функция не сработала, и вывела нечетное число - False """
    if get_next_number(num) % 2 == 0:
        return True
    else:
        return False


print("Является ли число четным", is_even_number(num))'''

# Задача 4
"""Напиши функцию is_password_hard, которая принимает на вход пароль и возвращает True, 
если он надёжный или False в противном случае.
Надёжным считаем пароль, длина которого 12 и больше символов, 
который содержит хотя бы 1 букву в большом регистре, хотя бы 1 букву в маленьком регистре и хотя бы одну цифру."""
'''password = input("Придумайте пароль: ")

def is_password_hard(password):
    """"эта функция принипает от перменной password строку, в цикле считает колличество символов в верхнем, нижнем
    регистре, число, и длину пароля не менее 12 символов. Эта функция возвращает True или False
        """
    pas_int = 0
    pas_lower = 0
    pas_up = 0
    for i in password:
        if 'a' <= i <= 'z':
            pas_lower += 1
        if "0" <= i <= "9":
            pas_int += 1 
        if 'A' <= i <= 'Z':
            pas_up += 1
    if pas_up and pas_int and pas_lower > 0 and len(password) > 12 :
        print(True)
    else: 
        print(False)
is_password_hard(password)
'''