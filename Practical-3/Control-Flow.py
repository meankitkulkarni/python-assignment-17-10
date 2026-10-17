def show_menu():
    print("\n=== Utility Calculator ===")
    print("1. Add numbers")
    print("2. Subtract numbers")
    print("3. Multiply numbers")
    print("4. Divide numbers")
    print("5. Show Summary")
    print("6. Average of three numbers")
    print("0. Exit")


def get_number(prompt="Enter a number: "):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def add(*args):
    return sum(args)


def average(a, b, c):
    return (a + b + c) / 3


def calculate(a, b, operation="+"):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    else:
        raise ValueError("Unsupported operation.")


def grade_from_marks(marks, maximum=100):
    if maximum <= 0 or marks < 0 or marks > maximum:
        raise ValueError("Marks must be within the valid range.")

    percentage = (marks / maximum) * 100

    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


def show_summary(**kwargs):
    print("\n--- Summary ---")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def show_local_variable():
    message = "This variable is local to the function."
    print(message)


def main():
    history = []

    show_local_variable()

    print("\nAddition test:", add(2, 4, 6, 8))

    show_summary(
        student="Student A",
        practical=3,
        status="Complete"
    )

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "0":
            print("Exiting...")
            break

        elif choice not in {"1", "2", "3", "4", "5", "6"}:
            print("Invalid input. Please enter a valid option.")
            continue

        elif choice == "5":
            show_summary(
                total_calculations=len(history),
                last_result=history[-1] if history else "No calculations yet"
            )
            continue

        elif choice == "6":
            a = get_number("First number: ")
            b = get_number("Second number: ")
            c = get_number("Third number: ")

            result = average(a, b, c)
            label = "average"

        else:
            a = get_number("First number: ")
            b = get_number("Second number: ")

            if choice == "1":
                result = add(a, b)
                label = "addition"

            elif choice == "2":
                result = calculate(a, b, "-")
                label = "subtraction"

            elif choice == "3":
                result = calculate(a, b, "*")
                label = "multiplication"

            else:
                try:
                    result = calculate(a, b, "/")
                except ZeroDivisionError as error:
                    print("Error:", error)
                    continue

                label = "division"

        format_result = lambda value: f"{value:.2f}"
        print(f"Result ({label}): {format_result(result)}")
        history.append(result)


if __name__ == "__main__":
    main()