numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total_sum = sum(filter(lambda x: not x % 2, numbers))

print("Сума парних чисел:", total_sum)