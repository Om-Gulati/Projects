print("Welcome to Custom Operation Calculator!")
print("Supported operations: + (Add), - (Subtract), * (Multiply), / (Divide), ** (Power), % (Modulus)")
print("Type 'exit' anytime to quit.\n")

while True:
    operation = input("Enter the operation you want to perform (+, -, *, /, **, %): ")

    if operation.lower() == "exit":
        print("Goodbye! See you soon.")
        break

    count = input("How many numbers do you want to use? ")
    if count.lower() == "exit":
        print("Goodbye! See you soon.")
        break

    try:
        count = int(count)
        numbers = []
        for i in range(count):
            num = input(f"Enter number {i+1}: ")
            if num.lower() == "exit":
                print("Goodbye! See you soon.")
                exit()
            numbers.append(float(num))

        result = numbers[0]

        for num in numbers[1:]:
            if operation == "+":
                result += num
            elif operation == "-":
                result -= num
            elif operation == "*":
                result *= num
            elif operation == "/":
                if num == 0:
                    raise ZeroDivisionError
                result /= num
            elif operation == "**":
                result **= num
            elif operation == "%":
                result %= num
            else:
                print("Unsupported operation. Try again.\n")
                break
        else:
            print(f"Result: {result}\n")

    except ValueError:
        print("Please enter valid numbers.\n")
    except ZeroDivisionError:
        print("Oops! Cannot divide by zero.\n")
