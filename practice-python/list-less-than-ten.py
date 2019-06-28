# practice 3

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b =[]

user_input = int(input("Enter a number:"))
for i in a:
    if i < user_input:
        print(i)
        b.append(i)
    else:
        pass
print(b)