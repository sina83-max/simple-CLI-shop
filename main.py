from math import floor


products = {
    "pencil": 5000,
    "notebook": 20000,
    "eraser": 3000,
    "bag": 80000,
    "calculator": 150000
}

shopping_cart = {}

def get_yes_no_input(prompt):
    """
    A Function to validate user's input regarding a
    yes or no question.
    """
    while True:
        response = input(prompt).strip().lower()
        if response in ('y', 'yes'):
            return 'y'
        elif response in ('n', 'no'):
            return 'n'
        print("Invalid input. Please enter 'y'/'yes' or 'n'/'no'.")

def get_positive_item_count(prompt):
    """
    Validating the input number for a count object.
    """
    while True:
        count = floor(float(input(prompt)))
        print(count)
        if count > 0:
            return count
        else:
            print("Enter a positive integer please!")

def get_menu_choice():
    while True:
        choice = input("\nEnter your choice (1-4): ").strip()
        if choice in ('1', '2', '3', '4'):
            return choice
        print("Invalid choice. Please enter a number between 1 and 4.")
def get_option_choice():
    while True:
        choice = input("\nEnter your choice (1-2): ").strip()
        if choice in ('1', '2'):
            return choice
        print("Invalid choice. Please enter 1 or 2.")


def back_to_main_menu():
    """
    Function use in the CLI for better UX.
    """
    while True:

        print("\nOptions:")
        print("1. Back to main menu")
        print("2. Exit the app")

        choice = get_option_choice()
        if choice == '1':
            return  # Returns to main menu
        elif choice == '2':
            exit_checkout()
            exit()  # Completely exits the program


def list_items():
    """
    List products in our store.
    """
    print("\n=== Available Products ===")
    for item, price in products.items():
        print(f"{item}: {price}")

    back_to_main_menu()



def add_to_shopping_cart():
    """
    Adding new items to the user shopping cart
    :return:
    """
    print("\n=== Available Products ===")
    for item, price in products.items():
        print(f"{item}: {price}")

    wants_to_buy = get_yes_no_input(
        "Do you want to add items to your shopping cart?(y,n)\n"
    )
    if wants_to_buy == 'y':
        while True:
            item = input("Enter your desired item: ")
            if item in products.keys():
                count = get_positive_item_count(
                    "Enter the count(1 or more): "
                )
                shopping_cart[item] =  [
                    count, count * products.get(item)]
                wants_to_continue = get_yes_no_input(
                    "Do you want to continue shopping?(y,n)\n"
                )

                if wants_to_continue == 'n':
                    print(
                        "Thanks for adding the items to your shopping cart!\n" +
                        "Please continue to checkout step to finalize your purchase."
                    )

                    break
                else:
                    continue
            else:
                print("Please enter a valid product name from the following list:")
                list_items()




    else:
        print("Heading back to the main menu...")

def calculating_purchase_invoice():
    """
    Calculating the total price regarding probable discounts
    """
    total_price = 0
    if shopping_cart.items():
        for item, count in shopping_cart.items():
            total_price += shopping_cart.get(item)[1]
        if total_price > 200000:
            total_price = total_price * 0.85
            print(f"The total cost of the purchase with 15% discount: {total_price}")
        elif total_price > 100000:
            total_price = total_price * 0.9
            print(f"The total cost of the purchase with 10% discount: {total_price}")
        else:
            print(f"The total cost of the purchase: {total_price} ")






def showing_purchase_invoice():
    """
    Display the purchase invoice
    """
    if shopping_cart.items():
        for item, count in shopping_cart.items():
            print("-----")
            print(f"item: {item}\ncount: {count[0]}\nItem total price: {count[1]}")
            print("-----")
        calculating_purchase_invoice()
        back_to_main_menu()

    else:
        print("You haven't added any items to your shopping cart.\n" +
              "Please go back to the Add items to shopping cart option and add to your shopping cart.")
        back_to_main_menu()


def exit_checkout():
    if shopping_cart.items():
        calculating_purchase_invoice()
        print("Thanks for your trust in our shop! ")
    else:
        response = get_yes_no_input(
            "You haven't bought anything yet. Are you sure you want to quit?(y,n)\n"
        )
        if response == 'y':
            print('See you soon!')
        else:
            print("Going back to the main menu...")
            display_menu()


def display_menu():
    """
    Displays the main menu and handles user navigation
    """
    while True:
        print("\n=== Shopping App Menu ===")
        print("1. List available items")
        print("2. Add items to shopping cart")
        print("3. Display invoice")
        print("4. Exit/Checkout")

        choice = get_menu_choice()

        if choice == '1':
            list_items()
        elif choice == '2':
            add_to_shopping_cart()
        elif choice == '3':
            showing_purchase_invoice()
        elif choice == '4':
            exit_checkout()
            break  # Exit the loop and end the program
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


# Main program entry point
if __name__ == "__main__":
    print("Welcome to the Shopping App!")
    display_menu()

