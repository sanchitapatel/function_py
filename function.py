def greet():
    print('Hello World!')

# call the function
greet()

print('Outside function')
x = lambda a, b : a * b
print(x(5, 6))