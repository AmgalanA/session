string = input('Input string: ')
if(string[0] == 'a'):
    # оканчивается на а
elif(string[string.length - 1] == 'w'):
    # оканчивается на w
elif(string[string.length - 1] == string[0]):
    # пункт в
elif(string.includes('d')):
    # пункт г

amountOfL = 0
for i in range(len(string)):
    if(string[i] == 'l'):
        amountOfL += 1
if(amountOfL == 3):
    # пункт д

shortestLength = 100
shortestLengthString = ''
arrayOfStrings = string.split(',')
for i in range(len(arrayOfStrings)):
    if(len(arrayOfStrings[i]) < shortestLength):
        shortestLengthString = arrayOfStrings[i]