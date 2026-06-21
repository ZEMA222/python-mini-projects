print("Menu:")
print("1- Addition")
print("2- Subtraction")
print("3- Multiplication")
print("4- Division")

var_1 = int(input("Enter the first number: "))
var_2 = int(input("Enter the second number: "))

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Result =", var_1 + var_2)

    case 2:
        print("Result =", var_1 - var_2)

    case 3:
        print("Result =", var_1 * var_2)

    case 4:
        if var_2 == 0:
            print("Error: Division by zero")
        else:
            print("Result =", var_1 / var_2)

    case _:
        print("Invalid choice")