givenString = input("Enter a string: ")

for i in range(len(givenString)):
  apeareance = 0
  for j in range(len(givenString)):
    if(givenString[i] == givenString[j]):
      apeareance+=1
  if(apeareance==1):
    print("First non-repeated character is:", givenString[i])
    break
      