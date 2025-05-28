
#Додавання контакту
def add_contact(args, contacts):
    if len(args) != 2:
        return "Usage: add <name> <phone>"
    name, phone = args
    contacts[name] = phone
    return f"Contact '{name}' added."

def remove_contact(args, contacts):
    if not args:
        return "Usage: remove <name>"
    name = args[0]
    if name in contacts:
        del contacts[name]
        return f"Contact '{name}' removed"
    return f"Contact '{name}' not found"

def show_all_contacts(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
