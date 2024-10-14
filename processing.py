# Обрахуйте загальну суму заробітної плати, а потім розділіть її на кількість 
# розробників, щоб отримати середню зарплату.

def calculate_statistics (employees : list[float] = None) -> tuple:
    
    if not employees:
        return None
 
    return {
        sum(employees),
        sum(employees) / len(employees),
    }