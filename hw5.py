inputString = input("Пожалуйста, введите целые неотрицательные числа: ")
textList = inputString.split(" ")
numbersList = [int(item) for item in textList]

numbersList.sort()
ifFounded = False
for i in range(1, numbersList[len(numbersList) - 1]):
    if numbersList.count(i) == 0:
        ifFounded = True
        print(i)
        break
if not ifFounded:
    print(numbersList[len(numbersList) - 1] + 1)
