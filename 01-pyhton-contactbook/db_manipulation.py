import sqlite3

db_file = "C:\\Users\\brenn\\Documents\\GitHub\\pythonProjects\\01-pyhton-contactbook\\contact_book.db"

def register():
    with sqlite3.connect(db_file) as connexion:
        cursor = connexion.cursor()
        last_id = cursor.lastrowid
        try:
            name = input("Enter the name: ").strip().lower()
            number = int(input("Enter the number: "))
            print("Do you want to enter an email? [Y]es [N]o")
            email_conf = input("Your choice: ").strip().lower()
            email = input("Enter the email: ").strip().lower() if email_conf == 'y' else ""

            print("\n")

            data = (last_id, name, number, email)
            cursor.execute("INSERT INTO p_contact VALUES (?,?,?,?)", data)
            connexion.commit()
            
            name = (name,)
            contact = cursor.execute("SELECT * FROM p_contact WHERE contact_name = ?", name)
            contact = contact.fetchone()
            showable_string = "{}. {} : Phone number: {}, Email address: {}.".format(
                contact[0],contact[1].capitalize(),contact[2],contact[3])
            print(showable_string)
            print("The new contact is successfully registered.")

        except Exception as e:
            print("Error: ", e)

def show_contacts():
    with sqlite3.connect(db_file) as connexion:
        cursor = connexion.cursor()
        rq = cursor.execute("SELECT * FROM p_contact")
        rq = rq.fetchall()
        for c in rq:
            showable_string = "{}. {} : Phone number: {}, Email address: {}.".format(
                c[0],c[1].capitalize(),c[2],c[3])
            print(showable_string)

def show_edited_contact(id_contact):
    with sqlite3.connect(db_file) as connexion:
        cursor = connexion.cursor()
        contact = cursor.execute("SELECT * FROM p_contact WHERE id_contact = ?", id_contact)
        contact = contact.fetchone()
        print("\n")
        showable_string = "{}. {} : Phone number: {}, Email address: {}.".format(
            contact[0],contact[1].capitalize(),contact[2],contact[3])
        print(showable_string)
        print("The new contact is successfully registered.")

def edit(id_contact):
    with sqlite3.connect(db_file) as connexion:
        cursor = connexion.cursor()
        flag1 = True
        flag2 = True
        id_contact = (id_contact,)
        try:
            rq = cursor.execute("SELECT * FROM p_contact WHERE id_contact = ?", id_contact)
            rq = rq.fetchone()
            
            while flag1:
                while flag2:
                    print('\n')
                    print("What do you want to edit? 1: Name; 2: Number; 3: Email, 0: Return to initial menu")
                    choice = int(input("Your choice: "))
                    if choice == 1:
                        new_name = input("Enter the new name: ").strip().lower()
                        data = (new_name, id_contact[0])
                        cursor.execute("UPDATE p_contact SET contact_name = ? WHERE id_contact = ?", data)
                        connexion.commit()

                        show_edited_contact(id_contact)
                        flag2 = False
                    elif choice == 2:
                        new_number = input("Enter the new number: ").strip().lower()
                        data = (new_number, id_contact[0])
                        cursor.execute("UPDATE p_contact SET contact_number = ? WHERE id_contact = ?", data)
                        connexion.commit()

                        show_edited_contact(id_contact)
                        flag2 = False
                    elif choice == 3:
                        new_email = input("Enter the new email: ").strip().lower()
                        data = (new_email, id_contact[0])
                        cursor.execute("UPDATE p_contact SET contact_email = ? WHERE id_contact = ?", data)
                        connexion.commit()

                        show_edited_contact(id_contact)
                        flag2 = False
                    elif choice ==0:
                        break
                    else:
                        print("You have not entered a correct option.")

                print("Do you want to change something else on this contact? 1: Yes; 2: No")
                n_choice = int(input("Your choice: "))
                if n_choice == 1:
                    flag2 = True
                elif n_choice == 2:
                    flag1 = False

        except Exception as e:
            print("Error: ", e)

def delete(id_contact):
    with sqlite3.connect(db_file) as connexion:
        cursor = connexion.cursor()
        flag = True
        id_contact = (id_contact,)

        try:
            cursor.execute("DELETE FROM p_contact WHERE id_contact =?", id_contact)
            print("This contact has been deleted successfully.")
        except Exception as e:
            print("Error: ", e)


