class ArrayTransformer:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def sum_of_numbers(s):
        try:
            numbers = [int(x) for x in s.split(',')]
            return sum(numbers)
        except ValueError:
            return "Не можу це зробити!"

    def transform_all(self):
        return [self.sum_of_numbers(item) for item in self.data]



some_array = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3", "1,2,3,4,100"]
process = ArrayTransformer(some_array)
print(process.transform_all())