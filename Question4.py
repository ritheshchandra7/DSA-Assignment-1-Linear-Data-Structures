# Q4. Write a program to print the first non-repeated character from a string?

from collections import Counter
inp_str = input("Enter string: ")
counter = Counter(inp_str)
non_repeated = {inp_str.index(i):i for i in counter.keys() if counter[i] == 1}
if non_repeated:
  first_non_repeated = min(non_repeated.keys())
  print("first non-repeated character is", non_repeated[first_non_repeated])
else:
  print("all characters are repeated")