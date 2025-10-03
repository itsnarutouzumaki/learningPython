age = int(input("Enter your pet's age in years: "))
species = input("Enter your pet's species (dog/cat): ").lower()


if species == "dog":
    if age < 2:
        print("Recommended food: Puppy food")
    elif 2 <= age <= 7:
        print("Recommended food: Adult dog food")
    else:
        print("Recommended food: Senior dog food")

if species == "cat":
    if age < 1:
        print("Recommended food: Kitten food")
    elif 1 <= age <= 7:
        print("Recommended food: Senior cat food")