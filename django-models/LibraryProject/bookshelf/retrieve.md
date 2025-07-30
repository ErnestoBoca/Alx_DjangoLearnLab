```python
book = Book.objects.get(title="1984")
print(book.title, book.author, book.year)
# Output: 1984 George Orwell 1949
```