from functions import *

def mainLoop():
    contacts = {}
    printSuccess("Welcome to the Contact Management System!\nMenu:")
    while True:
        if contacts == {}:
            user_input = askMenu([
                "Add a new contact",  
                "Import contacts from a text tile", 
                "Quit"], 
                "Please choose an operation: ")
            try:
                user_input = int(user_input)
                id_to_edit = ""
                if user_input == 0:
                    contacts = createEntry(contacts, [("name", "str"), ("email", "str"), ("phone", "str")])
                elif user_input == 1:
                    contacts = importToDict("./contacts.txt", ["name", "email", "phone"])
                elif user_input == 2:
                    break
            except Exception as e:
                printCritical(e)
            else:
                printWorking("Working...")
            finally:
                print("-----------------------------------")
        elif contacts != {}:
            user_input = askMenu([
                "Add a new contact", 
                "Edit an existing contact", 
                "Delete a contact", 
                "Search for a contact", 
                "Display all contacts", 
                "Export contacts to a text file", 
                "Import contacts from a text tile", 
                "Quit"], 
                "Please choose an operation: ")
            try:
                user_input = int(user_input)
                id_to_edit = ""
                if user_input == 0:
                    contacts = createEntry(contacts, [("name", "str"), ("email", "str"), ("phone", "str")])
                elif user_input == 1:
                    search_method = int(askMenu(["Edit from full list", "Search for contact to edit"], "Please choose an operation: "))
                    id_to_edit = ""
                    if search_method == 0:
                        list_of_contacts = contacts.items()
                        index_to_edit = int(askMenu(list_of_contacts, "Please choose one to edit: "))
                        id_to_edit = list(list_of_contacts)[index_to_edit][0]
                    elif search_method == 1:
                        if contacts != {}:
                            id_to_edit = searchEntry(contacts, ["name", "email", "phone"])[0]
                    if id_to_edit != "" and id_to_edit != -1:
                        editEntry(contacts, id_to_edit, ["name", "email", "phone"])
                    else:
                        print("Unable to find an entry to edit!")
                elif user_input == 2:
                    search_method = int(askMenu(["Delete from full list", "Search for contact to delete"], "Please choose an operation: "))
                    id_to_delete = ""
                    if search_method == 0:
                        list_of_contacts = contacts.items()
                        index_to_delete = int(askMenu(list_of_contacts, "Please choose one to delete: "))
                        id_to_delete = list(list_of_contacts)[index_to_delete][0]
                    elif search_method == 1:
                        if contacts != {}:
                            id_to_delete = searchEntry(contacts, ["name", "email", "phone"])[0]
                    if id_to_delete != "" and id_to_delete != -1:
                        deleteEntry(contacts, id_to_delete)
                    else:
                        print("Unable to find an entry to delete!")
                elif user_input == 3:
                    entry = searchEntry(contacts, ["name", "email", "phone"])
                    displayEntries(entry, "Contact Info: ")
                elif user_input == 4:
                    displayEntries(contacts, "Contacts: ")
                elif user_input == 5:
                    exportItemsToFile(contacts, "contacts.txt")
                elif user_input == 6:
                    contacts = importToDict("./contacts.txt", ["name", "email", "phone"])
                elif user_input == 7:
                    break
            except Exception as e:
                printCritical(e)
            else:
                printWorking("Working...")
            finally:
                print("-----------------------------------")

mainLoop()


