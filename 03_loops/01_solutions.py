numbers = list(map(int,input("Enter the list:").split())) # for list in integers
# for list of string: items = input("Enter items separated by spaces: ").split()
# comma-separated : items = [item.strip() for item in input("Enter items separated by commas: ").split(",")]

positive_numbers = 0
for i in numbers:
    if i > 0:
        positive_numbers += 1
print ("positive number count is:",positive_numbers)
    