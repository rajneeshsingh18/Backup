def decimal(a):
  result = 0
  power = len(str(a)) - 1

  for x in str(a):
    result += int(x) * (2 ** power)
    power -= 1

  return str(result)

def binary(a):
  converted = ""

  while a != 0:
    remainder = a % 2
    converted = str(remainder) + converted
    a //= 2

  return converted


def twos(num):
  i = len(num) - 1
  pos = -1
  result = ""

  while i >= 0:
    result = num[i] + result
    if num[i] == "1":
      pos = i
      break
    i -= 1
  
  if pos == -1:
    return '1' + num

  pos -= 1
  bits = list(num)

  while pos >= 0:
    if bits[pos] == "1":
      result = "0" + result
    else:
      result = "1" + result
    pos -= 1
    
  return int(result)

a = input("Enter a binary number: ")
b = input("Enter another binary number: ")

decimal_a = decimal(a)
decimal_b = decimal(b)

if decimal_a > decimal_b:
  twos_b = twos(b)
  sum = int(decimal_a) + int(decimal(twos_b))

  print ("Result: ", sum)
else:
  twos_b = twos(b)
  sum = binary(int(decimal_a) + int(decimal(twos_b)))
  twos_sum = "-" + str(twos(sum))

  print ("Result: ", twos_sum)