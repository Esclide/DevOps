import time

start_time = time.clock()


def IsPalindrome(number):
    return str(number) == str(number)[::-1]


sum = 0
for i in range(0, 1000000):
    if IsPalindrome(i) and IsPalindrome(format(i, 'b')):
        print(i, " ", int(str(bin(i))[2::]))
        sum += i

print("===============================")
print("Общая сумма чисел: ", sum)
print("Время выполнения программы: {:g} s".format(time.clock() - start_time))
