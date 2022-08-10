# task1
'''number = int(input())
max_num = number%10
number = number//10
while number > 0:
    if number%10 > max_num:
        max_num = number%10
    number = number//10
print(max_num)'''

#task2

'''import random
number = random.sample(range(1, 99), 10 )
num_max = number[0]
num_min = number[0]
for num in number:
    if num_max < num:
        num_max = num 
    if num_min > num:
        num_min = num    
print("максимальное число:", num_max)
print("Минимальное число:", num_min)
print("Разница между мах и min:", num_max - num_min)
print("Числа из рандом", number)'''

'''task3
import random
number = random.sample(range(1, 99), 10 )
num_first = number[0]
num_second = number[0]
for num in number:
    if num_first < num:
        num_first = num 
for num in number:        
    if num_first < num and num_first != num_second:
        num_second = num
print("первое число:", num_first)
print("второе число:", num_second)
print("Сумма чисел:", num_first + num_second)
print("Числа из рандом", number)'''