**Berikut ini adalah link menuju aplikasi Heroku yang sudah di-deploy**


https://katalog-lab02-2106653060.herokuapp.com/katalog/

**Bagan Request ke Web Aplikasi Django**


<img width="1264" alt="Untitled" src="https://user-images.githubusercontent.com/112610405/190167373-a6d6eba8-3016-4050-a76e-ad6e48d040ca.png">
Dari gambar diatas kita ketahui bahwa bagan tersebut menjelaskan request client ke web aplikasi berbasis Django beserta responnya dimana terdapat kaitan antara urls.py, views.py, models.py, dan berkas html yang ada. Dimulai dari proses permintaan yang dilakukan di server Django melalui __urls__ yang nantinya akan diteruskan ke __views__. Dalam tahapan ini, pihak pengembang akan mengartikan sinyal tersebut sebagai tanda untuk memproses permintaan tersebut. Jika nantinya dalam proses memerlukan keterlibatan database, tentu query akan dipanggil oleh __views__ menuju ke models dan database akan mengembalikan hasil dari query tersebut ke __views__. Selanjutnya saat proses permintaan telah selesai, hasil proses tersebut akan dipetakan ke dalam HTML yang sudah didefinisikan sebelum akhirnya HTML tersebut ditampilkan kepada user.



**Virtual Environment**


Pertama, virtual env itu sendiri merupakan sebuah tools yang digunakan untuk membuat lingkungan python secara virtual yang terisolasi atau dengan kata lain tools untuk mengenkapsulasi serta manajemen package atau library pada proyek. Arti kata terisolasi disini adalah tidak dapat diakses dari lingkungan luar (tertutup) karena masing-masing program python yang berjalan di virtual env tentunya memiliki rules atau modul yang berbeda dan program dibuat agar program dari luar tidak dapat mengakses sedangkan program Python yang berjalan tanpa virtual env hanya bisa menggunakan modul-modul umum atau global saja.


Lalu, mengapa kita perlu menggunakan virtual env? tentunya dikarenakan kita perlu memastikan bahwa setiap kali kita membuat project baru, versi dari sebuah library yang kita gunakan dalam satu project tidak akan berubah meskipun kita melakukan update di library yang sama namun dalam project  lainnya. Misal, saat ini kita sedang mengerjakan Project X yang menggunakan library numpy version 2.0 dan sekarang sedang mengerjakan Project B yang juga menggunakan library numpy. Tetapi , Project B ini memperlukan numpy yang version-nya lebih lama misal 1.0, karena ada library lain yang menggunakan numpy juga dan diharuskan numpy nya version 1.0. Misalnya saat ini kita tidak menggunakan environment manager dan hanya ada satu versi numpy di komputer, maka terpaksa harus downgrade numpy ke version 1.0, nah tetapi ini bisa nge-break Project A. Solusi dari skenario ini adalah untuk menggunakan environment manager dimana kamu harus membuat 2 env yaitu environment A dan environment B, jadi masing-masing project memiliki versi numpy masing-masing. Karena itu kita membutuhkan virtual env agar masing-masing aplikasi memiliki modulnya sendiri.


Selanjutnya apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment? tentunya tetap bisa. Namun, tentu kehadiran virtual env adalah memudahkan user. Dengan demikian, jika tanpa virtual env akan ada kekurangannya. Jika pakai virtual environtment, kita dapat mencegah adanya issue dependency yang terjadi saat ada update atau perbedaan versi seperti yang sudah dijelaskan sebelumnya.


**Cara mengimplementasikan poin 1 sampai dengan 4**


Secara garis besar, kita diminta untuk set-up virtual env dalam pembuatan aplikasi dimana terdapat template yang disediakan untuk kita clone. Dari template yang ada, kita akan mengisi sesuai dengan to-do yang ada.


**Dimulai dari yang pertama, yaitu:**


        urls.py


        urls.py pada project_django



        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', include('example_app.urls')),
            path("katalog/", include("katalog.urls")),
        ]
Diatas terdapat bagian urls.py di project_django, kita menambahkan line path("katalog/", include("katalog.urls")) sebagai arahan untuk mengambil data sesuai dengan request.


**Lalu dilanjut dengan:**

        urls.py pada katalog


        urlpatterns = [
            path("", show_katalog, name = "show_katalog"),
        ]
Terdapat bagian urls.py di katalog, kita menambahkan line app_name = "katalog" untuk menambahkan namespace dalam aplikasi dan line path("", show_katalog, name = "show_katalog") berfungsi sebagai arahan untuk memunculkan isi data dari function show_katalog pada views.py .


**Selanjutnya adalah sebagai berikut:**


        models.py
        class CatalogItem(models.Model):
            item_name = models.CharField(max_length=255)
            item_price = models.BigIntegerField()
            item_stock = models.IntegerField()
            description = models.TextField()
            rating = models.IntegerField()
            item_url = models.URLField()
Terdapat bagian models.py, dimana ada proses pendefinisian database yang akan disimpan pada variabel-variabel untuk dipakai pada views.py.


**Dilanjut dengan bagian views.py:**


        views.py
        from django.shortcuts import render
        from katalog.models import CatalogItem

        #TODO: Create your views here.

        def show_catalog_item(request):
            data_catalog_item = CatalogItem.objects.all()
            context = {
                'nama' : 'Rebeka',
                'NPM' : '2106653060',
                'list_catalog': data_catalog_item
            }

    return render(request, "katalog.html", context)
Terdapat bagian views.py di katalog yang memunculkan function show_katalog yang memuat database pada models.py untuk disimpan pada variabel list_catalog agar variabel bisa digunakan dalam loop pada html dan bisa ditampilkan.


**Dan yang terakhir:**


        html
        {% for item in list_catalog %}
            <tr>
                <th>{{item.item_name}}</th>
                <th>{{item.item_price}}</th>
                <th>{{item.item_stock}}</th>
                <th>{{item.rating}}</th>
                <th>{{item.description}}</th>
                <th>{{item.item_url}}</th>
              </tr>
            {% endfor %}
Terdapat bagian html, dimana ada penambahan loop yang berfungsi untuk memanggil variabel yang telah di-define dalam views.py dimana parameter data yang diambil adalah pada variabel list_barang yang telah di-define untuk mencakup semua isi object pada models.py. Data-data yang sesuai kemudian akan dimunculkan atau ditampilkan dalam aplikasi.
