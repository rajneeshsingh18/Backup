def swap(n):

    for x in range(len(n)):

        if n[x]=='0':
            n[x]=='1'
        else: 
            n[x]=='1'

    return n

def nines_complement(number):
    k=len(number)
    base=10
    nines_comp=(base**k-1) - int(number)
    return nines_comp

def tens_complement(number):
    k=len(number)
    base=10
    tens_comp=(base**k) - int(number)
    return tens_comp

#Menu 

print("******* Complement ******")

a=input("Enter a decimal number : ")

print(f"""
Result:
1. 9th Complement = {nines_complement(a)}
2. 10th complement = {tens_complement(a)}
""")


    