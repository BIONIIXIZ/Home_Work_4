
#Додавання контакту
def add_contact(args, contacts):
    if len(args) != 2:
        return "Usage like: add <name> <phone>"
    name, phone = args
    contacts[name] = phone
    return f"Contact '{name}' added."

def remove_contact(args, contacts):
    if not args:
        return "Usage like: remove <name>"
    name = args[0]
    if name in contacts:
        del contacts[name]
        return f"This Contact '{name}' removed"
    return f"This Contact '{name}' not found"

def show_all_contacts(args, contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def change_phone(args, contacts):
    if len(args) != 2:
        return "Usage like: change <username> <new_phone>"
    name, new_phone = args
    if name not in contacts:
        return f"This Contact '{name}' not found."
    contacts[name] = new_phone
    return f"Phone number for '{name}' changed to {new_phone}."

def get_phone(args, contacts):
    if len(args) != 1:
        return "Usagel like: phone <username>"
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    return f"Contact '{name}' not found."
