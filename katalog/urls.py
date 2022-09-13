# TODO: Implement Routings Here
from katalog.views import show_catalog_item
from django.urls import path

app_name = 'catalog'

urlpatterns = [
    path('', show_catalog_item, name='show_catalog'),
]