from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# TODO: Create your views here.

def show_my_watch_list(request):
    data_my_watch_list = MyWatchList.objects.all()

    data_watched = data_my_watch_list.filter(watched=True)
    data_unwatched = data_my_watch_list.filter(watched=False)

    if len(data_watched) >= len(data_unwatched):
        pesan = "Selamat, kamu sudah banyak menonton! :D"
    else:
        pesan = "Wah, kamu masih sedikit menonton!"

    context = {
        'nama' : 'Rebeka',
        'NPM' : '2106653060',
        'mywatchlist': data_my_watch_list,
        'pesan' : pesan
    }

    return render(request, "mywatchlist.html", context)

def show_my_watch_list_xml(request):
    data_my_watch_list = MyWatchList.objects.all()

    return HttpResponse(serializers.serialize("xml", data_my_watch_list), content_type = "application/xml")

def show_my_watch_list_json(request):
    data_my_watch_list = MyWatchList.objects.all()

    return HttpResponse(serializers.serialize("json", data_my_watch_list), content_type = "application/json")
    
