a=int(input("enter your attendence:"))
m=input("do you have medcales (Y/N)")

if m=="y":
     print(" you are allowed")
else:
     if a>= 75:
        print("you are allowed")
     else:
         print("you are not allowed to sit in the exam room ")
         