"""
Ohm's Law and Power Calculator
Author: Hassan Abdulsubur Ayobami

A beginner-friendly calculator for voltage, current, resistance and power.
It also keeps a history of calculations during the current program session.
"""

def get_positive_number(prompt):
    """Ask for a number and keep asking until the user enters a valid positive value."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than zero.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number, for example 12 or 2.5.")


def calculate_value(target, first_name, first_value, second_name, second_value):
    """Calculate the selected electrical quantity from two known quantities."""
    values = {
        first_name: first_value,
        second_name: second_value
    }

    # Find voltage (V)
    if target == "V":
        if "I" in values and "R" in values:
            return values["I"] * values["R"]
        elif "P" in values and "I" in values:
            return values["P"] / values["I"]
        elif "P" in values and "R" in values:
            return (values["P"] * values["R"]) ** 0.5

    # Find current (I)
    elif target == "I":
        if "V" in values and "R" in values:
            return values["V"] / values["R"]
        elif "P" in values and "V" in values:
            return values["P"] / values["V"]
        elif "P" in values and "R" in values:
            return (values["P"] / values["R"]) ** 0.5

    # Find resistance (R)
    elif target == "R":
        if "V" in values and "I" in values:
            return values["V"] / values["I"]
        elif "V" in values and "P" in values:
            return (values["V"] ** 2) / values["P"]
        elif "I" in values and "P" in values:
            return values["P"] / (values["I"] ** 2)

    # Find power (P)
    elif target == "P":
        if "V" in values and "I" in values:
            return values["V"] * values["I"]
        elif "V" in values and "R" in values:
            return (values["V"] ** 2) / values["R"]
        elif "I" in values and "R" in values:
            return (values["I"] ** 2) * values["R"]

    return None


def show_history(history):
    """Display all calculations made during this session."""
    if len(history) == 0:
        print("\nNo calculations have been made yet.")
    else:
        print("\n--- CALCULATION HISTORY ---")
        for number, item in enumerate(history, start=1):
            print(f"{number}. {item}")
        print("---------------------------")


def main():
    # Store completed calculations in a list (our extra feature).
    history = []

    print("====================================")
    print("   OHM'S LAW AND POWER CALCULATOR")
    print("====================================")

    # Keep the calculator running until the user chooses to quit.
    while True:
        print("\nWhat would you like to calculate?")
        print("1. Voltage (V)")
        print("2. Current (I)")
        print("3. Resistance (R)")
        print("4. Power (P)")
        print("5. View calculation history")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "6":
            print("\nThank you for using the calculator. Goodbye!")
            break
        elif choice == "5":
            show_history(history)
            continue
        elif choice in ("1", "2", "3", "4"):
            targets = {
                "1": ("V", "voltage", "volts (V)"),
                "2": ("I", "current", "amperes (A)"),
                "3": ("R", "resistance", "ohms (Ω)"),
                "4": ("P", "power", "watts (W)")
            }
            target, target_name, unit = targets[choice]

            # Ask which two known electrical quantities the user has.
            print("\nChoose the two values you already know:")
            print("1. Voltage and current (V and I)")
            print("2. Voltage and resistance (V and R)")
            print("3. Current and resistance (I and R)")
            print("4. Power and current (P and I)")
            print("5. Power and voltage (P and V)")
            print("6. Power and resistance (P and R)")

            pair_choice = input("Enter your choice (1-6): ").strip()

            pairs = {
                "1": ("V", "I", "voltage (V)", "current (A)"),
                "2": ("V", "R", "voltage (V)", "resistance (Ω)"),
                "3": ("I", "R", "current (A)", "resistance (Ω)"),
                "4": ("P", "I", "power (W)", "current (A)"),
                "5": ("P", "V", "power (W)", "voltage (V)"),
                "6": ("P", "R", "power (W)", "resistance (Ω)")
            }

            if pair_choice not in pairs:
                print("Invalid choice. Please select a number from 1 to 6.")
                continue

            first_code, second_code, first_label, second_label = pairs[pair_choice]

            # A quantity cannot be both the target and one of the known values.
            if target in (first_code, second_code):
                print(f"You selected {target_name} to find, so do not enter it as a known value.")
                print("Please choose a pair that does not include the value you want to find.")
                continue

            first_value = get_positive_number(f"Enter {first_label}: ")
            second_value = get_positive_number(f"Enter {second_label}: ")

            answer = calculate_value(
                target, first_code, first_value, second_code, second_value
            )

            if answer is None:
                print("Those values cannot be used to calculate the selected quantity.")
            else:
                result = f"{target_name.title()} = {answer:.2f} {unit}"
                print("\n--- RESULT ---")
                print(result)
                history.append(result)

        else:
            # Handle menu choices that are not recognised.
            print("Invalid menu choice. Please enter a number from 1 to 6.")


# Start the program.
if __name__ == "__main__":
    main()
