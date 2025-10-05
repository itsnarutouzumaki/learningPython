def even_generator(n):
    for num in range(n):
        if num % 2 == 0:
            yield num

result=even_generator(10)
print(result) 
for even_num in result:
    print(even_num)