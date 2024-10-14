# Розробіть скрипт, який приймає шлях до директорії в якості аргументу командного рядка і 
# візуалізує структуру цієї директорії, виводячи імена всіх піддиректорій та файлів. Для кращого 
# візуального сприйняття, імена директорій та файлів мають відрізнятися за кольором.


from colorama import Fore, Back, Style
import sys 
from pathlib import Path

# Скрипт відображати як імена директорій, так і імена файлів, використовуючи 
# рекурсивний спосіб обходу директорій .
def get_path_content (folder_path : str = '') :

    if Path(folder_path).exists() :
        for x in Path(folder_path).iterdir() :
            if x.is_dir() :
                print(Fore.GREEN + f"{x}")   
                #If dir -> parse it          
                get_path_content (x)
            else :
                # Використання бібліотеки colorama для реалізації кольорового виведення.
                print(Fore.BLUE + f"{x}")
    else :
        # Повинна бути перевірка та обробка помилок, наприклад, якщо вказаний шлях не існує або він не 
        # веде до директорії.       
        print("Not a path")


def main() :
    # Check if no input
    if len(sys.argv) > 1 :
        # Скрипт має отримувати шлях до директорії як аргумент при запуску. Цей шлях вказує, де знаходиться 
        # директорія, структуру якої потрібно відобразити.
        folder_path = sys.argv[1]
        print(f"Your path {folder_path}")
        get_path_content(folder_path)
    else :
        print("No file path")

    print(Style.RESET_ALL)

#for test purpose: python task_3\main.py D:\MyRepos\goit-pycore-hw-04-1\.venv

if __name__ == "__main__":
    main()
