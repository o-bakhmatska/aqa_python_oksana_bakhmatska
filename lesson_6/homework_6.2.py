while True:
    word = input("Введіть слово, в якому є літера 'h': ")
    if 'h' in word.lower():
        print("Так! У слові є літера 'h'.")
        break
    else:
        print("У слові немає літери 'h'. Спробуйте ще раз.")