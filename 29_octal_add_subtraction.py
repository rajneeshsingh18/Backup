"""
#octal addition
bina1 = input("enter the first binary = ")
bina2 = input("enter the second binary = ")

intsum = int(bina1, 8) + int(bina2, 8)
binasum = oct(intsum).replace("0o","")
print("bit wise sum is =" ,binasum)


#octal substraction
bina1 = input("enter the first octal = ")
bina2 = input("enter the second octal = ")

int1=int(bina1 ,8)
print("first number = ",int1)
int2=int(bina2 ,8)
print("second number = ",int2)

if int2 > int1:
  k=len(bina2)
  comp2 = (8**k - 1)-int2+1
  int2 = comp2
  print(int2)
  intsub = int1 + int2
  k1=len(str(oct(intsub).replace("0o","")))
  comp3 = (8**k1 - 1)-intsub+1
  binsub = comp3
  print("bitwise subtraction is = -",oct(binsub).replace("0o",""))
else:
  intsum = int(bina1, 8) - int(bina2, 8)
  binasum = oct(intsum).replace("o","")
  print("bit wise subtraction is =" ,binasum)


"""


def num_to_hex(digit):
    if digit > 9:
        return str(hex(digit)).replace('0x', '')
    else:
        return str(digit)

def hex_to_num(digit):
    if digit == 'a':
        return 10
    elif digit == 'b':
        return 11
    elif digit == 'c':
        return 12
    elif digit == 'd':
        return 13
    elif digit == 'e':
        return 14
    elif digit == 'f':
        return 15
    else:
        return int(digit)
        
def octal_addition(num1, num2):
    sums = []
    carry = 0

    while num1 > 0 or num2 > 0 or carry:
        osum = 0
        carry = 0
        result = ''

        while num1 > 0 or num2 > 0 or carry:
            sub_sum = hex_to_num(num1) % 10 + hex_to_num(num2) % 10 + hex_to_num(carry)

            if sub_sum > 15:
                carry = sub_sum // 16
                sub_sum =  sub_sum % 16
            else:
                carry = 0

            result += '' + num_to_hex(sub_sum)

            num1 = num1 // 10
            num2 = num2 // 10

        return result[::-1]


def octal_subtraction(num1, num2):
    borrowed = False
    result = ''
    minus = False

    if num2 > num1:
        temp = num1
        num1 = num2
        num2 = temp
        minus = True

    while num1 > 0 or num2 > 0:
        num1_l = num1 % 10
        num2_l = num2 % 10

        if borrowed:
            num1_l = num1_l - 1
            borrowed = False

        sub = num1_l - num2_l
        if sub < 0:
            sub = (num1_l + 8) - num2_l
            borrowed = True

        result += str(sub)


        num1 = num1 // 10
        num2 = num2 // 10

    if minus:
        return '-' + result[::-1]
    else:
        return result[::-1]


# MENU
print('***** OCTAL ADDITION AND SUBSTRACTION *****')
a = int(input('Enter first octal number: '))
b = int(input('Enter second octal number: '))

print(f"""
Result:
1. {a} + {b} = {octal_addition(a, b)}
2. {a} - {b} = {octal_subtraction(a, b)}
""")
