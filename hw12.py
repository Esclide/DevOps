

def fibRecursion(n):
    if n in (1, 2):
        return 1
    return fibRecursion(n - 1) + fibRecursion(n - 2)

def fibIterat(n):
    fib1=fib2=fibSum=1
    i = 2
    while i < n:
        fibSum = fib2 + fib1
        fib1 = fib2
        fib2 = fibSum
        i += 1
    return fibSum

def fibArray(n):
    listFib = [1, 1]
    for i in range(2, n):
        listFib.append(listFib[i - 1] + listFib[i - 2])

    return listFib[len(listFib)-1]

def fibTail(n, a = 0, b = 1):
    if n == 0:
        return a
    if n == 1:
        return b
    return fibTail(n - 1, b, a + b);

def printMethodsCompare(n):
    import time
    print ("results for {} number:".format(n))
    startTime = time.time()
    print(">By recursion method: \n{}".format(fibRecursion(n)))
    print("Elapsed time: {:.6f} sec".format(time.time() - startTime))
    startTime = time.time()
    print(">By iteration method: \n{}".format(fibIterat(n)))
    print("Elapsed time: {:.6f} sec".format(time.time() - startTime))
    startTime = time.time()
    print(">By tail recurssive method: \n{}".format(fibTail(n)))
    print("Elapsed time: {:.6f} sec".format(time.time() - startTime))
    startTime = time.time()
    print(">By array method: \n{}".format(fibArray(n)))
    print ("Elapsed time: {:.6f} sec\n".format(time.time() - startTime))



printMethodsCompare(38)
printMethodsCompare(10)