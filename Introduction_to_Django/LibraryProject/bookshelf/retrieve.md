```python
book = Book.objects.all()
for book in books:
    print(book.title, book.author, book.year)
# Output: 1984 George Orwell 1949
```