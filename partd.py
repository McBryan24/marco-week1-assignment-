#Part D: Error Handling
try:
    m = int(input("Enter first number:"))
    n = int(input("Enter second number:"))
    result = m/n
except ZeroDivisionError:
    print("Division by zero detected")
except ValueError:
    print("ValueError detected")
else:
    print("Result:", result)
finally:
    print("Division Complete!")