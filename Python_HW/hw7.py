filePasswd = open('/etc/passwd', 'r')

dictShells = {}
dictUID = {}
dictGUID = {}
for line in filePasswd:
    # Информация об оболочках
    shell = line.split(':')[6].strip('\n')
    dictShells.update({shell: dictShells.get(shell, 0) + 1})

    # Информация об UID
    dictUID[line.split(':')[0]] = line.split(':')[2]
    dictGUID[line.split(':')[2]] = line.split(':')[3]

strShells = str(dictShells).strip('{, }').replace(',', ';')
filePasswd.close()

fileGroup = open('/etc/group', 'r')

strGroups = ''
for line in fileGroup:
        counter = 0
        strGroups += line.split(':')[0] + ':'
        strUsers = ''
        for key,value in dictGUID.items():
            if value == line.split(':')[2]:
                strUsers += key + ', '
                counter = 1
        strGroups += strUsers
        if line.split(':')[3] != '\n':
            strUsers = ''
            for user in line.split(':')[3].rstrip('\n').split(','):
                strUsers += dictUID[user] + ', '
            strGroups += strUsers
            counter = 1
        if counter == 0:
            strGroups += "отсутствует, "

fileGroup.close()

fileOut = open('output.txt', 'w')
fileOut.write(strShells + '\n' + strGroups.rstrip(' ,'))
