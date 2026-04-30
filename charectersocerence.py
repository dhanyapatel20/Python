s=input("enteryour string:")
c=input("enter the character you want to serch for")
i=0
count  = 0
while i <len(s) :
    if s[i]==c :
        count= count+1
    i=i+1
print (count)


