# ask if user wants to create tournament
# if yes, ask user to enter the parameters
# when it's done, show a recap before confirmation
# if no, quit

def main_menu():
    print("[1] Create a tournament")
    print("[2] Add a new player")
    print("[3] Show lists")
    print("[0] Exit")


main_menu()
option = int(input("Enter your option: "))

while option != 0:
    if option == 1:
        # beep
        print("selected option 1")
    elif option == 2:
        # boop
        print("selected option 2")
    elif option == 3:
        # bibop
        print("selected option 3")
    else:
        print("Invalid option")

    print()
    main_menu()
    option = int(input("Enter your option: "))
