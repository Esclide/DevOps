def Collats(num, counter):
    if num == 1:
        return counter
    else:
        return Collats((lambda x: x / 2 if (x % 2 == 0) else x * 3 + 1)(num), counter + 1)


print("Необходимое число шагов: " + str(Collats(12, 0)))
