try:
    num1=int(input("enter a number1:"))
    num2=int(input("enter a number2:"))
    result=num1/num2
    print("the result of the division is :", result)
except ValueError:
    print("please enter a valid number")
except ZeroDivisionError:
    print("please enter a non-zero number for the divisor")
except:
    print("an unexpected error occurred")
finally:
    print("the program has completed execution")