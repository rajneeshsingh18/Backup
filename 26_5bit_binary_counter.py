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



"""
def bsum(bina1):
  intsum = int(bina1, 2) + 1
  binasum = bin(intsum).replace("0b","")
  return binasum

def bsub(bina1):
  intsum = int(bina1, 2) - 1
  binasum = bin(intsum).replace("0b","")
  return binasum

bin1 = input("Enter your binar number = ")
op = int(input("enter your option 1 for counter up and 0 of counter down = "))
if op <= 1 and op > -1:
  k=len(bin1)
  loop=2**k

  for i in range (loop):
    if op == 1:
      a=bsum(bin1)
      
      if len(a) > k:
        c=a.replace("1",'')
        print(c)
        bin1=c
      else:
        print(a)
        bin1=a
    if op == 0:
      a=bsub(bin1)
      if len(a) < k:
        a=a+"1"
        print(a)
        bin1=a
      else:
        print(a)
        bin1=a
"""