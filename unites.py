u=int(input("enter the unites consumed"))
if u<50:
    a=u*2.5
    s=25
elif u<100:
    a=u *3.5
    s=35
else:
    a=u*5
    s=45
t=a+s
print("electricity bill",t)
