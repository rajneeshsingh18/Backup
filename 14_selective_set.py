#Menu driven for selective set , selective clear and selective compliment

#selective set  OR opertaions
num1=input("Enter the first binary number : ")
num2=input("Enter the second binary number : ")

result=[]
k=len(num1)

for i in range (k):
    if(num1[i]=="0" and num2[i]=="0"):
        result.append(0)
    else:
        result.append(1)

print(result)

