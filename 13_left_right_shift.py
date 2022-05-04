
#Left shifting the first number by the second

#LEFT SHIFTING MEANS mulitply by 2
def left_shift(a, b):
    a = list(bin(a).replace('0b', ''))
    while b:

        a.append('0')
        b = b - 1
        
    final = ''
    for x in a:
        final =final+x
    return int(final, 2)

# MENU
print('***** SHIFTS *****')
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

print(f"a << b = {left_shift(a, b)}")



        

