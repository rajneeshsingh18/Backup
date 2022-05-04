#selective complement  XOR

num1=input("Enter a first binary number : ")
num2=input("Enter a second binary number : ")

k=len(num1)
result=[]

for i in range(k):

    if (num1[i]!=num2[i]):
        result.append(1)
    else:
        result.append(0)

print("\nSelective Complement : " , result)
