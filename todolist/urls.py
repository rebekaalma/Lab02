from todolist.views import marker, register, login_user, logout_user, show_todolist, savetask, delete_task
from django.urls import path


app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', savetask, name='savetask'),
    path('marker/<int:id>', marker, name='marker'),
    path('delete/<int:id>', delete_task, name='delete')
]