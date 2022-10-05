# README untuk Tugas 5 PBP


link:


## Inline, Internal, dan Eksternal CSS


Cascading Style Sheets (CSS) adalah bahasa pemrograman untuk mendesain tampilan website yang memiliki tiga metode penulisan kode dengan style berbeda yaitu Inline CSS, Internal CSS, dan External CSS. Tentunya setiap metode penulisan kode CSS memiliki kelebihan, kekurangan, serta manfaatnya yang berbeda-beda.


### Inline CSS
Inline CSS adalah kode CSS yang ditulis langsung pada atribut elemen HTML. Setiap elemen HTML memiliki atribut style, di situ lah inline CSS ditulis. Kurang efisien karena setiap tag HTML yang diberikan harus memiliki style masing-masing. Anda akan lebih sulit dalam mengatur website jika hanya menggunakan inline style CSS. Sebab, Inline CSS digunakan hanya untuk mengubah satu elemen saja.


**Kelebihan**


Sangat membantu ketika hanya ingin menguji dan melihat perubahan pada satu elemen dan memperbaiki kode dengan cepat.
Proses permintaan HTTP yang lebih kecil dan proses load website akan lebih cepat


**Kekurangan**


Tidak efisien karena Inline style CSS hanya bisa diterapkan pada satu elemen HTML
 
 
 
 
### Internal CSS


Dimulai dari Internal CSS yaitu kode CSS yang ditulis di dalam tag <style> dan kode HTML dituliskan di bagian atas (header) file HTML. Internal CSS dapat digunakan untuk membuat tampilan pada satu halaman website dan tidak digunakan pada halaman website yang lain.
Internal CSS biasa dipakai untuk membuat halaman web dengan tampilan yang berbeda. Dengan kata lain, Internal CSS ini bisa dipakai untuk menciptakan tampilan yang unik, pada setiap halaman website.
  
  
**Kelebihan**
 
 
Perubahan pada Internal CSS hanya berlaku pada satu halaman saja sehingga tidak perlu melakukan upload beberapa file karena HTML dan CSS berada dalam satu file.
Class dan ID bisa digunakan oleh internal stylesheet.
 
  
**Kekurangan**
 
 
Tidak efisien apabila ingin menggunakan CSS yang sama dalam beberapa file.
Membuat performa website lebih lemot karena CSS yang berbeda-beda akan mengakibatkan loading ulang setiap kali ganti halaman website. 
  
  
### Ekstrnal CSS
 
 
Eksternal CSS adalah kode CSS yang ditulis terpisah dengan kode HTML Eksternal CSS ditulis di sebuah file khusus yang berekstensi .css. File eksternal CSS biasanya diletakkan setelah bagian <head> pada halaman.Lebih sederhana dan simpel daripada menambahkan kode CSS di setiap elemen HTML yang ingin diatur tampilannya.
  
  
**Kelebihan**
 
 
Ukuran file HTML akan menjadi lebih kecil dan struktur dari kode HTML jadi lebih rapi.
Loading website menjadi lebih cepat.
File CSS dapat digunakan di beberapa halaman website sekaligus. 
 
**Kekurangan**
 
 
Halaman akan menjadi berantakan, ketika file CSS gagal dipanggil oleh file HTML. Hal ini terjadi disebabkan karena koneksi internet yang lambat.
 
 
 
 
