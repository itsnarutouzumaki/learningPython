def operationOnTwoNumbers(num1, num2):
    return num1 * num2, num1 + num2, num1 - num2, num1 / num2

multiplication, addition, subtraction, division = operationOnTwoNumbers(10, 5)

print("Multiplication:", multiplication)
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Division:", division)