def union(lst1, lst2):
    return list(set(lst1) | set(lst2))

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print(f"Union: {union(list1, list2)}")
