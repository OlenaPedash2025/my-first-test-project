# Mandatory Tasks (K1 - K3)
# Define: Create a Python class Artist with a constructor (__init__).
# Behavior: Add a method calculate_age() to the class.
# Instantiate: Create two different Artist objects and print their data.
# Inherit: Create a subclass MuseumStaff that inherits from a generic Person class.
# Private State: Use the _ prefix to mark an attribute as internal and provide a public method to view it.

from datetime import date
from typing import Optional


class Artist:
    def __init__(
        self,
        artist_id: int,
        first_name: str,
        last_name: str,
        genre: Optional[str] = None,
        date_of_birth: int = 0,
        birth_place: Optional[str] = None,
        country: Optional[str] = None,
    ):
        self._id = artist_id
        self._first_name = first_name
        self._last_name = last_name
        self._genre = genre
        self._birth_year = date_of_birth
        self._birth_place = birth_place
        self._country = country

    def __str__(self) -> str:
        return f"Artist: {self._first_name} {self._last_name}, Genre: {self._genre}, Born: {self._birth_year}, Birth Place: {self._birth_place}, Country: {self._country}"

    @property
    def full_name(self) -> str:
        return f"{self._first_name} {self._last_name}"

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, value: str):
        if not value.strip():
            raise ValueError("Name cannot be empty")
        self._first_name = value

    @property
    def get_age(self) -> int:
        current_year = date.today().year
        return current_year - self._birth_year


artist1 = Artist(1, "John", "Doe", "Rock", 1990, "New York", "USA")
artist2 = Artist(2, "Jane", "Smith", "Pop", 1985, "Los Angeles", "USA")

print(artist1)
print(f"{artist1.full_name} is {artist1.get_age} years old.")
print(artist2)
print(f"{artist2.full_name} is {artist2.get_age} years old.")


class Person:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    def greet(self) -> str:
        return f"Hello, my name is {self._name} and I am {self._age} years old."


class MuseumStaff(Person):
    def __init__(self, name: str, age: int, position: str):
        super().__init__(name, age)
        self.position = position

    def greet(self) -> str:
        base_greet = super().greet()
        return f"{base_greet} I work as a {self.position} at the museum."
