## CRUD Operations in Django Shell

### CREATE
```python
from library.models import Book
book = Book.objects.create(title="1984", author="George Orwell", year=1949)
# Output: <Book: Book object (1)>
```

### RETRIEVE
```python
book = Book.objects.get(title="1984")
print(book.title, book.author, book.year)
# Output: 1984 George Orwell 1949
```

### UPDATE
```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
# Output: Nineteen Eighty-Four
```

### DELETE
```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print(Book.objects.all())
# Output: <QuerySet []>
```