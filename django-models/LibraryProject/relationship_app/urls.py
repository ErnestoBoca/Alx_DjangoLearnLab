from django.urls import path
from .views import list_books
from .views import LibraryDetailView

urlpatterns = [
    path('list/', views.list_books, name='list-books'),
    path('library/', views.LibraryDetailView.as_view(), name='libray-detail')
]