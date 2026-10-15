items = ["toyota","mercedes","lexus","volvo","toyota","honda","mercedes"]

seen = set()
duplicate = set()

for item in items:
    if item in seen:
        duplicate.add(item)
    else:
        seen.add(item)
print("All duplicate items: ", list(duplicate))
print("All seen items: ", list(seen))

