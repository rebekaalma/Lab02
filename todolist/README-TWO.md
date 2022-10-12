**Link heroku: **


# Asynchronous Programming Vs Synchronous Programming


Mari kita mulai dari asynchronous programming. Asynchronous programming merupakan sebuah pendekatan pemrograman yang tidak terikat pada input output (I/O)  protocol. Ini menandakan bahwa pemrograman asynchronous tidak melakukan pekerjaannya secara old style / cara lama yaitu dengan eksekusi baris program satu persatu secara hirarki. Asynchronous programming melakukan pekerjaannya tanpa harus terikat dengan proses lain atau dapat kita sebut secara Independent. Untuk lebih jelasnya, mari kita perhatikan Gambar di bawah ini:



 <img width="260" alt="image" src="https://user-images.githubusercontent.com/112610405/195434373-30c0606c-409c-4cdf-83eb-df64fc51632e.png">



Dari gambar diatas terlihat bahwa pendekatan model pemrograman Asynchronous memiliki waktu eksekusi yang lebih cepat 25 detik dibandingkan dengan pendekatan metode pemrograman Synchronous. Terlihat pula, pada asynchronous tiap modul atau task tidak perlu menunggu task lainnya selesai untuk berjalan. Dengan begitu, waktu eksekusi juga dapat menjadi lebih singkat dan cepat.


Berbeda dengan asynchronous, synchronous programming memiliki pendekatan yang lebih old style. Task akan dieksekusi satu persatu sesuai dengan urutan dan prioritas task. Hal ini memiliki kekurangan pada lama waktu eksekusi karena masing-masing task harus menunggu task lain selesai untuk diproses terlebih dahulu.
Namun, bukan berarti Synchronous programming jauh lebih jelek dibandingkan dengan asynchronous programming. Terdapat beberapa hal yang menjadi synchronous programming memiliki keunggulan dibandingkan dengan asynchronous programming. Beberapa diantaranya adalah kemudahan yang ditawarkan oleh synchronous programming dibandingkan dengan asynchronous programming. Kedepannya, 2 pendekatan programming ini akan semakin banyak diadopsi dan berada pada 1 fungsi dan tujuan yang sama. Terlebih dengan semakin berkembangnnya Rest API dan teknologi pemrograman.


# Paradigma Event-Driven Programming 
Event-Driven Programming adalah salah satu teknik pemrograman yang konsep kerjanya tergantung dari kejadian atau event tertentu. Misal ketika tombol A diklik maka nilai label 2 ditambah nilai label 3 lalu dibagi nilai label 4.  Tetapi jika tombol A diklik dan ternyata label satu berisikan penjumlahan. maka program yang dijalankan label 2 ditambah label 3.


Konsep Event-Driven Programming sama seperti konsep pemrograman menggunakan Procedure yaitu pemrograman yang memiliki input, proses dan output. Namun, ada satu penambahan yang berbeda, yaitu konsep pemilihan untuk mengeksekusi proses programnya. Event-Driven programming juga bisa dibilang suatu paradigma pemrograman yang alur programnya ditentukan oleh suatu event / peristiwa yang merupakan keluaran atau tindakan pengguna atau bisa berupa pesan dari program lainnya.  Event yang dimaksud dapat berupa perubahan waktu, button click, button hover, key press, dan sebagainya. Seperti yang kita lakukan pada tugas 6 ini dimana kita membuat modal (sudah ada di html) yang hanya akan muncul jika tombol Add Task diklik. Ada juga menjalankan fungsi yang dibentuk untuk memunculkan atau menghilangkan modal (pop up) untuk melakukan add task.  Selain itu ada .ready(function()) yang berarti ketika pada halaman pertama kali muncul dan siap ditampilan, akan menjalankan perintah-perintah yang sudah diatur pada fungsi tersebut.


# Penerapan Asynchronous Programming pada AJAX
Jika kita menggunakan AJAX, pengambilan data yang berasal dari backend tanpa reloading atau mengirim dan menerima data dari server dapat dilakukan secara asynchronous . Untuk pengimplemantasiannya dapat dilakukan dengan mudah, namun butuh penyesuaian terhadap syntax yang ada. Pada tugas ini, contoh implementasinya adalah  AJAX get dan AJAX post dimana akan ditrigger ketika html mengirim method post ataupun get yang akan ditangkap oleh ajax. Data yang ditangkap akan dikirimkan ke server tanpa melalui browser reload sehingga memberikan pengalaman browsing lebih baik.


# Steps Implementasi
[] route url ke todolist/json dan memanggil fungsi show_ajax.
[] Membuat fungsi show_ajax pada views.py yang mereturn response dalam bentuk Serializer json
[] Import Jquery Ajax dengan tag <script>
[] Menghapus code for loop menggunakan django syntax serta isinya dan membuat id pada div yang menaungi grid-cols
[] Membuat fungsi dalam js yang bernama loadData untuk merender cards todolist yang ada pada database.json dengan method GET yang diarahkan pada url todolist/json. [] Render kemudian dimasukkan kedalam div yang menaungi grid-cols atau card view.
[] Membuat document.ready function agar ketika website tampil, untuk pertama kalinya ia akan merender data data task yang sudah ada pada server
[] Membuat modal dalam tailwind css yang membaut ketika button dipencet, akan menghilangkan tailwind hidden yang sebelumnya sudah dirender. Button yang dibuat akan dipasangkan dengan on click yang menjalankan fungsi open modal dengan parameter true. Ketika parameter true, pop up akan muncul, ketika false, modal akan menghilang.
[] Dalam modal, terdapa form dengan method POST yang akan melakukan tembak ke database. Input dengan type submit yang ada pada form modal akan diarahkan ke todolist/add dan memanggil fungsi add_ajax yang ada pada views.py
[] Membuat fungsi yang dalam js yang ketika form dalam modal disubmit, akan mengirimkan response ajax POST ke todolist/add dan ditangkap oleh fungsi add_ajax
[] Membuat fungsi add_ajax dan mengambil data yang sudah dipost dengan cara request.POST.get dan membuat new object task kemudiam disave dalam database dengan method .save(). Fungsi ini juga mereturn response ok ketka berhasil dijalankan.

