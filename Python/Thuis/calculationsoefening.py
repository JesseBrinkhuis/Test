while True:
    operator = input("Toets een operator in (+ - * /) ")

    if operator == "+" or operator == "-" or operator == "/" or operator == "*":
        num1 = float(input("Voer een getal in "))
        num2 = float(input("Voer een getal in "))
        if operator == "+":
            result = num1 + num2
            print(f"De uitkomst = {result}")
        elif operator == "-":
            result = num1 - num2
            print(f"De uitkomst = {result}")
        elif operator == "*":
            result = num1 * num2
            print(f"De uitkomst = {result}")
        elif operator == "/":
            result = num1 / num2
            print(f"De uitkomst = {result}")
    else:
        print(f"{operator} is een incorrecte input")
