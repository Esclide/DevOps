inputString = input("Пожалуйста, введите целые неотрицательные числа: ")
textList = inputString.split(" ")
numbersList = [int(item) for item in textList]


numbersList.sort()
for i in range (1, len(numbersList)-1):
    if numbersList.count(i) == 0:
        print(i)
        break
