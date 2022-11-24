# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11
from decimal import Decimal
number=input('Введите вещественное число: ')

def getSumStr (num):
    sum=0
    for i in range(len(num)):
        if num[i:i+1].isdigit():
            sum+=int(num[i:i+1])
    return sum

def getSumArihmetic (num):
    sum=0
    temp=Decimal(num)
    while (temp!=int(temp)): # избавимся от нецелой части
        temp*=10
    while (temp>0):
        sum+=temp%10
        temp=temp//10
    return int(sum)

print (f'Через строку: {number} -> {getSumStr(number)}')
print (f'Через математику: {number} -> {getSumArihmetic (number)}')




