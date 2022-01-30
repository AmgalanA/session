mas = input('Ввести числа(через пробел): ')
masStrings = mas.split(' ')
for i in range(len(masStrings)):
    if(int(masStrings[i]) % 3 == 0):
        masStrings[i] += '100'