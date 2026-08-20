class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

ryd=Vehicle(9999, 8888)
print("the max speed of the vehicle is " , ryd.max_speed)
print("the mileage of the vehicle is " , ryd.mileage)