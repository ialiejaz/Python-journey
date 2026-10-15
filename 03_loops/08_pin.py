attempts = 3
set_pin = input("Set a PIN: ")

while attempts > 0:
    pin = input("Enter your PIN: ")

    if pin == set_pin:
        print("Access Granted")
        break

    attempts -= 1
    if attempts > 0:
        print(f"Wrong PIN. Only {attempts} tries left!")
else:
    print(f"Account locked. Too many wrong tries.")
    forget_pin = input('Type "forget" to reveal PIN: ')
    if forget_pin.strip().lower() == "forget":
        print(f"Your PIN is {set_pin}")