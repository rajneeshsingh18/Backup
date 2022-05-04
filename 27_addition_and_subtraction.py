"""
Ques. Write a program to implement the following binary operations
a. addition
b. subtraction using 2;s complement


#binary addition
bina1 = input("enter the first binary = ")
bina2 = input("enter the second binary = ")

intsum = int(bina1, 2) + int(bina2, 2)
binasum = bin(intsum).replace("0b","")
print("bit wise sum is =" ,binasum)


#binary substraction
bina1 = input("enter the first binary = ")
bina2 = input("enter the second binary = ")

int1=int(bina1 ,2)
print("first number = ",int1)
int2=int(bina2 ,2)
print("second number = ",int2)

if int2 > int1:
  k=len(bina2)
  comp2 = (2**k - 1)-int2+1
  int2 = comp2
  intsub = int1 + int2
  k1=len(str(bin(intsub).replace("0b","")))
  comp3 = (2**k1 - 1)-intsub+1
  binsub = comp3
  print(binsub)
  print("bitwise subtraction is = -",bin(binsub).replace("0b",""))
else:
  intsum = int(bina1, 2) - int(bina2, 2)
  binasum = bin(intsum).replace("b","")
  print("bit wise subtraction is =" ,binasum)
"""

def hex_to_dec(number):
    number = number.lower()
    if number == "a":
        return 10
    elif number == "b":
        return 11
    elif number == "c":
        return 12
    elif number == "d":
        return 13
    elif number == "e":
        return 14
    elif number == "f":
        return 15
    else:
        return int(number)

def num_to_hex(number):
    if number == 10:
        return "a"
    elif number == 11:
        return "b"
    elif number == 12:
        return "c"
    elif number == 13:
        return "d"
    elif number == 14:
        return "e"
    elif number == 15:
        return "f"
    else:
        return str(number)


def addition(num1, num2, base):
    num1 = list(num1)[::-1]
    num2 = list(num2)[::-1]

    if len(num2) > len(num1):
        t = num2
        num2 = num1
        num1 = t
    while len(num2) != len(num1):
        num2.append('0')

    add = []
    carry = 0
    for i in range(len(num1)):
        sum_ = hex_to_dec(num1[i]) + hex_to_dec(num2[i]) + carry

        if sum_ >= base:
            carry = sum_ // base
            sum_ = sum_ - base
        
        add.append(num_to_hex(sum_))

    final = ''
    if carry != 0:
       final += str(carry)

    for x in add[::-1]:
        final += x

    return final

# assert addition("102", "123", 10) == "225"
# assert addition("01", "11", 2) == "100"

def bin_substraction(num1, num2):
    if len(num2) > len(num1):
        t = num2
        num2 = num1
        num1 = t

    while len(num2) != len(num1):
        num2 = '0' + num2

    # 2's complement
    comp = (2 ** len(num2)) - int(num2, 2)
    return addition(num1, bin(comp)[2::], 2)


# MENU
print('***** BINARY ADDITION AND SUBSTRACTION *****')
a = input('Enter first binary number: ')
b = input('Enter second bnary number: ')


print(f"""
Result:
1. {a} + {b} = {addition(a, b, 2)}
2. {a} - {b} = {bin_substraction(a, b)}
""")
