from django.shortcuts import render
from jobsapp import forms
from jobsapp.models import IndiaJobs
# Create your views here.

def index_view(request):
    return render(request,'jobsapp/base.html')

def disPlay(request):
    jobs_list = IndiaJobs.objects.all()
    return render(request,'jobsapp/display.html',{'jobs_list':jobs_list})

def jobs_view(request):
    form = forms.JobsForm()
    if request.method == 'POST':
        form = forms.JobsForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            print("Data inserted into database successfully...")
        return index_view(request)
    return render(request,'jobsapp/register.html',{'form':form})

# Create your views here.
