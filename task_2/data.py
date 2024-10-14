import os, re
from pathlib import Path


def load_data(filename: str) -> list[str] :
    
    path = Path(filename)
    
    if path.exists() :
        with open(filename, "r") as file :
            return file.readlines()
    else :
        print("No such file")
        return []

def convert_data(cats_data: list[str]) -> list[dict] :
    
    cats_data_list = []

    for temp in cats_data :
        current_cat_data_list = temp.split(',')
        current_cat_data_dict = {"id" : current_cat_data_list[0], "name" : current_cat_data_list[1], "age" : current_cat_data_list[2].strip()} 
        cats_data_list.append(current_cat_data_dict)

    return cats_data_list