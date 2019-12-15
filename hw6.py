import time
start_time = time.clock()

def IfPalinromic(number):
    numberList=list(str(number))
    numberListReverse=numberList.copy()
    numberListReverse.reverse()
    for i in numberListReverse:
        if i=="0":
            numberListReverse.pop(0)
        else:
            break
    if ''.join(numberList) == ''.join(numberListReverse):
        return True
    else:
        return False




sum=0
for i in range (0,1000000):
    if IfPalinromic(i) and IfPalinromic(str(bin(i))[2::]):
        print (i," ",int(str(bin(i))[2::]))
        sum+=i

print ("===============================")
print("Общая сумма чисел: ",sum)
print ("Время выполнения программы: {:g} s".format(time.clock() - start_time))