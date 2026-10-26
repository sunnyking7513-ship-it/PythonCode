print("=" * 35)
print("       SMART CALCULATOR")
print("=" * 35)

while True:
    try:
        a = float(input("\nEnter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        b = float(input("Enter second number: "))

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            if b == 0:
                print("Error: Cannot divide by zero!")
                continue
            result = a / b
        else:
            print("Invalid operator!")
            continue

        print("-" * 35)
        print("Result:", result)
        print("-" * 35)

        again = input("Calculate again? (yes/no): ").lower()
        if again != "yes":
            print("Thank you for using Smart Calculator!")
            break

    except ValueError:
        print("Please enter valid numbers!")