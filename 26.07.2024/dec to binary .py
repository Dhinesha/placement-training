def decimal_to_binary(n):
    return bin(n).replace("0b", "")

num = input()
print(f"Binary of {num} is {decimal_to_binary(num)}")
