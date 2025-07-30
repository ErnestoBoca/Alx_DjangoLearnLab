Book.objects.filter(author__name="Ernest")
Library.objects.first().books.all()
Library.objects.get(name="UEM-CE").librarian