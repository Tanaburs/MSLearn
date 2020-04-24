first_number = input("Enter first number:")
operator = input("Enter operator")
second_number = input("Enter second number")

if not first_number.isnumeric() or not second_number.isnumeric():
    print("This is not a number!")
    exit()
else:
    if operator == "+":
        result = int(first_number) + int(second_number)
        print("Product of " + first_number + " " + operator + " " + second_number + " equals "
              + str(result))
    elif operator == "-":
        result = int(first_number) - int(second_number)
        print("Product of " + first_number + " " + operator + " " + second_number + " equals "
              + str(result))
    elif operator == "*":
        result = int(first_number) * int(second_number)
        print("Product of " + first_number + " " + operator + " " + second_number + " equals "
              + str(result))
    elif operator == "/":
        result = int(first_number) / int(second_number)
        print("Product of " + first_number + " " + operator + " " + second_number + " equals "
              + str(result))
    elif operator == "**":
        result = int(first_number) ** int(second_number)
        print("Product of " + first_number + " " + operator + " " + second_number + " equals "
              + str(result))
    elif operator == "%":
        result = int(first_number) % int(second_number)
        print("Product of " + first_number + " " + operator + " " + second_number + " equals "
              + str(result))
    else:
        print("Not a valid operator!")
        exit()





