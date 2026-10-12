age = int(input("Enter age of individual:"))

if age < 13:
    print("Child")
elif age < 19:
    print("Teenager")
elif age < 60:
    print("Adult")
elif age >= 100:
    print("living bonus life")
else:
    print("Senior citizen")
