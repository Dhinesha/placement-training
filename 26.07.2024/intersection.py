def intersection(lst1, lst2):
    return [value for value in lst1 if value in lst2]

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print(f"Intersection: {intersection(list1, list2)}")
