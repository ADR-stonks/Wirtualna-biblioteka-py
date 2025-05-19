class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True  # Domyślnie książka jest dostępna

    def __str__(self):
        return f"\"{self.title}\" autorstwa {self.author}"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.loans = []  # Lista wypożyczeń

    def borrow_book(self, book):
        if book.available:
            loan = Loan(book, self)
            self.loans.append(loan)
            book.available = False
            print(f"{self.name} wypożyczył(a) {book}")
        else:
            print(f"Książka {book} jest już wypożyczona.")

    def return_book(self, book):
        for loan in self.loans:
            if loan.book == book:
                book.available = True
                self.loans.remove(loan)
                print(f"{self.name} zwrócił(a) {book}")
                return
        print(f"{self.name} nie ma wypożyczonej książki {book}.")

    def list_loans(self):
        if self.loans:
            print(f"{self.name} wypożyczył(a):")
            for loan in self.loans:
                print(f"  - {loan.book}")
        else:
            print(f"{self.name} nie ma wypożyczonych książek.")


class Loan:
    def __init__(self, book, member):
        self.book = book
        self.member = member


# ---------- Test działania programu ----------
if __name__ == "__main__":
    # Książki
    book1 = Book("Wiedźmin", "Andrzej Sapkowski")
    book2 = Book("Lalka", "Bolesław Prus")
    book3 = Book("Zbrodnia i kara", "Fiodor Dostojewski")

    # Członkowie biblioteki
    member1 = Member("Alicja", "M001")
    member2 = Member("Bartek", "M002")

    # Wypożyczenia
    member1.borrow_book(book1)
    member1.borrow_book(book2)
    member2.borrow_book(book1)  # Już wypożyczona

    print("\n--- Lista wypożyczeń ---")
    member1.list_loans()
    member2.list_loans()

    # Zwrot
    print("\n--- Zwrot książki ---")
    member1.return_book(book1)
    member2.borrow_book(book1)  # Teraz dostępna

    print("\n--- Lista wypożyczeń po zwrocie ---")
    member1.list_loans()
    member2.list_loans()
