# Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать!
# Реализовать свой метод
from random import randint
n=int(input('Введите длину списка: '))
list=[randint(0,100) for i in range (n)]

def myShuffle(oldList):
    length=len(oldList)
    tempList=[i for i in range (length)] #Сделаем список индексов, элементы по которым еще не мешали
    newList=[None]*length
    for i in range(length):
        tempIndex=randint(0,len(tempList)-1) #Случайный индекс из списка неперемешанных
        newList[tempList[tempIndex]]=oldList[i]
        del tempList[tempIndex]
    return newList



print (f'Изначальный список:  {list}\nПеремешенный список: {myShuffle(list)}')

