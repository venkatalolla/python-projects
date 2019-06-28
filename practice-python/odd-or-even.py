# Practice 2

while True:
    try:
        user_input = int(input("Enter a number:"))
    except ValueError:
        print("Oops! That is not valid number. Enter again")
        continue
    break

if user_input % 2 == 0 and user_input % 4 == 0:
    print("The number {0} is even and a multiple of 4".format(user_input))
elif user_input % 2 == 0:
    print("The number {0} is even but not a multiple of 4".format(user_input))
else:
    print("The number {0} is odd".format(user_input))