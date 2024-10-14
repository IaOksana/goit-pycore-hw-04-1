# Розробіть скрипт, який приймає шлях до директорії в якості аргументу командного рядка і 
# візуалізує структуру цієї директорії, виводячи імена всіх піддиректорій та файлів. Для кращого 
# візуального сприйняття, імена директорій та файлів мають відрізнятися за кольором.


from colorama import Fore, Style
import sys 
from pathlib import Path, PurePath

# Скрипт відображати як імена директорій, так і імена файлів, використовуючи 
# рекурсивний спосіб обходу директорій .
def get_path_content (folder_path : str = '', file_prefix :str = "    ") :

    # Check if input is a path
    if Path(folder_path).exists() :
        
        for x in Path(folder_path).iterdir() :

            if x.is_dir() :
                print(Fore.GREEN + f"{file_prefix} {x.name}\\")   
                #If dir -> parse it       
                get_path_content (x, file_prefix + "    ")

            else :
                print(Fore.BLUE + f"{file_prefix} {x.name} ")
    else :  
        print("Not a path")


def main() :
    # Check if no input
    if len(sys.argv) > 1 :
        # Скрипт має отримувати шлях до директорії як аргумент при запуску. 
        folder_path = sys.argv[1]
        print(Fore.YELLOW + f"Your path: {Path(folder_path).parent}\\\n{Path(folder_path).name}\\ ") 
        get_path_content(folder_path)
        print(Style.RESET_ALL)

    else :
        print("No file path")


if __name__ == "__main__":
    main()
