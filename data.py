import os, re

def load_data(filename: str) -> list[str]:
    with open(filename, "r") as file:
        return file.readlines()

def clean_data(employees_data: list[str]) -> list[float]:
    return [int(re.sub(r"[^\d]", '', temp.strip())) for temp in employees_data if temp.strip()]
