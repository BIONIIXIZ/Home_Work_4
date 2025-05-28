from pathlib import Path

contact_file = Path("contacts.txt")

def load_contacts():
    contacts = {}
    if contact_file.exists():
        with open(contact_file, "r") as file:
            for line in file:
                name, phone = line.strip().split(",")
                contacts[name] = phone
    return contacts

def save_contacts(contacts):
    with open(contact_file, "w") as file:
        for name, phone in contacts.items():
            file.write(f"{name},{phone}\n")
