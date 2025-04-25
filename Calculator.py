a = float(input ("Enter Number A: "))
b = float(input ("Enter Number B: "))
operation = input ("Enter the operation you want to do (+, -, *, **, /): ")
if operation == "+":
    c = a + b
elif operation == "-":
    c = a - b
elif operation == "*":
    c = a * b
elif operation == "/":
    c = a / b
elif operation == "**":
    c = a ** b
else:
    print ("Invalid operation") 
print (c)
