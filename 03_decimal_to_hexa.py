#decimal to hexadecimal

def decimal_to_hexa(num):
    if num>1:
        decimal_to_hexa(num//16)
    b=num%16
    if b==10:
        b='A'
    elif b==11:
        b='B'
    elif b==12:
        b='C'
    elif b==13:
        b='D'
    elif b==14:
        b='E'
    elif b==15:
        b='F'
    print(b,end="")

number = int(input("Enter a  decimal number : "))

print("Hexadecmial conversion")

decimal_to_hexa(number)
        
