adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

print(adwentures_of_tom_sawer)

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print("Task 01.", adwentures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print("Task 02.", adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split())
print("Task 03.", adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print(f"Task 04. {adwentures_of_tom_sawer.count("h")}")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
count_capitalized = sum(1 for w in adwentures_of_tom_sawer if w[0].isupper())
print("Task 05.", count_capitalized)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_word = adwentures_of_tom_sawer.index("Tom")
second_word = adwentures_of_tom_sawer.index("Tom", first_word + 1)
print("Task 06. Друга позиція слова 'Tom':", second_word)


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
import re
adwentures_of_tom_sawer_sentences = re.split(r'(?<=[.!?])\s+', adwentures_of_tom_sawer)
print("Task 07.", adwentures_of_tom_sawer_sentences[-1])

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print("Task 08.", adwentures_of_tom_sawer_sentences[3].lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print(f"Task 09. {any(sentence.startswith("By the time") for sentence in adwentures_of_tom_sawer_sentences)}")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print(f"Task 10. {len(adwentures_of_tom_sawer_sentences[-1].split())}")