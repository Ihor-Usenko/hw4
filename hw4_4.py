def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    if not args:
        return "You have't entered a contact name!"
    if len(args) < 2:
        return "You have't entered a contact phone!"
    else:
        name, phone = args
        contacts[name] = phone
        return "Contact added."


def change_phone(args, contacts):
    if not args:
        return "You have't entered a contact name!"
    if len(args) < 2:
        return "You have't changed a contact phone!"
    if args[0] in contacts:
        contacts[args[0]] = args[1]
        return f"New phone '{args[1]}' for contact '{args[0]}' is saved."
    else:
        return f"Contact '{args[0]}' is not found!"


def show_phone(args, contacts):
    if not args:
        return "You have't entered a contact name!"
    if args[0] in contacts:
        return contacts[args[0]]
    else:
        return f"Contact '{args[0]}' is not found!"


def show_all(contacts):
    return contacts


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").lower()
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print(f"How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_phone(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")


a = 'Igor'
if __name__ == "__main__":
    main()
