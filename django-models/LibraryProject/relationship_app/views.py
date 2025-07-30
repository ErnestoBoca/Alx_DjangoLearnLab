from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic import ListView
from django.views.generic.detail import DetailView

def list_books(request):
    books = Book.objects.all()
    context = {
        'books':books
    }
    return render(request, 'relationship_app/list_books.html', context=context)


class LibraryDetailView(ListView):
    models = Book
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_queryset(self):
        return Library.objects.get(name='UEM-CE')
