import os, re
from pathlib import Path


def load_data(filename: str) -> list[str]:
    
    path = Path(filename)
    
    if path.exists() :
        with open(filename, "r") as file:
            return file.readlines()
    else :
        print("No such file")
        return []

def clean_data(employees_data: list[str]) -> list[float]:
    
    if employees_data :
        return [float(re.sub(r"[^\d]", '', temp.strip())) for temp in employees_data if temp.strip()]
    else :
        return []