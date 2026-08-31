class IOSTRING:
    def __init__(self):
        self.str1 = ""
    def get_string(self):
        self.str1 = input("Enter the string: ")
    def print_string(self):
        print("result: ",self.str1.upper())

str=IOSTRING()
str.get_string()
str.print_string()