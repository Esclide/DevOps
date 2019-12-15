def CreateDictFromList(inputList):
    dict = {}
    for el in inputList:
        if el not in dict:
            dict.setdefault(el, 1)
        else:
            dict[el] += 1
    return dict


def GetMaxValueFromDict(dict):
    listCounts = list(dict.values())
    listCounts.sort(reverse=True)
    return listCounts.pop(0)


def GetStringKeysByValue(dict, value):
    string = ""
    for key in dict:
        if dict[key] == value:
            string += str(value) + " - " + str(key) + "\n"
    return string


textString = (input("Пожалуйста, введите текст: ")).lower()
textList = textString.split(" ")
tempDict = CreateDictFromList(textList)
maxCount = GetMaxValueFromDict(tempDict)
print(GetStringKeysByValue(tempDict, maxCount))
