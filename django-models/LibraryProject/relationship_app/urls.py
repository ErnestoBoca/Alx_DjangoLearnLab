from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_books, name='list-books'),
    path('library/', views.LibraryDetailView.as_view(), name='libray-detail')
]