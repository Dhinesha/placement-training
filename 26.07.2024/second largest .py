def second_largest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2]

numbers = [1, 2, 3, 4, 5]
print(f"Second largest number is {second_largest(numbers)}")
