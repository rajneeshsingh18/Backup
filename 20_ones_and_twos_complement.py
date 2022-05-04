"""
Ques. Write a program that will prompt for the input of a binary value
and print:

a. One's Complement
b. Two's Complement

"""


def swap(n):

    for x in range(len(n)):

        if n[x]=='0':
            n[x]=='1'
        else:
            n[x] == '0'

    return n


def ones_complement(number):
    #swap 0's and 1's
    k=len(number)   #(r^n - 1)-N
    one_comp=(2**k-1)-int(number,2)
    return bin(one_comp).replace('0b','')

def twos_complement(number):
    k=len(number)
    two_comp=(2**k) - int(number,2)
    return bin(two_comp).replace('0b','')

#Menu
print('***** COmplements ******')
a=input('Enter binary number : ')

print(f"""
Result:
1. One's complement = {ones_complement(a)}
2. two's complement = {twos_complement(a)}

""")
