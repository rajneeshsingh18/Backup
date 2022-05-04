"""
Ques 1. Write  a program to convert an unsinged number in one radix 'A'
        to the equivalent number in another radix 'B' where A and B can be any positive interger.
"""

#From decimal to anybase or radix 'r'

def hexa_to_dec(number):
    number=number.upper()
    if number=='A':
        number=10
    elif number=='B':
        number=11
    elif number =='C':
        number=12
    elif number =='D':
        number=13
    elif number =='E':
        number=14
    elif number=='F':
        number=15
    else:
        return int(number)

def num_to_hexa(number):
    if number==10:
        number='A'
    elif number==11:
        number='B'
    elif number ==12:
        number='C'
    elif number ==13:
        number='D'
    elif number ==14:
        number='E'
    elif number==15:
        number='F'
    else:
        return str(number)

def decimal_to_anyradix(number,r):
    #successive divisons
    converted=""
    while number!=0:
        remainder=number%r
        converted += num_to_hexa(remainder)
        number=number//r

    return converted[::-1]

def anyradix_to_decimal(number,r):
    #number in string
    #successive multiplication

    converted=0
    number=number[::-1] #reversing the number
    for n in range(len(number)):
        converted += hexa_to_dec(number[n])*r**n
    return converted

def convert(num,fro,to):
    deci=anyradix_to_decimal(num,fro)
    conv= decimal_to_anyradix(deci,to)

    return conv

print("***** BASE CONVERSION *****")
number = input("Enter number: ")
fro = int(input("Enter base of the number: "))
to = int(input("Convert to base: "))
print("Result: ", convert(number, fro, to))
    
    
