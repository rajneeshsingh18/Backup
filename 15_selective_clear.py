#selective clear  r1 and r2'

num1=input("Enter a first binary number : ")
num2=input("Enter a second binary number : ")

result=[]
k=len(num1)

for i in range(k):

    if(num1[i]=='1' and num2[i]=='0'):
        result.append(1)
    else :
        result.append(0)

print("Selective clear : " ,result)
