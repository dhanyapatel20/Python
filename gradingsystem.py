print("enter your markes")
m=int(input("mathes="))
e=int(input("eng="))
h=int(input("his"))
sum=m+e+h
p=(sum/300)*100
if p>90:
    print("A+")
elif p>50:
    print("B-")
else:
    print("F--")
