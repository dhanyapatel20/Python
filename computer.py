class Computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def set_maxprice(self, price):
        self.__maxprice = price

see=Computer()
see.sell()

see.__maxprice = 1000
see.sell()

see.set_maxprice(1000)
see.sell()