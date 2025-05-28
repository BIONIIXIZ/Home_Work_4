from pathlib import Path
from colorama import Fore , Style, init , Back

init(autoreset=1)

contact_file = Path("contacts.txt")


#Відкриття файлу(котактів) створеного вище.
def open_contact_file():
    contacts = {}
    if contact_file.exists():
        with open(contact_file, "r+") as file:
            for line in file:
                name, phone = line.strip().split(",")
    return contacts

#Парсинг вашого вводу
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


#Додавання контакту
def add_contact(args, contacts):
    if len(args) != 2:
        return "Usage like: add <name> <phone>"
    name, phone = args
    contacts[name] = phone
    return f"Contact '{name}' added."

#видалення контаку(не допрацьовано тому що не знаю як правильно реалізувати так щоб видаляло не тільки імʼя
def remove_contacts(args, contacts):
    name = args[0] + args[1]
    if name in contacts:
        del contacts[name]
        return "Contact removed"
    return "Contact not Found"

def show_all_contacts(contacts):
    if not contacts:
        return "No contact found."
    result = [f"{name}: {phone}" for name, phone in contacts.items()]
    return "\n".join(result)


def bot_ass():
    contacts = open_contact_file()
    print(Back.GREEN + Fore.BLACK+ "Welcome to the assistant bot")
    while True:
        user_input = input("Enter me your command: ").strip().lower()
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(Back.GREEN + Fore.BLACK + 'Bye!')
            break

        elif command == 'hello':
            print(Fore.LIGHTGREEN_EX + "How can i help you?")

        elif command == "add":
            result = add_contact(args, contacts)
            print(Fore.CYAN + result)
        elif command == "show":
            result = show_all_contacts(contacts)
            print(Fore.GREEN + result)
        # elif command == "remove":
        else:
            print(Fore.RED + "Invalid command.")


if __name__ == "__main__":
    bot_ass()