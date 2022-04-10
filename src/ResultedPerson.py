class ResultedPerson:

    def __init__(self, name, gender, address, age, books):
        self.name = name
        self.gender = gender
        self.address = address
        self.age = age
        self.books = books

    def encode_books(self):
        temporary_list = []
        for book in self.books:
            temporary_list.append(book.encode())
        self.books = temporary_list

    def encode(self):
        return self.__dict__
