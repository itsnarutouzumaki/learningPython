givenString = input("Enter a string: ")
reversedString = ""

for i in range(len(givenString)-1, -1, -1):
    reversedString += givenString[i]

print("Reversed string:", reversedString)