# Каждая функция соответствует решенной задачи
from functools import reduce


# Special Pythagorean triplet
def problem9():
    print([(a, b, c, 'sum = ' + str(a * b * c)) for a in range(500) for b in range(500) for c in range(500) if
           (a * a + b * b == c * c and a + b + c == 1000)][0])

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


print("problem 9: (Она будет немножко долгой)")
problem9()
print("\nproblem 6:")
problem6()
print("\nproblem 48:")
problem48()
print("\nproblem 40:")
problem40()
