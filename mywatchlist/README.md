
# LINK HEROKU:
https://katalog-lab02-2106653060.herokuapp.com/mywatchlist/html/ 


# JSON


JavaScript Object Notation atau JSON merupakan sebuah format yang digunakan untuk menyimpan, membaca, serta menukar informasi dari web server sehingga dapat dibaca oleh para pengguna. Biasanya, file JSON berisikan teks dan file berekstensi .json. JSON ini berbeda dengan XML, namun keduanya memiliki fungsi yang serupa. JSON ini sendiri terdiri dari dua struktur atau bagian


1. kumpulan value yang saling berpasangan contohnya seperti object


2. kumpulan value yang berurutan seperti misalnya array. Selain itu, JSON dapat digunakan oleh bahasa pemrograman lain seperti PHP, Python, C++, dan Ruby.


# XML
XML adalah bahasa markup yang dirancang untuk menyimpan data. Ini populer digunakan atau transfer data. Case sensitive pada huruf besar/kecil. XML menawarkan kalian untuk menentukan elemen markup dan menghasilkan bahasa markup yang disesuaikan. Unit dasar dalam XML dikenal sebagai elemen. Ekstensi file XML adalah .xml.


Perbedaan dari JSON dengan XML berdasarkan beberapa poin penting, seperti:


**Elemen**


Yang pertama adalah cara menyimpan elemen,  JSON menyimpan elemennya secara efisien akan tetapi tidak rapi untuk dilihat. Sedangkan XML menyimpan elemen-elemen nya dengan cara yang terstruktur, mudah dibaca oleh manusia dan mesin, akan tetapi kurang efisien.


**Ekstensi file**


Nama dari file JSON akan diakhiri dengan ekstensi .json. Sementara file XML akan diakhiri dengan ekstensi .xml.


**Penerapan**


Untuk penerapannya, JSON digunakan untuk mengirimkan data dengan cara data diuraikan dan dikirimkan melalui internet. Sedangkan XML memiliki data yang lebih terstruktur dan pengguna dapat menggunakannya untuk menambahkan catatan.

 
 # HTML
HTML (HyperText Markup Language) adalah suatu bahasa yang menggunakan tanda-tanda tertentu (tag) untuk menyatakan kode-kode yang harus ditafsirkan oleh browser agar halaman tersebut dapat ditampilkan secara benar.
Secara umum, fungsi HTML adalah untuk mengelola serangkaian data dan informasi sehingga suatu dokumen dapat diakses dan ditampilkan di Internet melalui layanan web.


Fungsi HTML yang lebih spesifik yaitu :
- Membuat halaman web.
- Menampilkan berbagai informasi di dalam sebuah browser Internet.
- Membuat link menuju halaman web lain dengan kode tertentu (hypertext).


# Alasan dibutuhkannya data delivery dalam pengimplementasian sebuah platform
Penggunaan data delivery akan menjadi hal yang menguntungkan saat mengimplementasikan suatu platform. Dalam penggunaan sebuah platform, pertukaran data antara client dan server pasti terjadi, misalnya untuk melakukan CRUD (Create, Read, Update, Delete). Pertukaran ini akan dipermudah dan komunikasinya dapat diterima dengan baik dengan data delivery ini. Untuk melakukan data delivery, dapat digunakan format tertentu seperti HTML, JSON, dan XML.


# Step Pengimplementasian
- Mengaktivasi virtual environment di directory project lalu menjalankan ‘python manage.py startapp mywatchlist’ untuk membuat aplikasi Django baru bernama mywatchlist.


- Menambahkan path ` mywatchlist` di file `/project_django/urls.py` dengan kode:
`urlpatterns = [
    ...
    path('mywatchlist/', include('mywatchlist.urls')),
]`
 
 
- Menambahkan `mywatchlist` ke `INSTALLED_APPS` di file `/project_django/settings.py` dengan kode:
`INSTALLED_APPS = [
    ...,
    'mywatchlist',
]`


- Membuat model MyWatchlist di `/mywatchlist/models.py` dengan atribut-atribut yaitu `watched, title, rating, release_date, review` dan field yang sesuai. Kemudian, melakukan migrasi dengan menjalankan `python manage.py makemigration` dan `python manage.py migrate`


- Membuat direktori baru `/mywatchlist/fixtures/movies_catalog.json` dan menambahkan data berupa 10 film yang ingin dimasukkan ke database.


- Membuat fungsi untuk menampilkan data-data tersebut dengan format HTML, JSON, dan XML di `mywatchlist/views.py` kemudian melakukan routing untuk menampilkan masing-masing format dengan menambahkan path pada list `urlpatterns` di `/mywatchlist/urls.py.`


- Menambahkan `&& python manage.py loaddata movies_catalog.json` di baris pertama Procfile. Setelah semua selesai, melakukan `git pull, commit, push` lalu menjalankan workflow yang gagal agar aplikasi mywatchlist ter-deploy di aplikasi Heroku.
 
 # Postman
 
 **html response**
 
 
 ![image](https://user-images.githubusercontent.com/112610405/191510514-ddb3b54f-33b8-418f-aab9-c5f8127a00f1.png)

 
 
 **xml response**
 
 
 ![image](https://user-images.githubusercontent.com/112610405/191510808-8ba26681-c524-4dd1-bbb1-ef1d42e21a7d.png)

 
 **json response**
 
 ![image](https://user-images.githubusercontent.com/112610405/191512473-5c2b822b-ffe6-416c-bd85-78cde18ae4c9.png)

 
 
 
 
 
 
 
 
 
 
 



 
 
 
 
 
 
 



