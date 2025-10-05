text = input("Введіть рядок: ")
unique_count = len(set(text))
if unique_count > 10:
    print(True)
else:
    print(False)
