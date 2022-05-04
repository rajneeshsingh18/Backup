"""
Ques : Write a program to print the values of a 5 bit binary up-down counter. 
User should be able to specify the up or down nature of the counter
"""

def bin_plus_1(n):
    return bin(int(n, 2) + 1)[2::]

def bin_minus_1(n):
    return bin(int(n, 2) - 1)[2::]

def counter(bit, option):
    if option == 'up':
        i = '0' * bit
        for x in range(2 ** bit):
                
            while len(i) != bit:
                i = '0' + i
                
            print(i)
            i = bin_plus_1(i)

    else:
        i = '1' * bit
        for x in range(2 ** bit):
            
            while len(i) != bit:
                i = '0' + i
                
            print(i)
            i = bin_minus_1(i)


# MENU
print('***** BINARY COUNTER *****')
a = int(input('Enter counter nature (\'1\' for up and \'0\' for down): '))
if a:
    counter(5, 'up')
else:
    counter(5, 'down')
