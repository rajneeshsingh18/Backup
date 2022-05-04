# decimal to hexadecimal number

def decimal_to_hexa(num):
    if num>1:
        decimal_to_hexa(num//16)
        b=num%16
        if b==10:
            b='A'
        elif b==11:
            b='B'
        elif b==12:
            b='C'
        elif b==13:
            b='D'
        elif b==14:
            b='E'
        elif b==14:
            b='F'
        print(b,end="")

import math

def decimalpoint_to_hexapoint(num):
    for i in range(10):
        unum=16*num
        deci,inte=math.modf(unum)
        num=deci
        d=int(inte)
        if d==10:
            d='A'
        elif d==11:
            d='B'
        elif d==12:
            d='C'
        elif d==13:
            d='D'
        elif d==14:
            d='E'
        elif d==14:
            d='F'
        print(d,end="")

number=eval(input("Enter a decimal point number : "))

decimal,integer=math.modf(number)

print("Hexadecimal conaversion ")

decimal_to_hexa(int(integer)),print(".",end=""),decimalpoint_to_hexapoint(decimal)
