def swap(n):

    for x in range(len(n)):

        if n[x]=='0':
            n[x]=='1'
        else: 
            n[x]=='0'
    return n

def comp1(number):
    base=8
    k=len(number)
    comp_1=(base**k-1)-int('526',base)
    return oct(comp_1)[2:]

def comp2(number):
    k=len(number)
    base=8
    comp_=(base**k)-int('526',base)
    return oct(comp_)[2:]

print("******* Complement ******")
a=input("Enter a octal number : ")


print(f"""
Result:
1. 7's Complement = {comp1(a)}
2. 8's  complement = {comp2(a)}
""")