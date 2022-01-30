import random
m = int(input('m: '))
n = int(input('n: '))
if(n > 0):
    if(m // n == 0 or n // m == 0):
        print(1)
    else:
        print(random.randint(1, 100000000000000000))