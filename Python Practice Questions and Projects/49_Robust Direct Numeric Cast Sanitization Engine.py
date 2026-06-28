while True:
    try:
        # Read input
        value = input("Enter a number (or 'q' to quit): ")

        if value.lower() == 'q':
            print("Program terminated.")
            break

        # Convert input to integer
        num = int(value)

        # Perform a division
        result = 100 / num
        print("Result:", result)

    except ValueError:
        print("Handled: Invalid format numerical cast failed")

    except ZeroDivisionError:
        print("Handled: Division by zero forbidden")