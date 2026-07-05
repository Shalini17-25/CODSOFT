def calc():
    a = float(input("Enter first number: "))
    op = input("Enter operation (+, -, *, /): ")
    b = float(input("Enter second number: "))

    if op == '+':
        r = a + b
    elif op == '-':
        r = a - b
    elif op == '*':
        r = a * b
    elif op == '/':
        if b == 0:
            print("Error: division by zero")
            return
        r = a / b
    else:
        print("Invalid operation")
        return

    print(f"Result: {r}")

calc()