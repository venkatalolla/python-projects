# This is an initial exercise

import datetime

now = datetime.datetime.now()

user_name = input("Enter your name:")
while True:
    try:
        user_age = int(input("Enter your age:"))
    except ValueError:
        print("Oops! That is not valid age....")
        continue
    break
while True:
    try:
        user_print = int(input("How many times you want to print the output?"))
    except ValueError:
        print("Oops! That is not valid age....")
        continue
    break
user_years_to_hundred = 100 - user_age
actual_year = user_years_to_hundred + now.year

for i in range(user_print):
    print("{1}.Dude you will be 100 in {0}".format(actual_year, i))
