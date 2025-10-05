def recursiveFactorial (number):
    if number<=1:
        return 1
    return number * recursiveFactorial(number-1)

print("Factorial of 5 is", recursiveFactorial(5),'.')