class Book:

    number_of_copies: int

    def __init__(self, name='default', fee=1):
        self.name = name
        self.fee = fee

    def get_price(self, number_of_copies):
        return self.fee * number_of_copies


book1 = Book('A whole new world', 50)
book2 = Book('Think and grow rich', 65)

print(book1.get_price(100))
print(book2.get_price(200))