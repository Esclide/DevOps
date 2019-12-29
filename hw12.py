def fib(n):
    listFib = [1, 1]
    for i in range(2, n):
        listFib.append(listFib[i - 1] + listFib[i - 2])
    return listFib


print(fib(10))
print(fib(100))
