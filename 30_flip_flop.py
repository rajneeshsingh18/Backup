x = int (input("enter your input = "))

def dff(num1):
  global x
  if num1==0 :
    x=0
    return x 
  elif num1==1:
    x=1
    return x
n1 = int(input("Enter the D = "))
dff(n1) 



x = int (input("enter your input = "))

def tff(num1):
  global x
  if num1==0:
    return x
  elif num1==1:
    if x==0:
      x=1
      return x 
    else:
      x=0
      return x
n1 = int(input("Enter the t = "))
tff(n1) 



import random
x = int (input("enter your input = "))

def srff(num1,num2):
  global x
  if num1==0 and num2==0:
    return x
  elif num1==0 and num2==1:
    x=0
    return x 
  elif num1==1 and num2==0:
    x=1
    return x
  elif num1==1 and num2==1:
    y=random.random()
    if y > 0.5:
      return 1
    if y < 0.5:
      return 0 

n1 = int(input("Enter the s = "))
n2 = int(input("Enter the r = "))
srff(n1,n2)


x = int (input("enter your input = "))

def jkff(num1,num2):
  global x
  if num1==0 and num2==0:
    return x
  elif num1==0 and num2==1:
    x=0
    return x 
  elif num1==1 and num2==0:
    x=1
    return x
  elif num1==1 and num2==1:
    if x==0:
      x=1
      return x 
    else:
      x=0
      return x  

n1 = int(input("Enter the j = "))
n2 = int(input("Enter the k = "))

jkff(n1,n2)