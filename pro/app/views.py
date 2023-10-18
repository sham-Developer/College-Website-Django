from django.shortcuts import render, redirect
from .forms import RegForm
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def about(request):
    if request.user.is_authenticated:
        return render(request, 'about.html')
    else:
        return redirect('/')

def blog(request):
    if request.user.is_authenticated:
        return render(request, 'blog.html')
    else:
        return redirect('/')

def contact(request):
    if request.user.is_authenticated:
        return render(request, 'contact.html')
    else:
        return redirect('/')

def course(request):
    if request.user.is_authenticated:
        return render(request, 'course.html')
    else:
        return redirect('/')

def signup(request):
    if request.method=="POST":
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Congradulation on successful login. Click here to login ")
            return redirect('login')
    else:
        form = RegForm

    context = {'form':form}
    return render(request, "signup.html", context)


# Create your views here.
