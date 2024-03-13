import sys

#add
def add(a, b):
    return a + b

#sub
def sub(a, b):
    return a - b

#multi
def mult(a, b):
    return a * b

#div
def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        sys.exit(1)


while True:
    #get input
    try:
        a = int(input("Enter the first number: "))
        op = input("Enter the operation: ")
        b = int(input("Enter the second number: "))
    except ValueError:
        print("Invalid number argument...")
        continue

    # decides which one to put 
    if op in ("+", "-", "*", "/"):
        if op == "+":
            print("Sum:", add(a, b))
        elif op == "-":
            print("Difference:", sub(a, b))
        elif op == "*":
            print("Product:", mult(a, b))
        elif op == "/":
            print("Quotient:", div(a, b))
    else:
        print("Invalid operation...")

#dis da choice quit one
    q = input("Quit? [y/n] ")
    if q.lower() == "y":
        break
