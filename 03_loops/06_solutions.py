while True:
    number = int(input("Enter a value b/w 1 and 10: "))
    if 1 <= number <= 10:
        print("Entry Successful!")
        break
    else:
        print("Invalid entry, try again!")