from django.shortcuts import render
from django.views.generic import ListView,DetailView
from cbvapp.models import Book
# Create your views here.

class BookListView(ListView):
    model = Book

class BookDetailView(DetailView):
    model = Book
