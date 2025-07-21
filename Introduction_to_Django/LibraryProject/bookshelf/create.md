```python
from library.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book.save()
# Output: <Book: Book object (1)> (An instance is created and saved to the database)
```