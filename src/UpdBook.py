class UpdBook:

    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre

    def encode(self):
        return self.__dict__
