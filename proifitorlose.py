ac=int(input("actual coast:"))
sc=int(input("selling coast"))
if sc > ac:
    p=sc-ac
    print("proffit =",p)
else:
    print("no proffit made")
    