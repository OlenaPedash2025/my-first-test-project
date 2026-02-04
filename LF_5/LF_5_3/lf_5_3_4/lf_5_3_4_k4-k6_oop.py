import json as js
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Any, Optional


@dataclass
class Exhibit:
    id: int
    exhibit_title: str
    creation_year: int
    is_on_display: bool
    weight_kg: float
    creator: str

    def get_details(self) -> str:
        status = 'Yes' if self.is_on_display else 'No'
        return (f"ID: {self.id}\n"
                f"Title: {self.exhibit_title}\n"
                f"Year: {self.creation_year}\n"
                f"On Display: {status}\n"
                f"Weight: {self.weight_kg}kg\n"
                f"Creator: {self.creator}\n"
                f"{'-'*20}")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class MuseumInventory:
    def __init__(self, file_path: Path):
        self.file_path: Path = file_path
        self.exhibits: list[Exhibit] = self._load_data()

    def _load_data(self) -> list[Exhibit]:
        if not self.file_path.exists():
            return []
        with open(self.file_path, "r", encoding="utf-8") as f:
            try:
                data = js.load(f)
                return [Exhibit(**item) for item in data]
            except (js.JSONDecodeError, TypeError):
                return []

    def save_data(self) -> None:
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        data = [ex.to_dict() for ex in self.exhibits]
        with open(self.file_path, "w", encoding="utf-8") as f:
            js.dump(data, f, indent=4, ensure_ascii=False)
        print("Inventory saved.")

    def add_item(self, title: str, year: int, display: bool, weight: float, creator: str) -> Exhibit:
        new_id = max([ex.id for ex in self.exhibits], default=0) + 1
        new_ex = Exhibit(new_id, title, year, display, weight, creator)
        self.exhibits.append(new_ex)
        self.save_data()
        return new_ex

    def search_by_title(self, query: str) -> list[Exhibit]:
        return [ex for ex in self.exhibits if query.lower() in ex.exhibit_title.lower()]

    def delete_item(self, target_id: int) -> Optional[Exhibit]:
        for i, ex in enumerate(self.exhibits):
            if ex.id == target_id:
                deleted_item = self.exhibits.pop(i)
                self.save_data()
                return deleted_item
        return None


def main() -> None:
    path = Path(__file__).parent / "resources" / "exhibits.json"

    manager = MuseumInventory(path)

    print(f"Welcome! Items loaded: {len(manager.exhibits)}")

    while True:
        print("\n[1] List [2] Add [3] Delete [4] Search [5] Exit")
        choice = input("Select: ").strip()

        if choice == "1":
            for ex in manager.exhibits:
                print(ex.get_details())

        elif choice == "2":
            title = input("Enter Title: ").strip()
            if not title:
                continue

            try:
                year = int(input("Enter Year: ").strip())
                display_str = input("On Display? (yes/no): ").lower().strip()
                is_on_display = (display_str == 'yes')
                weight = float(input("Enter Weight (kg): ").strip())
                creator = input("Enter Creator: ").strip()

                new_item = manager.add_item(
                    title, year, is_on_display, weight, creator)
                print(f"Success! Added Exhibit #{new_item.id}")
            except ValueError:
                print("Invalid input. Please use numbers for year and weight.")

        elif choice == "3":
            try:
                tid = int(input("ID to delete: "))
                deleted = manager.delete_item(tid)
                print(
                    f"Deleted: {deleted.exhibit_title}" if deleted else "Not found")
            except ValueError:
                print("Invalid ID")

        elif choice == "4":
            query = input("Search for: ")
            results = manager.search_by_title(query)
            for res in results:
                print(res.get_details())

        elif choice == "5":
            manager.save_data()
            break


if __name__ == "__main__":
    main()
