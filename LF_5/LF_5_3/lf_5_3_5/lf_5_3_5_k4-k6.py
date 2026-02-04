from dataclasses import dataclass


@dataclass
class Exhibit:
    id: int
    exhibit_title: str
    creation_year: int
    is_on_display: bool
    weight_kg: float
    creator: str

    def __str__(self) -> str:
        status = "Yes" if self.is_on_display else "No"
        return (
            f"ID: {self.id}\n"
            f"Title: {self.exhibit_title}\n"
            f"Year: {self.creation_year}\n"
            f"On Display: {status}\n"
            f"Weight: {self.weight_kg}kg\n"
            f"Creator: {self.creator}\n"
            f"{'-' * 20}"
        )


@dataclass
class Gallery:
    name: str
    exhibits: list[Exhibit]
    location: str
    established_year: int

    def __str__(self) -> str:
        return (
            f"Gallery Name: {self.name}\n"
            f"Location: {self.location}\n"
            f"Established Year: {self.established_year}\n"
            f"{'-' * 20}"
        )

    def add_exhibit(self, exhibit: Exhibit):
        self.exhibits.append(exhibit)

    def list_exhibits(self) -> str:
        return "\n".join(str(exhibit) for exhibit in self.exhibits)

    def find_exhibit_by_title(self, title: str) -> list[Exhibit]:
        return [
            exhibit
            for exhibit in self.exhibits
            if title.lower() in exhibit.exhibit_title.lower()
        ]

    def get_exhibit_count(self) -> int:
        return len(self.exhibits)


my_gallery = Gallery("Modern Art Gallery", [], "New York", 1990)
exhibit1 = Exhibit(1, "Starry Night", 1889, True, 0.5, "Vincent van Gogh")
exhibit2 = Exhibit(2, "Mona Lisa", 1503, False, 0.8, "Leonardo da Vinci")

my_gallery.add_exhibit(exhibit1)
my_gallery.add_exhibit(exhibit2)
print(my_gallery)
print("Exhibits in the Gallery:")
print(my_gallery.list_exhibits())
search_results = my_gallery.find_exhibit_by_title("Mona")
print("Search Results for 'Mona':")
for exhibit in search_results:
    print(exhibit)
print(f"Total Exhibits: {my_gallery.get_exhibit_count()}")
print("-" * 40)
