def swap(n):

    for x in range(len(n)):

        if n[x]=='0':
            n[x]=='1'
        else: 
            n[x]=='0'
    return n

def comp1(number):
    base=16
    k=len(number)
    comp_1=(base**k-1)-int('AD9',base)
    return hex(comp_1)[2:]

def comp2(number):
    k=len(number)
    base=16
    comp_=(base**k)-int('AD9',base)
    return hex(comp_)[2:]

print("******* Complement ******")
a=input("Enter a Hexadecimal number : ")


print(f"""
Result:
1. 15's Complement = {comp1(a)}
2. 16's  complement = {comp2(a)}
""")