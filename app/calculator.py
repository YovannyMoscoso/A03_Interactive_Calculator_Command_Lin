from app.operations import Operations


class Calculator:

    @staticmethod
    def run():

        operations = {
            "1": ("Add", Operations.add),
            "2": ("Subtract", Operations.subtract),
            "3": ("Multiply", Operations.multiply),
            "4": ("Divide", Operations.divide)
        }

        while True:
            print("\n------------------ Interactive Calculator ------------------------------\n")

            for key, (name, _) in operations.items():
                print(f"\t{key}. {name}")

            print("\t0. Exit")

            choice = input("\nChoose an option: ")

            if choice == "0":
                print("Exit. Goodbye!")
                break

            if choice not in operations:
                print("Invalid option. Please try again.")
                continue

            name, operation = operations[choice]
            print(f"\nYou choose: {name.upper()}")

            try:
                first_number = float(input("\nEnter the first number: "))
                second_number = float(input("Enter the second number: "))

                result = operation(first_number, second_number)

                print(f"\nResult: {result}\n")

            except ValueError:
                print("Invalid number. Please enter numeric values.\n")

            except ZeroDivisionError:
                print("Error: Cannot divide by zero.\n")