
def get_non_empty_input(prompt):
    """Ask until the user enters non-empty text."""
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


def get_positive_integer(prompt):
    """Ask until the user enters a positive integer."""
    while True:
        value = input(prompt).strip()

        try:
            number = int(value)

            if number > 0:
                return number

            print("Enter a number greater than zero.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_menu_choice(prompt, valid_choices):
    """Accept only choices listed in valid_choices."""
    valid_choices = {str(choice) for choice in valid_choices}

    while True:
        choice = input(prompt).strip()

        if choice in valid_choices:
            return choice

        print(
            "Invalid choice. Select one of:",
            ", ".join(sorted(valid_choices))
        )


def get_yes_no(prompt):
    """Accept yes/y or no/n."""
    while True:
        answer = input(prompt).strip().casefold()

        if answer in ("yes", "y"):
            return True

        if answer in ("no", "n"):
            return False

        print("Please enter yes or no.")


if __name__ == "__main__":
    print("Testing input utilities...")

    name = get_non_empty_input("Enter your name: ")
    print("Name:", name)

    number = get_positive_integer("Enter a positive integer: ")
    print("Number:", number)

    choice = get_menu_choice(
        "Choose 1, 2, or 3: ",
        ["1", "2", "3"]
    )
    print("Choice:", choice)

    confirmed = get_yes_no("Continue? (yes/no): ")
    print("Confirmed:", confirmed)

    print("All utility functions tested successfully.")
