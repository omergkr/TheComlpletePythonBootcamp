class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        # print("A book object has been deleted")
        pass


my_book = Book("math", "Sammy", 200)
print(str(my_book))
print(my_book)
print(len(my_book))
