# Тут не было примера вывода функции, так что я сделала функцию, осуществляющую
# только сам перевод и выброс ошибки, не вывод


def covertTemperature(temp, typeTemp='C'):
    if str(typeTemp).lower() != 'c' and str(typeTemp).lower() != 'f':
        return 'IncorrectType'
    try:
        return (lambda temp: (float(temp) - 32) / 1.8 if typeTemp.lower() == 'f' else float(temp) * 1.8 + 32)(temp)
    except ValueError:
        return 'IncorrectTemp'


print("Температура равна %.2f цельсия" % (covertTemperature(10, 'f')))
print("Температура равна %.2f фаренгейта" % (covertTemperature(-12.22, 'c')))
print(covertTemperature('dfgdfh', 'c'))
print(covertTemperature('dfgdfh', 546))
