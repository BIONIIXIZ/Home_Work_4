from colorama import init, Fore, Back
from data.parse import parse_input
from data.contacts import (
    add_contact,
    remove_contact,
    show_all_contacts,
    get_phone,
    change_phone,
)
from data.storage import load_contacts, save_contacts

init(autoreset=True)

def bot_ass():
    contacts = load_contacts()

    print(Back.GREEN + Fore.BLACK + "Welcome to the assistant bot")

    # Словник команд: ключ -> (функція, чи потрібно зберігати)
    operations = {
        "add": (add_contact, True),
        "remove": (remove_contact, True),
        "change": (change_phone, True),
        "phone": (get_phone, False),
        "all": (show_all_contacts, False),
    }

    while True:
        user_input = input("Enter your command: ").strip()
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(Fore.GREEN + "Bye!")
            break

        elif command == "hello":
            print(Fore.LIGHTCYAN_EX + "How can I help you?")

        elif command in operations:
            func, should_save = operations[command]
            try:
                result = func(args, contacts)
                print(Fore.YELLOW + str(result))
                if should_save:
                    save_contacts(contacts)
            except Exception as e:
                print(Fore.RED + f"Error: {e}")

        else:
            print(Fore.RED + "Invalid command.")

if __name__ == "__main__":
    bot_ass()
