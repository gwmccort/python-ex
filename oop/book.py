

class Book:

    # class var
    name = "glen"

    def __init__(self, title):
        self.title = title


b1 = Book("title1")
print(b1.title)

b2 = Book("2nd title")
print(b2.title)

print(Book.name)
