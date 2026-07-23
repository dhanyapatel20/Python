test_dict = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
print("the original dictionary is : " + str(test_dict))
k=2
res=0
for key in test_dict:
    if test_dict[key] == k:
        res += 1
print("the number of keys with value " + str(k) + " is : " + str(res))