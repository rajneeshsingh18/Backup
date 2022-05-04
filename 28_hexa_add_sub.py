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

def hex_addition(num1, num2):
    num1 = list(str(num1))
    num2 = list(str(num2))

    hsum = 0
    carry = 0
    result = ''

    while len(num1) > 0 or len(num2) > 0 or carry:
        sub_sum = hex_to_num(num1[-1]) + hex_to_num(num2[-1]) + hex_to_num(carry)

        if sub_sum > 15:
            carry = sub_sum // 16
            sub_sum = sub_sum % 16

        else:
            carry = 0
        result += num_to_hex(sub_sum)

        num1 = num1[:-1]
        num2 = num2[:-1]

    return result[::-1]

def hex_subtraction(num1, num2):
	num1 = list(str(num1))
	num2 = list(str(num2))
	borrowed = False
	result = ''
	minus = False
 
	if num2 > num1:
		temp = num1
		num1 = num2
		num2 = temp
		minus = True
 
	while len(num1) > 0 or len(num2) > 0:
		num1_l = hex_to_num(num1[-1])
		num2_l = hex_to_num(num2[-1])
 
		if borrowed:
			num1_l = num1_l - 1
			borrowed = False
 
		sub = num1_l - num2_l
		if sub < 0:
			sub = (num1_l + 16) - num2_l
			borrowed = True
 
		result += num_to_hex(sub)
 
 
		num1 = num1[:-1]
		num2 = num2[:-1]
 
	if minus:
		return '-' + result[::-1]
	else:
		return result[::-1]
 


# MENU
print('***** HEX ADDITION AND SUBSTRACTION *****')
a = input('Enter first hex number: ')
b = input('Enter second hex number: ')

print(f"""
Result:
1. {a} + {b} = {hex_addition(a, b)}
 2. {a} - {b} = {hex_subtraction(a, b)}
""")