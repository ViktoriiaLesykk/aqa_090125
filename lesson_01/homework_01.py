# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print

for letter in "Hello world!":
    print(letter, end="")


# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4

# task 05 == виправте назви змінних
side_1 = 1
side_2 = 2
side_3 = 3
side_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimeter = side_1 + side_2 + side_3 + side_4
print(perimeter)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""

apple_tree = 4
pear_tree = apple_tree + 5
# "слив - на 2 менше" звучить не однозначно. Припускаю, що менше ніж яблунь.
plum_tree = apple_tree - 2

garden_trees = apple_tree + pear_tree + plum_tree

print (garden_trees)


# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""

before_lunch_temperature = 5
after_lunch_temperature = before_lunch_temperature - 10
late_evening_temperature = after_lunch_temperature + 4

print ("Late evening temperature:", late_evening_temperature)

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""


total_boys = 24
total_gils = total_boys / 2
absent_boys = 1
absent_girls = 2

present_children = total_boys - absent_boys + total_gils - absent_girls

print (present_children)

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже, 
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
#не "дорожче", а "дорожче" в умові

book_1_price = 8
book_2_price = book_1_price + 2
book_3_price = (book_1_price + book_2_price) / 2

print (book_1_price + book_2_price + book_3_price)