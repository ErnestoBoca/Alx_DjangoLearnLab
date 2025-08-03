from django.urls import path
from .views import list_books, LibraryDetailView, register_view, home_view, login_view, logout_view


urlpatterns = [
    path('list/', list_books, name='list-books'),
    path('library/', LibraryDetailView.as_view(), name='libray-detail'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', home_view, name='home')
]