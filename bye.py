while True:
    try:
        n=int(input("enter a number:"))
        while (n%2==0):
            print("bye")
        break
    except ValueError:
        print("invaled input")
        