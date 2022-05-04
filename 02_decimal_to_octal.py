# decimal to octal

def decimal_to_octal(num):
    if num>1:
        decimal_to_octal(num//8)
    print(num%8,end="")

number=int(input("Enter the deciaml number : " ))

print("Octal conversion " )
decimal_to_octal(number)
