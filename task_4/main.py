# Напишіть консольного бота помічника, який розпізнаватиме команди, що вводяться з клавіатури, 
# та буде відповідати відповідно до введеної команди.
# наш бот-асистент повинен вміти зберігати ім'я та номер телефону, знаходити номер телефону за ім'ям,
# змінювати записаний номер телефону, виводити в консоль всі записи, які зберіг. Щоб реалізувати таку 
# нескладну логіку, скористаємося словником. У словнику будемо зберігати ім'я користувача, як ключ, 
# і номер телефону як значення.

import re

# розбиратиме введений користувачем рядок на команду та її аргументи. 
# Команди та аргументи мають бути розпізнані незалежно від регістру введення.
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args : list[str], contacts : list[dict] = []) -> str:
    if len(args) < 2 : return "Invalid data entered"

    name, phone = args
    contact = {"name" : name, "phone" : phone}
    contacts.append(contact) 
    
    return "Contact added."


def change_contact(args : list[str], contacts : list[dict]) -> str:
    if len(args) < 2 : return "Invalid data entered"
    name, phone = args

    for contact in contacts :       
        if contact["name"] == name : 
            contact["phone"] = phone
            return "Contact updated"

    return ("No such contact")

    
def show_phone(args : list[str], contacts : list[dict]) -> str:
    if len(args) < 1 : return "Invalid data entered"

    for contact in contacts :       
        if contact["name"] == args[0] : 
            return contact["phone"]

    return ("No such contact")



def main() :
    # словник Python для зберігання імен і номерів телефонів. Ім'я буде ключем, а номер телефону – значенням.
    contacts = []

    print("Welcome to the assistant bot!")
    while True:
        user_input  = input("Enter a command: ").strip().lower()
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        #  За цією командою бот зберігає у пам'яті, наприклад у словнику, новий контакт. 
        elif command == "add":
            print(add_contact(args, contacts))
 
        #За цією командою бот виводить всі збереженні контакти з номерами телефонів у консоль
        elif command == "all" :
            if contacts :
                print(contacts)
            else: 
                print("No contacts")

        # За цією командою бот виводить у консоль номер телефону для зазначеного контакту username
        elif command == "phone" :
            print(show_phone(args, contacts))

        # За цією командою бот зберігає в пам'яті новий номер телефону phone для контакту username, що вже існує в записнику.
        elif command == "change" :
            print(change_contact(args, contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()