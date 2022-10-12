from todolist.views import marker, register, login_user, logout_user, show_todolist, savetask, delete_task, show_todolist_json, add_todolist_json
from django.urls import path


app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', savetask, name='savetask'),
    path('marker/<int:id>', marker, name='marker'),
    path('delete/<int:id>', delete_task, name='delete'),
    path('json/', show_todolist_json, name='todolist_json'),
    path('add/', add_todolist_json, name='add_todolist_json ')
]