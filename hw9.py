# Каждая функция соответствует решенной задачи
from functools import reduce


# Special Pythagorean triplet
def problem9():
    print([(a, b, 1000-(a+b), 'sum = ' + str(a * b * (1000-(a+b)))) for a in range(500) for b in range(a) if
           a**2 + b**2 == (1000-(a+b))**2 ][0])

    # Можно добавить функцию, вызывающую исключение и завершующую работу функции, если числа нашлись единожды
    # Но задача была, как я поняла, в одну строку сделать


# Sum square difference
def problem6():
    print("Разница равна " + str(sum(a for a in range(100)) ** 2 - sum(a * a for a in range(100))))


# Self powers
def problem48():
    print("Последние 10 цифр суммы: " + str(sum(a ** a for a in range(1000)))[-10:])


# Champernowne's constant
def problem40():
    strNumbers = (str(''.join([str(a) for a in range(1000000)])))
    print(reduce(lambda x, y: int(x) * int(y), [strNumbers[10 ** a] for a in range(7)]))


print("problem 9:")
problem9()
print("\nproblem 6:")
problem6()
print("\nproblem 48:")
problem48()
print("\nproblem 40:")
problem40()
