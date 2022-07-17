import math

lst = [5, 8, 3]
histo = []

for item in lst:
    histo.append("x"*item)
print("Histogram = ", histo)

lst1 = ["ab", "ef", "lm"]
lst2 = ["no", "jk", "cd"]
lst_res = []

for i in range(len(lst1)):
    j = -(i + 1)
    lst_res.append(lst1[i] + lst2[j])
print("lst_res = ", lst_res)








