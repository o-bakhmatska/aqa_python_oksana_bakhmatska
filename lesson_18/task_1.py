from Generator_Iterator_Decorator import Generator

gen = Generator()

print("Even number to 10:")
for x in gen.even_numbers(10):
    print(x)

print("\nFibonacci to 30:")
for x in gen.fibonacci(30):
    print(x)