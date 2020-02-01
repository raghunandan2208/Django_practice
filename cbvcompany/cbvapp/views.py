from django.shortcuts import render
from cbvapp.models import Company
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# from django.core.urlresolvers import reverse_lazy

# Create your views here.
class CompanyListView(ListView):
    model = Company

class CompanyDetailView(DetailView):
    model = Company

class CompanyCreateView(CreateView):
    model = Company
    fields = ('name','ceo','location')

class CompanyUpdateView(UpdateView):
    model = Company
    fields = ('name','ceo')

class CompanyDeleteView(DeleteView):
    model = Company
