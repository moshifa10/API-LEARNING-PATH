from api import view_events, create_event, delete_event

def menu():
    print("\n==== Mini CLI Calendar ====")
    print("1. View events")
    print("2. Create event")
    print("3. Delete event")
    print("4. Exit")

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        view_events()
    elif choice == "2":
        title = input("Enter event title: ")
        body = input("Enter event description: ")
        create_event(title, body)
    elif choice == "3":
        event_id = input("Enter event ID to delete: ")
        delete_event(event_id)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
