#octal to decimal

n=int(input("Enter a octal number : "))
i=0
final=0

while(n!=0):
    temp=n%10
    temp=temp*8**i
    i=i+1
    final=final+temp
    n=n//10

print("Decimal number : ",final)
