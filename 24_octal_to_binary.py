num=int(input("Enter a octal number : "))
i=0
final=0
while(num!=0):
    temp=num%10
    temp=temp*8**i
    i=i+1
    final= final+temp
    num=num//10

print("Decimal number : ", final)

def decimal_to_binary(num):

    if num>1:
        decimal_to_binary(num//2)
    print(num%2,end="")

print("Binary conversion from octal number ")

decimal_to_binary(final)
