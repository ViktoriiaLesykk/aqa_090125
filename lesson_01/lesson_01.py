user_name = "Ivan"
user_age = 10 + 8
user_salary = 10000000.23 # хай ця зарплата справді буде у мене

print(user_name, user_age, user_salary)

if user_age > 35:
   print("Hello!")
else:
    print("Hi, bro!")

current_year = 2025

born_year = current_year - user_age
old_year = current_year + user_age
mult = current_year * user_age
div = current_year / user_age
print("Ви народилися:", born_year, "\n", "Ваш вік старості:", old_year,)
print(mult,"\n", div)