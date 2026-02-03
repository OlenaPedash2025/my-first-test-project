# %%
# Optional Tasks (K4 - K6)
# Create: Build a CLI-based inventory list where users can append new items via a loop.
# Imperative Programming Approach
import json as js
from pathlib import Path

FILE_PATH = Path(__file__).parent / "resources" / "exhibits.json"


def load_data():
    if FILE_PATH.exists():
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            try:
                return js.load(file)
            except js.JSONDecodeError:
                print("Error: JSON file is corrupted. Starting with an empty list.")
                return []
    return []


def save_data(exhibits):
    FILE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        js.dump(exhibits, file, indent=4, ensure_ascii=False)
    print("Exhibits saved successfully.")


def show_exhibit_details(exhibit):
    display_status = "On Display" if exhibit['is_on_display'] else "In Storage"
    print(f"ID: {exhibit['id']}")
    print(f"Title: {exhibit['exhibit_title']}")
    print(f"Creation Year: {exhibit['creation_year']}")
    print(f"Display Status: {display_status}")
    print(f"Weight (kg): {exhibit['weight_kg']}")
    print(f"Creator: {exhibit['creator']}")
    print("-" * 20)


def add_item(exhibits):
    print("--Add new exhibit--")

    while True:
        exhibit_title = input(
            "Enter the name of the new item to add: ").strip()
        if exhibit_title:
            break
        print("Exhibit title cannot be empty. Please try again.")

    while True:
        try:
            creation_year = int(
                input("Enter the creation year of the item: ").strip())
            break
        except ValueError:
            print("Invalid year. Please enter a valid number.")

    while True:
        is_on_display = input(
            "Is the item on display? (yes/no): ").strip().lower()
        if is_on_display in ['yes', 'no']:
            is_on_display = (is_on_display == 'yes')
            break
        print("Invalid input. Please enter 'yes' or 'no'.")

    while True:
        try:
            weight_kg = float(
                input("Enter the weight of the item in kg: ").strip())
            break
        except ValueError:
            print("Invalid weight. Please enter a valid number.")

    while True:
        creator = input("Enter the creator of the item: ").strip()
        if creator:
            break
        print("Creator cannot be empty. Please try again.")
    new_id = max([ex.get("id", 0) for ex in exhibits], default=0) + 1
    new_exhibit = {
        "id": new_id,
        "exhibit_title": exhibit_title,
        "creation_year": creation_year,
        "is_on_display": is_on_display,
        "weight_kg": weight_kg,
        "creator": creator
    }
    exhibits.append(new_exhibit)
    print("New exhibit added successfully: /n")
    show_exhibit_details(new_exhibit)


def list_of_exhibits(exhibits):
    if not exhibits:
        print("No exhibits in the inventory.")
        return
    print("\n--Current Exhibits--")
    for idx, exhibit in enumerate(exhibits, start=1):
        show_exhibit_details(exhibit)


def search_exhibit_by_title(exhibits):
    title: str = str(
        input("Enter the title of the exhibit to search for: ").strip())
    results = [ex for ex in exhibits if title.lower()
               in ex['exhibit_title'].lower()]
    if results:
        print("\n--Search Results--")
        for exhibit in results:
            show_exhibit_details(exhibit)
    else:
        print("No exhibits found with that title.")


def delete_item(exhibits):
    try:
        target_id = int(
            input("Enter the ID of the exhibit to delete: ").strip())
    except ValueError:
        print("Invalid ID. Please enter a valid number.")
        return

    item_to_delete = next(
        (ex for ex in exhibits if ex.get("id") == target_id), None)
    if item_to_delete:
        exhibits[:] = [ex for ex in exhibits if ex.get("id") != target_id]

        print(f"Exhibit deleted successfully:")
        show_exhibit_details(item_to_delete)
    else:
        print(f"ID {target_id} not found.")


def main():
    inventory = load_data()
    print(
        f"Welcome to the Museum Management System. Items loaded: {len(inventory)}")

    while True:
        print("\nMain Menu:")
        print("[1] List All [2] Add New [3] Delete Exhibit [4] Search [5] Save & Exit")
        choice = input("Select: ").strip()

        if choice == "1":
            list_of_exhibits(inventory)
        elif choice == "2":
            add_item(inventory)
        elif choice == "3":
            delete_item(inventory)
        elif choice == "4":
            search_exhibit_by_title(inventory)
        elif choice == "5":
            save_data(inventory)
            print("Shutting down... Goodbye!")
            break
        else:
            print("Unknown command. Please select 1-5.")


if __name__ == "__main__":
    main()
