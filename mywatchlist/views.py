from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# TODO: Create your views here.

def show_my_watch_list(request):
    data_my_watch_list = MyWatchList.objects.all()
    context = {
        'nama' : 'Rebeka',
        'NPM' : '2106653060',
        'mywatchlist': data_my_watch_list
    }

    return render(request, "mywatchlist.html", context)

def show_my_watch_list_xml(request):
    data_my_watch_list = MyWatchList.objects.all()

    return HttpResponse(serializers.serialize("xml", data_my_watch_list), content_type = "application/xml")

def show_my_watch_list_json(request):
    data_my_watch_list = MyWatchList.objects.all()

    return HttpResponse(serializers.serialize("json", data_my_watch_list), content_type = "application/json")
    
