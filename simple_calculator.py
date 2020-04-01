# Calculator
operator = ""
result = 0
print("Calculator\n==========\nGive me two numbers...")
x = input("First Number: ")
y = input("Second Number: ")
print("The numbers you gave are "+str(x)+" and "+str(y)+"\nIs that right?(Y/N)")
value = input()
if value == "Y":
    print("For subtraction type -\nFor addition type +\nFor division type /\nFor multiplication type *")
    operator = input()
elif value == "N":
    print("Type the numbers again!")
    x = input("First Number: ")
    y = input("Second Number: ")
else:
    print("Exiting...")
    exit(1)

if operator == "-":
    result = float(x) - float(y)
elif operator == "+":
    result = float(x) + float(y)
elif operator == "/":
    if y == 0:
        print("Division by 0 is not defined!")
        exit(1)
    result = float(x) / float(y)
elif operator == "*":
    result = float(x) * float(y)
else:
    print("Invalid Operator")
    exit(1)

print("Result is: " + str(result))
