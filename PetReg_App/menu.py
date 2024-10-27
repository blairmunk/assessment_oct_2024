from service import *

def menu():
    while True:
        print("\n1. Add animal")
        print("2. Teach command")
        print("3. List animals")
        print("4. Count animals")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_animal()
        elif choice == "2":
            teach_command()
        elif choice == "3":
            list_animals()
        elif choice == "4":
            count_animals()
        elif choice == "5":
            break
        else:
            print("Invalid option.")