#decimal point to octal point

def decimal_to_octal(num):
    if num>1:
        decimal_to_octal(num//8)
        print(num%8,end="")

import math

def decimalpoint_to_octalpoint(num):
    for i in range(10):
        unum=8*num
        deci,inte=math.modf(unum)
        num=deci
        print(int(inte),end="")

number=eval(input("Enter a decimal point number : " ))

decimal,integer=math.modf(number)

print("Octal point number ")

decimal_to_octal(int(integer)),print(".",end=""),decimalpoint_to_octalpoint(decimal)

