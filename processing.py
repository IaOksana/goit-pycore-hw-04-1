# Обрахуйте загальну суму заробітної плати, а потім розділіть її на кількість 
# розробників, щоб отримати середню зарплату.

def calculate_statistics (employees : list[float] = None) -> tuple[float, float]:
    
    if not employees:
        return (0, 0)
 
    return (
        sum(employees),
        sum(employees) / len(employees),
    )