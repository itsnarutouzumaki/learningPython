password = input("Enter your password: ").strip()

passwordSize=len(password)

if passwordSize<6:
  print("Weak password")
elif passwordSize<=10:
  print("Moderate password")
else:
  print("Strong password")