from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.

def show_catalog_item(request):
    data_catalog_item = CatalogItem.objects.all()
    context = {
        'nama' : 'Rebeka',
        'NPM' : '2106653060',
        'list_catalog': data_catalog_item
    }

    return render(request, "katalog.html", context)

