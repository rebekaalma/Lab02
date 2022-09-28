# Kegunaan `% csrf_token %` pada elemen `<form>` 


CSRF atau singkatan dari Cross Site Request Forgery merupakan sebuah serangan eksploitasi web yang membuat menjebak pengguna karena tanpa sadar mengirim sebuah permintaan atau request ke website melalui website yang sedang digunakan saat itu. Hal tersebut membuat aplikasi web akan mengeksekusi request tersebut yang sebenarnya bukan keinginan dari pengguna.  Oknum yang tidak bertanggung jawab ini biasanya menyematkan link pada sebuah gambar atau yang lain. Apabila kita tidak sengaja mengklik, maka akan dibawa pada sebuah web yang mengandung malicious code atau kode berbahaya. Kode ini dirancang sedemikian rupa sehingga pengguna tidak perlu lagi melakukan aksi lanjutan agar CSRF berhasil karena hanya membutuhkan satu kali klik saja. Maka dari itu, CSRF juga sering disebut one click attack.



Contoh tindakannya sendiri beragam dan yang pastinya merugikan. Contohnya seperti mengganti foto profil dengan gambar orang lain, menghapus akun pengguna, hingga mentransfer uang ke sebuah akun. Oleh karena itu, Django memberikan fasilitas yaitu CSRF Token yang merupakan kode rahasia acak dan unik untuk setiap situs tertentu. CSRF Token akan dikirimkan dengan setiap form yang dikirimkan oleh web kepada user sebagai proteksi dari serangan eksploitasi web. Semua request yang masuk harus memiliki cookie CSRF, CSRF Token juga harus ada dan benar yang membuat sulit bagi oknum yang tidak bertanggung jawab tersebut untuk meniru request yang sama karena CSRF Token sangat panjang. **Tanpa CSRF Token, pengguna akan mendapatkan 403 error.**


# Elemen <form> secara manual


Ya, tentunya kita dapat elemen form secara manual tanpa menggunakan generator seperti `form.as_table` dengan cara mengisi bagian di antara start tag dan end tag form dengan `<input><\input>` berdasarkan keinginan kita. Selanjutnya, kita dapat menambahkan `<input>` sesuai dengan tipe yang dibutuhkan dan name untuk identifier. Setelah form di-submit, akan dikembalikan ke def atau fungsi yang memanggil form tersebut dan kita dapat mengakses input yang dimasukkan dengan menggunakan method `request.POST.get(name yang kita buat).`


# Alur data dari submisi yang dilakukan oleh user


- Menampilkan form default untuk user request
- Mendapatkan data dari user melalui request submit. 
- Setelah mendapatkan data yang diinput, membersihkan dan validasi data tersebut
- Saat ada data yang tidak valid, beri informasi ke user mengenai data mana yang tidak valid untuk prompt ulang
- Saat semua data valid, data tersebut akan disimpan dan lakukan sesuai logic yang kita inginkan dan kita deliver ke dalam context agar dapat di-render ke html
- Untuk tugas 3 PBP kali ini, kita diminta untuk membuat task baru sesuai dengan input title dan description.
