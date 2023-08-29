# Function to make the program read the file
def read_file():
    global imported_txt
    global path
    print("Please end with the extension like 'sample_file.txt'")
    path = input("Enter the path to the text file: ")
    try:
        file = open(path, "r")
    except:
        print('File not found')
    else:
        imported_txt = file.read()
        file.close()
        print("\U0001F44D")

# Function to display the text in the screen
def display_text():
    global imported_txt
    try:
        print()
        print(imported_txt)
        print()
    except:
        print()
        print("No file has been loaded yet.")
        print()

# Function to modity / update the txt
def update_text():
    try:
        global imported_txt
        print("where_to_modify did you want to add Something in the text?")
        where_to_modify = input("Press\n'1' if you to add content the beginning\n'2'for the middle\n'3' to add a the end\n'4'if you want to add in a new line at the end\n")
        while where_to_modify not in ['1', '2', '3', '4']:
            where_to_modify = input("Invalid Input! Please enter either 1 or 2 or 3: ")

        if where_to_modify == '1':
            content = input("PLease write down the text you want to add in the beggining of the text >>> ")
            imported_txt = content + " " + imported_txt
            print("The Text have been updated\n")
        elif where_to_modify == "2":
            find_word = input("Please type the last letter that is in the word you want to write content after  >>> ")
            index = imported_txt.find(find_word)
            content =  input(f"PLease write down the text you want to add after the word that ends with '{find_word}' in the text >>> ")
            listed_imported_txt = [imported_txt[:index+2], content, " ", imported_txt[index+2:]]
            imported_txt = "".join(listed_imported_txt)
            print("The Text have been updated\n")
        elif where_to_modify == "3":
            content = input("PLease write down the text you want to add at the end of the text >>> ")
            imported_txt = imported_txt + " " + content
            print("The Text have been updated\n")
        elif where_to_modify == "4":
            content = input("PLease write down the text you want to add in a next at the end of the text >>> ")
            imported_txt = imported_txt + "\n" + content
            print("The Text have been updated\n")
    except:
        print("\nThe program did not read the file yet")

def clean_text():
    try:
        global imported_txt
        what_to_remove = input("Press\n'1' if you want to remove extra whitespace (useless Whitespace in the beginnng and the end of the text)\n'2' to remove a specific character\n>>> ")
        while what_to_remove not in ['1', '2']:
            print("Invalid Input!")
            what_to_remove = input("Press\n'1' if you want to remove extra whitespace (useless Whitespace in the beginnng and the end of the text)\n'2' to remove a specific character\n>>> ")
        if what_to_remove == "1":
            imported_txt = imported_txt.strip()
            print("Test successfully cleaned")
        elif what_to_remove == "2":
            char_to_remove = input("Which character you you want to remove all over the text? Write it down >>> ")
            new_text = "".join([char for char in imported_txt if char != char_to_remove])
            imported_txt = new_text
            print("Test successfully cleaned\n")
    except:
        print("\nThe program did not read the file yet")

# Function to save the text
def save_text():
    try:
        global path
        global imported_txt
        how_to_save = input("Press\n'1' If you want to save a copy\n'2' If you want to owerwhite the original file\n>>> ")
        while how_to_save not in ['1', '2']:
            print("Invalid Input!")
            how_to_save = input("Press\n'1' If you want to save a copy\n'2' If you want to owerwhite the original file\n>>> ")
        if how_to_save == "1":
            print("Write down the new path or just the name end up with the extension like 'sample_file.txt'")
            new_path = input(">>> ")
            try:
                new_file = open(new_path, "w")
                new_file.write(imported_txt)
                new_file.close()
                print(f"File {new_path} saved successfully")
            except:
                print("An error occured. We will save it as 'save_file.txt.txt'")
                new_file = open("save_file.txt", "w")
                new_file.write(imported_txt)
                print("File 'save_file.txt' saved successfully")
        else:
            overwriten_file = open(path, "w")
            overwriten_file.write(imported_txt)
            overwriten_file.close()
            print(f"File {new_path} saved successfully")
    except:
        print("\nThe program did not read the file yet")




