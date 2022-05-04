#Menu driven program for selective set , selective clear , selective complement and selective mask.

print("""
******* MENU *******"
1. For Selective set 
2. For Selective mask 
3. For Selective clear 
4. For Selective Compliment
""" )




op=input("Enter your option : " )




if op=="1":

    num1=input("Enter a first binary number : " )
    num2=input("Enter a second binary number : " )
    
    k=len(num1)
    result=[]
    
    for i in range(k):

        if(num1[i]=="0" and num2[i]=="0"):
            result.append(0)
        else :
            result.append(1)
            
    print("Selective set : " , result)

elif op=="2":

    num1=input("Enter a first binary number : " )
    num2=input("Enter a second binary number : " )

    k=len(num1)
    result=[]

    for i in range(k):

        if(num1[i]=="1" and num2[i]=="1"):
            result.append(1)
        else :
            result.append(0)
            
    print("Selective Mask : " , result)

elif op=="3":
    num1=input("Enter a first binary number : " )
    num2=input("Enter a second binary number : " )

    k=len(num1)
    result=[]

    for i in range(k):

        if(num1[i]=="1" and num2[i]=="0"):
            result.append(1)
        else :
            result.append(0)

    print("Selective clear : " , result)

elif op=="4":

    num1=input("Enter a first binary number : " )
    num2=input("Enter a second binary number : " )

    k=len(num1)
    result=[]

    for i in range(k):

        if(num1[i]!=num2[i]):
            result.append(1)

        else:
            result.append(0)

    print("Selective complement : " ,result)

