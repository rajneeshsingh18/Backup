#any base to decimal number

n=int(input("Enter any base number : "))
base=int(input("Enter base value :"))

i=0
final=0
while(n!=0):
    temp=n%10
    temp=temp*base**i
    i=i+1
    final = final+temp
    n=n//10

print("Any base conversion number : ",final)
