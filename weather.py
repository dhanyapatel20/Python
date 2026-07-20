weather=(1,0,0,1,0,0,0,1)
suny=0
rainy=0
for i in weather:
    if i==1:
        suny+=1
    else:
        rainy+=1
if suny>rainy:
    print("goood weather")
else:
    print("bad weather")