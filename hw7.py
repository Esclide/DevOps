filePasswd = open('/etc/passwd', 'r')

dictShells = {}
dictUID = {}
for line in filePasswd:
    # Информация об оболочках
    shell = line.split(':')[6].strip('\n')
    dictShells.update({shell: dictShells.get(shell, 0) + 1})

    # Информация об UID
    dictUID[line.split(':')[0]] = line.split(':')[2]


strShells = str(dictShells).strip('{, }').replace(',', ';')
filePasswd.close()

fileGroup = open('/etc/group', 'r')

strGroups = ''
for line in fileGroup:
    if line.split(':')[3] != '\n':
        strGroups += line.split(':')[0] + ':'
        strUsers = ''
        for user in line.split(':')[3].rstrip('\n').split(','):
            strUsers += dictUID[user] + ', '
        strGroups += strUsers
    else:
        strGroups += line.split(':')[0] + ':' + dictUID.get(line.split(':')[0], 'Не найдено') + ', '


fileGroup.close()

fileOut = open('output.txt', 'w')
fileOut.write(strShells + '\n' + strGroups.rstrip(' ,'))
