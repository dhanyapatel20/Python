basket1={"apple" , "banana" , "apple","mango","grape"}
basket2={"banana" , "kiwi" , "mango","kiwi"}
print("basket1 : " + str(basket1))
print("basket2 : " + str(basket2))

basket1.add("orange")
print("basket1 after adding orange: " + str(basket1))

common_fruits = basket1.intersection(basket2)
print("common fruits in basket1 and basket2 : " + str(common_fruits))

import array as arr
frite_count = arr.array('i', [6, 5, 3, 0, 5])
print("fruit count : " + str(frite_count))

frite_count.insert(0,12)
frite_count.append(676767)
print("fruit count after adding items : " + str(frite_count))

count_of_5 = frite_count.count(5)
print("count of 5 in fruit count : " + str(count_of_5))

frite_count.reverse()
print("fruit count after reversing : " + str(frite_count))

print("")
print("===== CLASS FRUIT BASKET ORGANIZER =====")
print("basket1 : " + str(basket1))
print("basket2 : " + str(basket2))
print("shared fruits in basket1 and basket2 : " + str(common_fruits))
print("fruit count : " + str(frite_count))   
print("===========================================")