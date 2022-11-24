# Написать программу, которая будет ввыводит в консоль заданный текст
# (Python - один из самых популярных языков программирования в мире),
# затем принимать из консоли шаблон подстроки и удалять в задданом тексте все слова
# в которых присутствует введенный шаблон
# Пример:
# Python - один из самых популярных языков программирования в мире
# Введите подстроку: ам
# Python - один из популярных языков в мире

text='Python - один из самых популярных языков программирования в мире'
print (text)
pattern=input('Введите шаблон подстроки: '))
words=text.split()
goodWords=[]
for word in words:
    goodWord=True
    if len(word)>len(pattern):
        for i in range(len(word)-len(pattern)+1):
            if word[i:i+len(pattern)]==pattern:
                goodWord=False
                break
    if goodWord:
        goodWords.append(word)
print (*goodWords, sep=' ')

