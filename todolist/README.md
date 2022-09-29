Tautan Heroku: https://katalog-lab02-2106653060.herokuapp.com/todolist/ 

# Kegunaan `% csrf_token %` pada elemen `<form>` 


CSRF atau singkatan dari Cross Site Request Forgery merupakan sebuah serangan eksploitasi web yang membuat menjebak pengguna karena tanpa sadar mengirim sebuah permintaan atau request ke website melalui website yang sedang digunakan saat itu. Hal tersebut membuat aplikasi web akan mengeksekusi request tersebut yang sebenarnya bukan keinginan dari pengguna.  Oknum yang tidak bertanggung jawab ini biasanya menyematkan link pada sebuah gambar atau yang lain. Apabila kita tidak sengaja mengklik, maka akan dibawa pada sebuah web yang mengandung malicious code atau kode berbahaya. Kode ini dirancang sedemikian rupa sehingga pengguna tidak perlu lagi melakukan aksi lanjutan agar CSRF berhasil karena hanya membutuhkan satu kali klik saja. Maka dari itu, CSRF juga sering disebut one click attack.



Contoh tindakannya sendiri beragam dan yang pastinya merugikan seperti mengganti foto profil dengan gambar orang lain, menghapus akun pengguna, hingga mentransfer uang ke sebuah akun. Oleh karena itu, Django memberikan fasilitas yaitu CSRF Token yang merupakan kode rahasia acak dan unik untuk setiap situs tertentu. CSRF Token akan dikirimkan dengan setiap form yang dikirimkan oleh web kepada user sebagai proteksi dari serangan eksploitasi web. Semua request yang masuk harus memiliki cookie CSRF, CSRF Token juga harus ada dan benar yang membuat sulit bagi oknum yang tidak bertanggung jawab tersebut untuk meniru request yang sama karena CSRF Token sangat panjang. **Tanpa CSRF Token, pengguna akan mendapatkan 403 error.**


# Elemen `<form>` secara manual


Ya, tentunya kita dapat elemen form secara manual tanpa menggunakan generator seperti `form.as_table` dengan cara mengisi bagian di antara start tag dan end tag form dengan `<input><\input>` berdasarkan keinginan kita. Selanjutnya, kita dapat menambahkan `<input>` sesuai dengan tipe yang dibutuhkan dan name untuk identifier. Setelah form di-submit, akan dikembalikan ke def atau fungsi yang memanggil form tersebut dan kita dapat mengakses input yang dimasukkan dengan menggunakan method `request.POST.get(name yang kita buat).`


# Alur data dari submisi yang dilakukan oleh user


- Menampilkan form default untuk user request
- Mendapatkan data dari user melalui request submit. 
- Setelah mendapatkan data yang diinput, membersihkan dan validasi data tersebut
- Saat ada data yang tidak valid, beri informasi ke user mengenai data mana yang tidak valid untuk prompt ulang
- Saat semua data valid, data tersebut akan disimpan dan lakukan sesuai logic yang kita inginkan dan kita deliver ke dalam context agar dapat di-render ke html
- Untuk tugas 3 PBP kali ini, kita diminta untuk membuat task baru sesuai dengan input title dan description.


Untuk lebih jelas, dapat dilihat seperti flowchart dibawah ini:


<img width="232" alt="image" src="https://user-images.githubusercontent.com/112610405/192869239-33b7a2dd-1de1-4a80-92a6-d602c6b9a1c4.png">


# Step implementasi
- Dalam cmd sesuaikan dengan folder yang dituju dan jalankan python manage.py startapp todolist
- Menambahkan path('todolist/', include('todolist.urls')), di urls.py. .project django agar route dengan url yang ada di todolist dan menjalankan fungsi show_todolist yang ada di todolist/views.py.
- Menambahkan class di todolist/models.py dan membuatnya field sesuai dengan steps dalam soal.
- Membuat fungsi login, logout, register yang masing masing terhubung dengan login.html dan register.html dan membuat restriksi agar user harus login dahulu dengan menambahkan @login_required(login_url='/todolist/login/') diatas fungsi yang merupakan main dari project.
- Mengedit bagian html agar menampilkan user dengan mengakses variable yang ada di context ({{username}}) dan membuat dua buah button yang masing-masing memiliki logical command untuk logout, tambah task baru, dan membuat tabel untuk menampilkan data-data todolist yang sudah di submit ke database.
- Ketika user meng-klik tombol tambah task, user akan diarahkan ke halaman baru todolist/create-task dan akan membuat form yang berisi task dan description yang akan dikirim ke fungsi create di views.py untuk ditambahkan ke database.
- Membuat route agar terhubung dengan fungsi fungsi yang ada di views py ketika mengakses link todolist/register, login, create-task, delete, change, dan lain-lain sesuai kebutuhan soal.
- Deploy ke heroku dan membuat 2 user sesuai dengan soal.
akun 1: rebeka_alma, pass: bkbkbkbk
akun 2: rebeka_2, pass: bkbkbkbk
