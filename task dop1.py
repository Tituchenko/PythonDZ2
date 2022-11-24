# Написать программу, которая состоит 4 из этапов:
# - создает список из рандомных четырех значных чисел
# - принимает с консоли цифру и удаляет ее из всех элементов списка
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# - из финального списка убирает все дублирующиеся элементы
# - после каждого этапа выводить результат в консоль
# Пример:
# - 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
# - 2 этап: Введите цифру: 3
# - 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
# - 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
# - 3 этап: [3, 1, 5, 5, 3, 5, 4]
# - 4 этап: [3, 1, 5, 4]
from random import randint
#Этап 1
n=7
list=[randint(1000,9000) for i in range (n)]
print (f'1 этап: {list}')

#Этап 2
number=int(input('Введите цифру: '))
for i in range (0,len(list)):
    element=str(list[i])
    newElement=''
    for j in range (0,len(element)):
        if int(element[j])!=number:
            newElement+=element[j]
    list[i]=int(newElement)
print (f'2 этап: {list}')

#Этап 3
for i in range (0,len(list)):
    element = str(list[i])
    print(f'    {element}',end='')
    while int(element)>9:
        sum = 0
        print('->', end='')
        for j in range(0, len(element)):
            if j==0:
                print(element[j], end='')
            else:
                print(f'+{element[j]}', end='')
            sum+=int(element[j])
        element=str(sum)
        print(f'->{element}', end='')
    list[i]=int (element)
    print ('')
print (f'3 этап: {list}')

#Этап 4
newList=[]
for i in range (0,len(list)):
    noPovtor=True
    for j in range (0,i):
        if list[j]==list[i]:
            noPovtor=False
            break
    if noPovtor:
        newList.append(list[i])
list=newList
print(f'4 этап: {list}')