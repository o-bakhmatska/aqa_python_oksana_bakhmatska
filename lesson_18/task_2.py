from Generator_Iterator_Decorator import IteratorReverseList, IteratorEvenNumbers

lst = [1, 2, 3, 4, 5]
print("Reverse List from 1 to 5:")
for item in IteratorReverseList(lst):
    print(item)

print("\nEven numbers to 10:")
for num in IteratorEvenNumbers(10):
    print(num)