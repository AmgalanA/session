# a 
x = int(input('x: '))
y = int(input('y: '))
if(x <= 8 and x >= -8 and y <= 4 and y >= 0):
    # принадлежит
    print('Принадлежит')
else:
    print('Не принадлежит к пункту a')

# b
if(x <= 8 and x >= 3 and ((y <= 5 and y >= 3) or (y >= -5 and y <= -3))):
    # принадлежит
    print('Принадлежит')
else:
    print('Не принадлежит к пункту b')
