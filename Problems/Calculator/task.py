# put your python code here
a = float(input())
b = float(input())
operation = input()

if (operation in ["/", "mod", "div"]) and b == 0:
    print("Division by 0!")
else:
    if operation == "+":
        print(a + b)
    elif operation == "-":
        print(a - b)
    elif operation == "*":
        print(a * b)
    elif operation == "/":
        print(a / b)
    elif operation == "mod":
        print(a % b)
    elif operation == "div":
        print(a // b)
    elif operation == "pow":
        print(a ** b)

