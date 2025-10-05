#in args we can pass only variable number of non-keyword arguments to a function which can be accessed as a tuple

#in kwargs we can pass variable number of keyword arguments to a function which can be accessed as a dictionary

def print_kwargs(**kwargs):
  print(kwargs)
  for key,value in kwargs.items():
    print(f"{key} : {value}")


print_kwargs(name="John", age=30, city="New York")
print_kwargs(country="USA",profession="Engineer")