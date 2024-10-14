import re, pathlib

# import random
# import pathlib

# current_dir = pathlib.Path(__file__).parent

# def get_random_joke():
#     try:
#         with open(current_dir / "jokes.txt", "r", encoding="utf-8") as file:
#             jokes = file.readlines()
#             return random.choice(jokes).strip()
#     except FileNotFoundError:
#         return "Не вдалося знайти файл з анекдотами."
# Цей код визначає функцію get_random_joke(), яка відкриває файл 
# jokes.txt, розташований у тій же директорії, що й сам скрипт, 
# і вибирає з нього випадковий анекдот. Змінна current_dir визначає 
# директорію, де знаходиться файл скрипту. Нам це необхідно, щоб шлях 
# до файлу current_dir / "jokes.txt" завжди був вірний де б ми 
# не виконали нашу програму.
# 📦example_joke
#  ┣ 📂joke
#  ┃ ┣ 📜jokes.txt
#  ┃ ┣ 📜jokes_handler.py
#  ┃ ┗ 📜__init__.py
#  ┗ 📜main.py
# Файл __init__.py:
# from .jokes_handler import get_random_joke

# from joke import get_random_joke

# def main():
#     name = input("Будь ласка, введіть ваше ім'я: ")
#     print(f"Привіт, {name}!")

#     while True:
#         user_response = input(f"{name}, бажаєте почути анекдот? (так/ні): ").lower()
#         if user_response == "так":
#             print(get_random_joke())
#         elif user_response == "ні":
#             print(f"До побачення, {name}!")
#             break

# if __name__ == "__main__":
#     main()



#У вас є текстовий файл, який містить інформацію про місячні заробітні плати 
# розробників у вашій компанії. Кожен рядок у файлі містить прізвище розробника та його 
# заробітну плату, які розділені комою без пробілів.
# Наприклад:
# Alex Korp,3000
# Nikita Borisenko,2000
# Sitarama Raju,1000


# Функція повинна точно обчислювати загальну та середню суми.
# Функція total_salary(path) має приймати один аргумент - шлях до текстового файлу (path).
# Файл містить дані про заробітні плати розробників, розділені комами. Кожен рядок 
# вказує на одного розробника.
# Результатом роботи функції є кортеж із двох чисел
def create_file(file_path : str = None) -> str :   
    
    #if file_path and  file_path ;

    fh = open("test.file", 'w')
    
    if employees :
        for employee in employees:
            fh.write(f"{employee['name']}, {employee['salary']}\n") 

   # symbols_written = fh.write('hello!')
   # print(symbols_written) 
    fh.close()
    return file_path


def total_salary(file_path : str = "") -> tuple :
    # Повинна бути обробка випадків, коли файл відсутній або пошкоджений.
    # Опрацьовуйте можливі винятки при роботі з файлами, такі як відсутність файлу.
    salary = 0
    empoyees_number = =
   
    with open(file_path, "r") as file_object :
  
        #lines = [el.strip() for el in fh.readlines()]
        while True:
            line = file_object.readline()
            if not line:
                break
           
        pattern = r"[^\d]"
        salary += int(re.sub(pattern, '', line.strip()))
        empoyees_number += 1
                # Використовуйте менеджер контексту with для читання файлів.
        # Пам'ятайте про встановлення кодування при відкриті файлів
        # Для розділення даних у кожному рядку можна застосувати метод split(',').
        # Обрахуйте загальну суму заробітної плати, а потім розділіть її на кількість 
        # розробників, щоб отримати середню зарплату.


empl = [{'name':'Alex Korp', 'salary': 3000},
{'name':'Nikita Borisenko', 'salary': 2000},
{'name':'Sitarama Raju', 'salary': 1000}]

total, average = total_salary(create_file(empl))
#total, average = total_salary(input("Вкажіть шлях до файлу для обчислення: "))
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")