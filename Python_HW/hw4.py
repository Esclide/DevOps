inputString = input("Пожалуйста, введите целые неотрицательные числа: ")+" "


sum=0

tempString=""
for i  in inputString:
    if ord(i)>47 and ord(i)<58:
        tempString+=str(i)
    else:
        if tempString != "" :
            sum+=(int(tempString))
            tempString = ""
print (sum)

# В задании опечатка? Из строки "123dfgdr%0&45ty-45--900" ведь не получить суммированием 777.
# Или я не так задание поняла?