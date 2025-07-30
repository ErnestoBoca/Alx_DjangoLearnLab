Book.objects.filter(author__name=author_name)
Library.objects.get(name=library_name).books.all()
Library.objects.get(name=library_name).librarian