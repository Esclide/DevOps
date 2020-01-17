textString = input("Пожалуйста, введите текст: ")
textList = textString.split(" ")
textSet = set(textList)  # Если использовать set

# Если добавлять в список через словарь
tempDict = {}
textListWithoutDuplicates = [tempDict.setdefault(el, el) for el in textList if el not in tempDict]

print("С сохранением порядка: ")
for el in textListWithoutDuplicates:
    print(el, end=' ')
print("\nБез сохранения порядка: ")
for el in textSet:
    print(el, end=' ')
