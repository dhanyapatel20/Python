class PairofElements:
    def two_sum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num], i)
            lookup[num] = i

value = int(input("Enter sum for which you want to find pair of elements: "))
print("index1=%d, index2=%d" % PairofElements().two_sum((20,30,60,70,50,100), value))