import math

print("Exercise 1:")
s = "dabaxyddab"
my_dict = {}
for char in s:
    if char in my_dict:
        my_dict[char] = my_dict[char] + 1
    else:
        my_dict[char] = 1

for k in sorted(my_dict):
    print(f"{k} - {my_dict[k]}")

reverseDict = {}
for k in my_dict:
    if my_dict[k] in reverseDict:
        reverseDict[my_dict[k]].append(k)
    else:
        reverseDict[my_dict[k]] = list(k)
print(reverseDict)

print("Exercise 2:")
lst1 = [11, 7, 5, 8, 5, 37, 11, 5]
lst2 = [22, 8, 10, 1, 11]
lst3 = [71, 3, 22, 8, 2, 5, 1]
lst = (lst1, lst2, lst3)
list_of_b = []

print("lists with double items:")
for item in lst:
    temp_set = set(item)
    if len(item) > len(temp_set):
        print(item)
    else:
        list_of_b.append(temp_set)

print("Common values are:")
if len(list_of_b) == 0:
    print("[]")
elif len(list_of_b) == 1:
    print(list_of_b)
elif len(list_of_b) == 2:
    print(list_of_b[0].intersection(list_of_b[1]))
else:
    print(list_of_b[0].intersection(list_of_b[1], list_of_b[2]))

print("Exercise 3:")
my_list = [31, 99, 3, 1943555]
sort_order = "desc"
detailed_list = []
for item in my_list:
    num = 0
    for char in str(item):
        digit = int(str(item)[num])
        detailed_list.append(digit)
        num = num + 1

if sort_order == "asc":
    print(sorted(set(detailed_list)))
elif sort_order == "desc":
    print(sorted(set(detailed_list), reverse=True))