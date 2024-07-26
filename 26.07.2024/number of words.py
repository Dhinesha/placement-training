def count_words(s):
    return len(s.split())

text = input()
print(f"The number of words in '{text}' is {count_words(text)}.")
