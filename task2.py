# Задайте список из n чисел последовательности (1 + 1/n)^n.
# Вывести в консоль сам список и сумму его элементов.
from decimal import Decimal
n=int(input('Введите N: '))
sum=0
list=[]
for i in range (1,n+1):
    temp=Decimal((1+1/i)**i)
    list.append(temp)
    sum+=temp
print (f'Список: {list}\nСумма: {sum}')