import db_manipulation

def init_menu():
    """Initial menu of the contact book."""
    flag = True

    print('\n')
    print('#'*55)
    print('#'*10," "*9, 'Contact Book'," "*10, '#'*10)
    print('#'*55)
    print('#'*2," "*7," Select one of the options below:"," "*7,'#'*2)
    print("#"*2," "*10,"[1] See your contacts "," "*15, "#"*2)
    print("#"*2," "*10,"[2] Register a new contact "," "*10, "#"*2)
    print("#"*2," "*10,"[3] Edit a existent contact "," "*9, "#"*2)
    print("#"*2," "*10,"[0] To quit the contact book "," "*8, "#"*2)
    print('#'*55)
    print('\n')

    while flag:
        try:
            choice = int(input("Enter your choice here: "))
            if choice == 0:
                flag = False
            elif choice == 1:
                contacts_menu()
                flag = False
            elif choice == 2:
                register_menu()
                flag = False
            elif choice == 3:
                edit_menu()
                flag = False
            else:
                print("This is not in the options. Please, select one of the options.")
        except:
            print("The key you entered is not accepted.")

def contacts_menu():
    """Menu with the list of all contacts."""
    flag = True

    print('\n')
    print('#'*55)
    print('#'*20, 'Contact Book', '#'*21)
    print('#'*55)
    print('#'*11, " "*6," List of Contacts:", " "*5,'#'*11)
    print("\n")

    db_manipulation.show_contacts()

    print("\n")
    print('#'*55)
    print('#'*2,"Select one of the options below:"," "*16,'#'*2)
    print("#"*2,"[1] Select one contact to see more informations"," ", "#"*2)
    print("#"*2,"[2] Register a new contact "," "*21, "#"*2)
    print("#"*2,"[3] Edit one of these contacts "," "*17, "#"*2)
    print("#"*2,"[4] Delete one of these contacts "," "*15, "#"*2)
    print("#"*2,"[5] Return to the initial menu "," "*17, "#"*2)
    print("#"*2,"[0] To quit the contact book "," "*19, "#"*2)
    print('#'*55)
    print('\n')

    while flag:
        try:
            choice = int(input("Enter your choice here: "))
            if choice == 0:
                flag = False
            elif choice == 1:
                #detail_menu()
                print('To be developped...')
                flag = False
            elif choice == 2:
                register_menu()
                flag = False
            elif choice == 3:
                edit_menu()
                flag = False
            elif choice == 4:
                delete_menu()
            else:
                print("This is not in the options. Please, select one of the options.")
        except:
            print("The key you entered is not accepted.")

def register_menu():
    """Register menu to new contacts."""

    print('\n')
    print('#'*35)
    print('#'*10, 'Contact Book', '#'*11)
    print('#'*35)
    print('#', " "*2," Creating a new contact:", " "*3,'#')
    
    db_manipulation.register()
    init_menu()

    print('#'*35)
    print('\n')

def edit_menu():
    """Edit menu to edit contacts."""

    print('\n')
    print('#'*55)
    print('#'*20, 'Contact Book', '#'*21)
    print('#'*55)
    print("#"*2," "*15,"Editing a contact "," "*14, "#"*2)
    print('\n')
    db_manipulation.show_contacts()
    print('\n')
    print("Select the contact to edit by its ID.")
    choice = int(input("Your choice: "))

    db_manipulation.edit(choice)
    init_menu()

    print('#'*35)
    print('\n')

def delete_menu():
    """Delete menu to delete contacts."""

    print('\n')
    print('#'*55)
    print('#'*20, 'Contact Book', '#'*21)
    print('#'*55)
    print("#"*2," "*15,"Deleting a contact "," "*14, "#"*2)
    print('\n')
    db_manipulation.show_contacts()
    print('\n')
    print("Select the contact to edit by its ID.")
    choice = int(input("Your choice: "))

    db_manipulation.delete(choice)
    init_menu()

    print('#'*35)
    print('\n')




init_menu()
