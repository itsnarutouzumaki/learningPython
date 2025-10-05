#it use to pass variable number of arguments to a function without defining them in definition


def sum_all(*args):
  total =0
  print(args)
  for num in args:
    total += num
  return total

print("Sum of all numbers is", sum_all(10,20,30,40,50))
