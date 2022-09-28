from http.client import HTTPResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from todolist.models import Task
from django.contrib.auth.decorators import login_required
from todolist.forms import TaskForm
from django.http import HttpResponseRedirect
from datetime import date

# Create your views here.
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = Task.objects.all().filter(user=request.user)

    context = {
        'nama' : request.user,
        'todolist': data_todolist,
    }

    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def savetask(request):
    task = Task(user=request.user, date=date.today())
    form = TaskForm(request.POST or None, instance=task)
    if (form.is_valid() and request.method == 'POST'):
        form.save()
        return HttpResponseRedirect('/todolist/')

    context = {}

    return render(request, 'form-task.html', context)

def marker(request, id):
   task = Task.objects.get(id = id)
   task.is_finished = not(task.is_finished)
   task.save()
   return redirect('todolist:show_todolist')

def delete_task(request, id):
    task = Task.objects.get(id = id)
    task.delete()
    return redirect('todolist:show_todolist')