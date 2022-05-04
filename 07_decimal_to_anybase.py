#Decimal to any base

def decimal_to_anybase(num,base):
    if num>1:
        decimal_to_anybase(num//base,base)
        b=num%base
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
        elif b==15:
            b='F'
        print(b,end="")

import math

def decimalpoint_to_anybasepoint(num,base):
    for i in range(10):
        unum=base*num
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
        elif d==15:
            d='F'
        print(d,end="")

number=eval(input("Enter deciaml number :"))
base=int(input("Enter the base conversion you want : "))

decimal,integer=math.modf(number)

print("Any base conversion ")

decimal_to_anybase(int(integer),base),print(".",end=""),decimalpoint_to_anybasepoint(decimal,base)
