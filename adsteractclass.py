from abc import ABC, abstractmethod
class Absclass(ABC):
    def print(self,x):
        print(x)
    @abstractmethod
    def task(self):
        print("wr are inside the acs class")

class testclass(Absclass):
    def task(self):
        print("we are inside the test class")


obj=testclass()
obj.task()
obj.print(48389)

        