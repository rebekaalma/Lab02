from http.client import HTTPResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from todolist.models import Task
from django.contrib.auth.decorators import login_required
from todolist.forms import TaskForm
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from datetime import date
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404

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
        # 'todolist': data_todolist,
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

def show_todolist_json(request):
    data_todolist = Task.objects.all().filter(user=request.user)

    return HttpResponse(serializers.serialize("json", data_todolist), content_type = "application/json")

def add_todolist_json(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax and request.method == "POST":
        task = Task(user=request.user, date=date.today())
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login')
@csrf_exempt
def delete_task_ajax(request, id):
    if request.method == "DELETE":
        task = get_object_or_404(Task, id = id)
        task.delete()
    return HttpResponse(status=202)

@login_required(login_url='/todolist/login')
@csrf_exempt
def update_task_ajax(request, id):
    if request.method == "PATCH":
        task = get_object_or_404(Task, id = id)
        task.is_finished = not task.is_finished
        task.save()
    
    result = {
        'fields':{
            'title': task.title,
            'description': task.description,
            'is_finished': task.is_finished,
            'date': task.date,
            },
            'pk': task.pk
        }
        
    return JsonResponse(result)

    
