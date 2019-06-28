# A simple calculator

def print_result(x):
    print("The result is:", x, "\n")

while True:
    print("Welcome to a Simple Calculator")
    print(" a. Addition \n b. Subraction \n c. Multiplication \n d. Division \n e. Modulus ")
    options = ["a","b","c","d","e","quit"]
    print("Enter 'quit' to close the calculator")
    option = input("Please enter an Option:")
    if option not in options:
        print("Please enter a valid Operator")
    elif option != "quit":
        while True:
            try:
                val1= int (input("Enter Value1:"))
            except ValueError:
                print("Oops! That is not valid number. Try an integer...")
                continue
            break
        while True:
            try:
                val2= int (input("Enter Value2:"))
            except ValueError:
                print("Oops! That is not valid number. Try an integer...")
                continue
            break
        i = 0
        if option is "a":
            i = val1+val2
        elif option is "b":
            i = val1-val2
        elif option is "c":
            i = val1*val2
        elif option is "d":
            i = val1/val2
        elif option is "e":
            i = val1%val2
        else:
            print("Not a valid Operator \n")
        print_result(i)
    else:
        print("Closing Calculator. Bye!")
        break