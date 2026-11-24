from itertools import groupby

s = input("Enter a combination: ").strip()
print(*(f"({len(list(group))}, {int(key)})" for key, group in groupby(s)))