extraShotChoice=input("Do you want extra shot(Yes/No): ").lower().strip()

sizeOfCup=input("What size of cup do you want(Small/Medium/Large): ")

if extraShotChoice=="yes":
  print(f"You have chosen {sizeOfCup} size of  coffee with extra shot")
else:
  print(f"You have chosen {sizeOfCup} size of  coffee without extra shot")