list1 = [1,2,3,4,5,6]
list2 = [3,4,5,6,7,8]

my_set1 = set(list1)
my_set2 = set(list2)

print(my_set1)
print(my_set2)

#adding and removing
my_set1.add(9)
my_set2.remove(3)

print(my_set1)
print(my_set2)

#union
    # 1st method
union_set = my_set1.union(my_set2)
print(union_set)

    # 2nd method
union_set2 = my_set1 | my_set2
print(union_set2)

#intersection
    #1st method
int_set1 = my_set1.intersection(my_set2)
print(int_set1)
    #2nd method
int_set2 = my_set1 & my_set2
print(int_set2)

#difference
    #1st method
dif_set1 = my_set1.difference(my_set2)
print(dif_set1)
    #2nd method
dif_set2 = my_set1 - my_set2
print(dif_set2)








