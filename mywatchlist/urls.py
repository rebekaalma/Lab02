from mywatchlist.views import show_my_watch_list, show_my_watch_list_xml, show_my_watch_list_json
from django.urls import path


app_name = 'mywatchlist'

urlpatterns = [
    path('html/', show_my_watch_list, name='show_my_watch_list'),
    path('xml/', show_my_watch_list_xml, name='show_my_watch_list_xml'),
    path('json/', show_my_watch_list_json, name='show_my_watch_list_json')
]