#Exclusive OR of the first number by the second bitwise

def ex_or(a,b):
    if b>a:
        t=a
        a=b
        b=t

    a=list(bin(a).replace('0b',''))
    b=list(bin(b).replace('0b',''))

    if len(a)>len(b):
        while len(b) != len(a):
            b.insert(0,'0')

    exor=[]

    for i in range(len(a)):

        if a[i] == '1' and b[i] == '1':
            exor.insert(0,'0')
            continue
        elif int(a[i]) or int(b[i]):
            exor.insert(0,'1')
        else:
            exor.insert(0,'0')

    final=''

    for x in exor:

        final +=x

    return int(final,2)


#OR of the first number by the second bitwise

def bit_or(a,b):

    if b>a:
        t=a
        a=b
        b=t

    a=list(bin(a).replace('0b',''))
    b=list(bin(b).replace('0b',''))

    if len(a)>len(b):
        while len(a)!=len(b):
            b.insert(0,'0')

    exor=[]

    for i in range(len(a)):

        if int(a[i]) or int(b[i]):
            exor.insert(0,'1')
        else:
            exor.insert(0,'0')

    final=''

    for x in exor :
        final =final+x

    return int(final,2)


#AND of the first number by the second bitwise


def bit_and(a,b):

    if b>a:
        t=a
        a=b
        b=t

    a=list(bin(a).replace('0b',''))
    b=list(bin(b).replace('0b',''))

    if len(a) > len(b):
        while len(a) != len(b):
            b.insert(0,'0')

    exor=[]

    for i in range(len(a)):

        if int(a[i]) and int(b[i]):
               exor.insert(0,'1')
        else :
            exor.insert(0,'0')

    final=''
    for x in exor :
        final = final+x

    return int(final,2)

            
           

# MENU
print('***** ^, |, & *****')
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

print(f"""
Result:
1.Exclusive OR (^) = {ex_or(a,b)}
2.Bitwise OR (|) = {bit_or(a,b)}
3. Bitwise AND (&) = {bit_and(a,b)}
""")
