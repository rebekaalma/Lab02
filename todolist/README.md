# Kegunaan `% csrf_token %` pada elemen `<form>` 


CSRF atau singkatan dari Cross Site Request Forgery merupakan sebuah serangan eksploitasi web yang membuat menjebak pengguna karena tanpa sadar mengirim sebuah permintaan atau request ke website melalui website yang sedang digunakan saat itu. Hal tersebut membuat aplikasi web akan mengeksekusi request tersebut yang sebenarnya bukan keinginan dari pengguna.  Oknum yang tidak bertanggung jawab ini biasanya menyematkan link pada sebuah gambar atau yang lain. Apabila kita tidak sengaja mengklik, maka akan dibawa pada sebuah web yang mengandung malicious code atau kode berbahaya. Kode ini dirancang sedemikian rupa sehingga pengguna tidak perlu lagi melakukan aksi lanjutan agar CSRF berhasil karena hanya membutuhkan satu kali klik saja. Maka dari itu, CSRF juga sering disebut one click attack.



Contoh tindakannya sendiri beragam dan yang pastinya merugikan. Contohnya seperti mengganti foto profil dengan gambar orang lain, menghapus akun pengguna, hingga mentransfer uang ke sebuah akun. Oleh karena itu, Django memberikan fasilitas yaitu CSRF Token yang merupakan kode rahasia acak dan unik untuk setiap situs tertentu. CSRF Token akan dikirimkan dengan setiap form yang dikirimkan oleh web kepada user sebagai proteksi dari serangan eksploitasi web. Semua request yang masuk harus memiliki cookie CSRF, CSRF Token juga harus ada dan benar yang membuat sulit bagi oknum yang tidak bertanggung jawab tersebut untuk meniru request yang sama karena CSRF Token sangat panjang. Tanpa CSRF Token, pengguna akan mendapatkan 403 error.
