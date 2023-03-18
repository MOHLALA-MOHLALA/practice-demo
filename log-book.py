contacts = {}  # dictionary to store contacts

# function to add a new contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts[name] = {'phone': phone, 'email': email}
    print("Contact added successfully")

# function to search for a contact
def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print("Name:", name)
        print("Phone:", contacts[name]['phone'])
        print("Email:", contacts[name]['email'])
    else:
        print("Contact not found")

# function to display all contacts
def display_contacts():
    if not contacts:
        print("No contacts found")
    else:
        for name, contact in contacts.items():
            print("Name:", name)
            print("Phone:", contact['phone'])
            print("Email:", contact['email'])
            print()

# main program loop
while True:
    print("Contact Log Book")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Display All Contacts")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        search_contact()
    elif choice == '3':
        display_contacts()
    elif choice == '4':
        break
    else:
        print("Invalid choice")
