#selective mask

num1=input("Enter a first binary number : " )
num2=input("Enter a second binary number : " )

k=len(num1)

result=[]

for i in range(k):

    if(num1[i]=='1' and num2[i]=='1'):
        result.append(1)
    else:
        result.append(0)

print("Selective Mask : " , result)
           
