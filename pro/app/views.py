from django.shortcuts import render, redirect
from .forms import RegForm
from django.contrib.auth import authenticate, login, logout
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

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "logged out Successfully")
    return redirect('/')

def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=="POST":
            name=request.POST.get('username')
            pwd = request.POST.get('password')
            user = authenticate(request, username=name, password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request, "logged in Successfully")
                return redirect('/')
            else:
                messages.error(request, "Invalid User name or Password")
                return redirect('/login')
        return render(request, 'login.html')
    
def error404(request, exception):
    return render(request, '404p.html', {})
# Create your views here.
