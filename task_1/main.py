from data import load_data, clean_data
from processing import calculate_statistics


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

def main():
    filename = "task_1/employees.txt"
    raw_data = load_data(filename)
    employees = clean_data(raw_data)
    
    total, average = calculate_statistics(employees)

    if total:
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    else:
        print("No data available.")

if __name__ == "__main__":
    main()