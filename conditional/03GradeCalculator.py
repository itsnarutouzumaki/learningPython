studentScore = int(input("Enter your Score (0-100):"))
Grade = ""
if studentScore >= 90:
    Grade = "A"
elif studentScore >= 80:
    Grade = "B"
elif studentScore >= 70:
    Grade = "C"
elif studentScore >= 60:
    Grade = "D"
else:
    Grade = "F"

print("Your Grade is:", Grade)