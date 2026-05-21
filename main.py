import random
import uuid

AUTHORS = ["Leo Tolstoy", "George Orwell", "J.K. Rowling", "Mark Twain"]
TITLES = ["The Lost World", "Shadows of Tomorrow", "The Last Horizon"]
GENRES = ["Fiction", "Mystery", "Sci-Fi", "Fantasy"]


class Book:
    def __init__(self, title: str, author: str, year: int, pages: int, genre: str, isbn: str):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.genre = genre
        self.isbn = isbn

    def __repr__(self) -> str:
        return f"Book(title={self.title!r}, author={self.author!r}, year={self.year})"


def generate_book() -> Book:
    return Book(
        title=random.choice(TITLES),
        author=random.choice(AUTHORS),
        year=random.randint(1900, 2024),
        pages=random.randint(100, 1000),
        genre=random.choice(GENRES),
        isbn=str(uuid.uuid4())[:13],
    )


if __name__ == "__main__":
    for _ in range(5):
        print(generate_book())