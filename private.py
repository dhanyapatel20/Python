class myClass:
    __privateVar = 27
    def __privMeth(self):
        print("I'm inside class myClass")
    def hi(self):
        print("private variable is: ", self.__privateVar)

fool = myClass()
fool.hi()