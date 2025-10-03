weather=input("Enter the current weather (sunny, rainy, snowy): ").strip().lower()

activity=""

if weather == "sunny":
    activity="Go for a walk in the park."
elif weather == "rainy":
    activity="Stay indoors and read a book."
elif weather == "snowy":
    activity="Build a snowman."

print("Suggested activity:", activity)