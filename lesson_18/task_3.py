from Generator_Iterator_Decorator import LogFunction, CatchErrors

@LogFunction
def sum(a, b, c=0):
    return a + b + c

sum(5, 10, c=20)

@CatchErrors
def div(a, b):
    return a / b

div(10, 0)