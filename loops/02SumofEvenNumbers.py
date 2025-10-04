number = int(input("Enter a Even integer: "))

sum_even = 0

for i in range(2,number + 1,2):
  sum_even += i

print("Sum of even numbers from 1 to", number, "is:", sum_even)