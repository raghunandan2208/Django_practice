from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from authapp.forms import SignUpForm
from django.http import HttpResponseRedirect
# Create your views here.
def home_page_view(request):
    return render(request,'authapp/home.html')

def logout_view(request):
    return render(request,'authapp/logout.html')

def signup_view(request):
    barat = SignUpForm()
    if request.method == 'POST':
        barat = SignUpForm(request.POST)
        user = barat.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'authapp/signup.html',{'form': barat})

@login_required
def salon_page_view(request):
    return render(request,'authapp/salon.html')

@login_required
def massage_page_view(request):
    return render(request,'authapp/massage.html')

@login_required
def repair_page_view(request):
    return render(request,'authapp/repair.html')
