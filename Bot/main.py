from colorama import init, Fore, Back
from data.parse import parse_input
from data.contacts import add_contact, remove_contact, show_all_contacts
from data.storage import load_contacts, save_contacts

init(autoreset=True)

def bot_ass():
    contacts = load_contacts()

    print(Back.GREEN + Fore.BLACK + "Welcome to the assistant bot")
    while True:
        user_input = input("Enter your command: ").strip()
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(Fore.GREEN + "Bye!")
            break
        elif command == "hello":
            print(Fore.LIGHTCYAN_EX + "How can I help you?")
        elif command == "add":
            print(Fore.YELLOW + add_contact(args, contacts))
            save_contacts(contacts)
        elif command == "remove":
            print(Fore.LIGHTYELLOW_EX + remove_contact(args, contacts))
            save_contacts(contacts)
        elif command == "show":
            print(Fore.CYAN + show_all_contacts(contacts))
        elif command == "save":
            result = save_contacts(contacts)
            return "Saved in contacts.txt successfully"
        else:
            print(Fore.RED + "Invalid command.")

if __name__ == "__main__":
    bot_ass()
