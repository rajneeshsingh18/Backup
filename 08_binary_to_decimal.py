#binary to decimal conversion

n=int(input("Enter a binary number :"))
i=0
final=0

while(n!=0):
    temp=n%10
    temp=temp*2**i
    i=i+1
    final=final+temp
    n=n//10

print("Decimal number is " ,final)
