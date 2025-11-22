class Generator:
    def even_numbers(self, n):
        for num in range(0, n + 1, 2):
            yield num

    def fibonacci(self, n):
        a, b = 0, 1
        while a <= n:
            yield a
            a, b = b, a + b

class IteratorReverseList:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.data[self.index]
        self.index -= 1
        return value

class IteratorEvenNumbers:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        value = self.current
        self.current += 2
        return value

class LogFunction:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"[LOG] Call function: {self.func.__name__}")
        print(f"[LOG] Arguments: args {args}, kwargs {kwargs}")

        result = self.func(*args, **kwargs)
        print(f"[LOG] Result: {result}")
        return result

class CatchErrors:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        try:
            return self.func(*args, **kwargs)
        except Exception as e:
            print(f"[ERROR] Error in function {self.func.__name__}: {e}")
            return None