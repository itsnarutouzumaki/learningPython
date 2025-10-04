number = int(input("Enter the Number: "))
factorial=1
for num in range(1,number+1):
  factorial=factorial*num
print(f"factorial of {number} is {factorial}")