def inputProcessing():
    inputString = input()
    if inputString == 'cancel':
        print("Bye")
        return ()
    try:
        strOut = lambda inputNumber: int(inputNumber / 2) if inputNumber % 2 == 0 else inputNumber * 3 + 1
        print (strOut(int(inputString)))
        inputProcessing()
    except ValueError:
        print("Не удалось преобразовать введенный текст в число.")
        inputProcessing()


inputProcessing()
