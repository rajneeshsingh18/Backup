#hexadecimal to decimal conversion

conversion_table={'1':1 , '2' : 2, '3':3 ,'4':4,'5':5, '6':6 , '7':7 ,'8' :8, '9':9, 'A':10 , 'B':11,'C':12, 'D':13 ,'E':14, 'F':15}

hexadecimal=input("Enter a hexidecimal number : ").strip().upper()
decimal=0

power=len(hexadecimal)-1

for i in hexadecimal:
    decimal = decimal + conversion_table[i]*16**power
    power = power -1

print("Decimal conversion : " , decimal)
