from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required, user_passes_test

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

def home_view(request):
    return render(request, 'relationship_app/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/register.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form':form})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('login')


def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')