from colorama import init, Fore, Back
from data.parse import parse_input
from data.contacts import add_contact, remove_contact, show_all_contacts, get_phone, change_phone
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
        #Додавання контаку
        elif command == "add":
            print(Fore.YELLOW + add_contact(args, contacts))
            save_contacts(contacts)
        #Видалення контакту
        elif command == "remove":
            print(Fore.LIGHTYELLOW_EX + remove_contact(args, contacts))
            save_contacts(contacts)
        #Показ всіх наявних контактів у файлі contacts.txt
        elif command == "all":
            print(Fore.CYAN + show_all_contacts(contacts))

        elif command == "change":
            print(Fore.YELLOW + change_phone(args, contacts))
            save_contacts(contacts)

        elif command == "phone":
            print(Fore.LIGHTBLUE_EX + get_phone(args, contacts))

        else:
            print(Fore.RED + "Invalid command.")

if __name__ == "__main__":
    bot_ass()
