number = int(input("Enter a number to print its multiplication table: "))

for i in range(1, 11):
    if(i==5):
        continue
    product = number * i
    print(f"{number} x {i} = {product}")