import file_fonctions as ff
import time

print("Welcome to the Text File Editor!")
print()

while True:
    print("1. Read Text File\n2. Display Text\n3. Update Text\n4. Clean Text\n5. Save Text\n6. Exit")
    choice = input("\nPlease select an option: ")
    while choice not in ["1", "2", "3", "4", "5", "6"]:
        choice = input("\nPlease select an option from the list above: ")

    if choice == "1":
        print()
        ff.read_file()
    elif choice == "2":
        print()
        ff.display_text()
    elif choice == "3":
        print()
        ff.update_text()
    elif choice == "4":
        print()
        ff.clean_text()
    elif choice == "5":
        print()
        ff.save_text()
    elif choice == "6":
        print("Exiting the Text File Editor... Goodbye! \U0001f44b \nIn twe (2) seconds")
        time.sleep(2)
        quit()
