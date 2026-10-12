pet = input("Which pet do you have? ").strip().lower()
age = float(input("Tell the age: "))
time_frame = int(input("(1) for week, (2) for month, (3) for year: "))

feed = None

if time_frame not in (1, 2, 3):
    print("Invalid time frame selected.")
    raise SystemExit

if pet == "cat":
    if time_frame == 1:
        if age <= 4:
            feed = "KMR"
        elif age <= 8:
            feed = "KMR with kitten tibble"

    elif time_frame == 2:
        if age <= 12:
            feed = "Canned wet kitten food"

    elif time_frame == 3:
        if 2 <= age <= 7:
            feed = "High protein, moderate fat"
        elif age > 7:
            feed = "Highly digestible protein, joint supplements"

elif pet == "dog":
    if time_frame == 1:
        if age <= 4:
            feed = "Mother's milk or Commercial Puppy Milk Replacer"
        elif age <= 8:
            feed = "Weaning slurry of puppy food mixed with milk replacer or warm water."

    elif time_frame == 2:
        if age <= 12:
            feed = "Breed-size specific puppy food"

    elif time_frame == 3:
        if 1 <= age <= 7:
            feed = "Sustained energy, muscle maintenance"
        elif age > 7:
            feed = "Lower calories to prevent obesity, increased fiber for gut motility"

if feed:
    print("Suggested feed:", feed)
else:
    print("Invalid details provided!")
