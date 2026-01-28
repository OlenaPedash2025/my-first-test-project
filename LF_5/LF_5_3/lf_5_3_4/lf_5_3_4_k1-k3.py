#%%
from datetime import datetime
import json
import os  
from typing import List, Optional

from models import Exhibit


script_dir = os.path.dirname(os.path.abspath(__file__)) 
file_path = os.path.join(script_dir, 'resources', 'exhibits.json')

def load_exhibits(file_path: str) -> List[Exhibit]:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from '{file_path}'.")
        return []
    
exhibits_list: List[Exhibit] = load_exhibits(file_path)

#K1 Variables: Create a script that uses at least 4 different data types.
title: str = "Gold mask"
creation_year: int = 1234
is_on_display: bool = True
weight_kg: float = 10.2

#K2 Comparison: Implement a logic block that uses and/or to validate an exhibit's date.
#Logic gate: Validating the date range
current_year: int = datetime.now().year

if creation_year <= current_year and creation_year > 0:
    print("Status: Valid historical era exhibit")
else:
    print("Status: Invalid date or Prehistoric era")

#Counting: Write a for loop that iterates through a list of exhibits and prints their titles.
if exhibits_list:
    print("List of Museum Exhibits")
    for exhibit in exhibits_list:
     exhibit_title: Optional[str] = exhibit.get("exhibit_title")
     print(f"Exhibit Title: {exhibit_title}")
else:
    print("No data to display")

#Search: Implement a while loop that searches for a specific string in a list.
search_target: str = "Bronze Chariot Wheel"
found: bool = False
index: int = 0

while index < len(exhibits_list) and not found:
    if exhibits_list[index]["exhibit_title"] == search_target:
        print(f"\nMatch found: {search_target} in {index} element")
        found = True
    index += 1

#Input Logic: Write a program that takes user input and casts it to an Integer safely.

def get_safe_int(promt: str) -> int:
    while True:
        user_input: str = input(promt)

        try:
            validated_data: int = int(user_input)
            if validated_data <= 0:
                print(f"Error: Age cannot be {validated_data}. Please enter a positive number.")
                continue
            if validated_data > 200:
                print(f"Error: This age seems unrealistic. Please enter a valid age.")
                continue
            return validated_data

        except ValueError:
            print(f"Error: {user_input} is not valid data. Please try again.")


if __name__ =="__main__":
    visitor_age: int = get_safe_int("Please, enter your age: ")
# %%
