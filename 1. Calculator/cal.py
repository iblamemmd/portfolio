first = int(input("first: "))
second = int(input("second: "))
op = input("op: ")
if op == "+":
    print("out:", first + second)
elif op == "-":
    print("out:", first - second)
elif op == "*":
    print("out:", first * second)
elif op == "/":
    if second != 0:
        print("out:", first / second)
    else:
        print("Division by zero is not allowed!")
else:
    print("Invalid operator")
    
