Library.objects.get(name=library_name).books.all()
author = Author.objects.get(name=author_name)
Book.objects.filter(author=author)
Library.objects.get(library=library_name).librarian