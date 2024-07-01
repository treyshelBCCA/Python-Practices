from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    price: float

    def get_book_info(self) -> str:
        return f"{self.title} by {self.author} - ${self.price}"

    def apply_discount(self, discount: float) -> None:
        self.price *= (1 - discount / 100)
