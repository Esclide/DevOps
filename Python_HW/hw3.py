textList = (input("Пожалуйста, введите текст: ")).lower().split(" ")

dictWords = {}

for el in textList: dictWords.update({el: dictWords.get(el, 0) + 1})
maxValue = max(list(dictWords.values()))
for key in dictWords:
    if dictWords[key] == maxValue: print(str(key) + ' - ' + str(maxValue))
