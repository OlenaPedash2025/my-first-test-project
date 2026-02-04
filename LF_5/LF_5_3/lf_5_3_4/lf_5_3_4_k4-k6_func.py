import json as js
from pathlib import Path
from typing import Any, NamedTuple, TypedDict, Unpack


class Exhibit(NamedTuple):
    id: int
    exhibit_title: str
    creation_year: int
    is_on_display: bool
    weight_kg: float
    creator: str


class ExhibitInputs(TypedDict):
    exhibit_title: str
    creation_year: int
    is_on_display: bool
    weight_kg: float
    creator: str


def get_details(ex: Exhibit) -> str:
    status: str = "Yes" if ex.is_on_display else "No"
    return (
        f"ID: {ex.id} | {ex.exhibit_title} ({ex.creation_year})\n"
        f"Creator: {ex.creator} | Weight: {ex.weight_kg}kg | On Display: {status}\n"
        f"{'-' * 30}"
    )


def add_exhibit(items: list[Exhibit], **kwargs: Unpack[ExhibitInputs]) -> list[Exhibit]:
    new_id: int = max([ex.id for ex in items], default=0) + 1
    new_item: Exhibit = Exhibit(id=new_id, **kwargs)
    return [*items, new_item]


def remove_exhibit(items: list[Exhibit], ex_id: int) -> list[Exhibit]:
    return [ex for ex in items if ex.id != ex_id]


def search_exhibits(items: list[Exhibit], query: str) -> list[Exhibit]:
    return [ex for ex in items if query.lower() in ex.exhibit_title.lower()]


def load_inventory(path: Path) -> list[Exhibit]:
    if not path.exists():
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data: list[dict[str, Any]] = js.load(f)
            return [Exhibit(**item) for item in data]
    except (js.JSONDecodeError, TypeError):
        return []


def save_inventory(path: Path, items: list[Exhibit]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        js.dump([ex._asdict() for ex in items], f, indent=4, ensure_ascii=False)


def main() -> None:
    db_path: Path = Path(__file__).resolve().parent / "resources" / "exhibits.json"
    inventory: list[Exhibit] = load_inventory(db_path)

    while True:
        print("\n[1] List All [2] Add New [3] Delete [4] Search [5] Exit")
        choice: str = input("Action: ").strip()

        if choice == "1":
            if not inventory:
                print("Vault is empty.")
            for ex in inventory:
                print(get_details(ex))

        elif choice == "2":
            try:
                title: str = input("Title: ").strip()
                year: int = int(input("Year: ").strip())
                display: bool = input("On display? (y/n): ").lower() == "y"
                weight: float = float(input("Weight (kg): ").strip())
                creator: str = input("Creator: ").strip()

                inventory = add_exhibit(
                    inventory,
                    exhibit_title=title,
                    creation_year=year,
                    is_on_display=display,
                    weight_kg=weight,
                    creator=creator,
                )
                save_inventory(db_path, inventory)
                print("Added successfully.")
            except ValueError:
                print("Input error.")

        elif choice == "3":
            try:
                ex_id: int = int(input("ID to delete: "))
                new_inventory: list[Exhibit] = remove_exhibit(inventory, ex_id)
                if len(new_inventory) < len(inventory):
                    inventory = new_inventory
                    save_inventory(db_path, inventory)
                    print(f"Item #{ex_id} removed.")
                else:
                    print("ID not found.")
            except ValueError:
                print("Invalid ID.")

        elif choice == "4":
            query: str = input("Search query: ").strip()
            results: list[Exhibit] = search_exhibits(inventory, query)
            for res in results:
                print(get_details(res))
            if not results:
                print("No matches found.")

        elif choice == "5":
            break


if __name__ == "__main__":
    main()
