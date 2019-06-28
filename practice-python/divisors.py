# practice 4

user_input = int(input("Enter a number:"))
i = 0
for i in range(user_input):
    i = user_input*2
    user_input += user_input
    print(i)
