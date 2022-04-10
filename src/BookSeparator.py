import json
from csv import DictReader
from src.ResultedPerson import ResultedPerson
from src.UpdBook import UpdBook

with open("resourses/users.json", "r") as list_of_users:
    users = json.load(list_of_users)

with open("resourses/books.csv", "r") as list_of_books:
    reader = DictReader(list_of_books)
    books = list(reader)

upd_books = []
for book in books:
    updBook = UpdBook(book['Title'], book['Author'], book['Pages'], book['Genre'])
    upd_books.append(updBook)

resulted_persons = []
for user in users['users']:
    resultedPerson = ResultedPerson(user['name'], user['gender'], user['address'], user['age'], [])
    resulted_persons.append(resultedPerson)

i = 0
for updBook in upd_books:
    if i != len(resulted_persons):
        resulted_persons[i].books.append(updBook)
        i = i + 1
    else:
        i = 0

for person in resulted_persons:
    person.encode_books()

temporary_list = []
for person in resulted_persons:
    temporary_list.append(person.encode())

with open("resourses/results.json", "w") as results:
    results.write(json.dumps(temporary_list, indent=4))
