#decimal point number to binary point number

#decimal to binary

def decimal_to_binary(num):
    if num>1:
        decimal_to_binary(num//2)
    print(num%2,end="")

import math

def decimalpoint_to_binarypoint(num):
    for i in range(10):
        unum=2*num
        deci,inte=math.modf(unum)
        num=deci
        print(int(inte),end="")


number=eval(input("Enter a decimal point number : "))

decimal, integer=math.modf(number)

print("Binary point conversion ")

decimal_to_binary(int(integer)),print(".",end=""),decimalpoint_to_binarypoint(decimal)
