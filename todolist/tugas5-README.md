# README untuk Tugas 5 PBP


link:
https://katalog-lab02-2106653060.herokuapp.com/todolist/

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
 

 ## Tag HTML5
 
 
Struktur HTML didefinisikan dengan <head></head> dan <body></body> dimana di dalam head terdapat tag yang mengandung informasi terkait halaman tersebut seperti <title></title> untuk judul halaman. Konten atau elemen bisa ditutup dalam <div></div> yaitu divider atau semacam container untuk elemen-elemen lainnya, seperti:
 
 
`<a>` : mendefinisikan suatu hyperlink
 
 
`<b>` : menyajikan teks dalam format bold
 
 
`<body>` : mendefinisikan body dari document
 
 
`<br>` : memberikan line break
 
 
`<button>` : membuat clickable button
 
 
`<div>` : menentukan suatu section dalam document
 
 
`<head>` : mendefinisikan head dari document
 
 
`<h1>` sampai `<h6>` : mendefinisikan heading dari HTML
 
 
`<hr>` : menyajikan garis horizontal
 
 
`<p>` : mendefinisikan paragraf
 
 
`<style>` : memasukkan informasi style pada head document
 
 
`<table>` : mendefinisikan data dari table
 
 
`<td>` : mendefinisikan cell pada table
 
 
`<th>` : mendefinisikan header cell pada table
 
 
`<tr>` : mendefinisikan row cell pada table
 
 
 
## Tipe - tipe CSS Selector
 
 
Selector merupakan sebuah penanda berupa kata kunci, tag html, ataupun simbol untuk memilih suatu elemen HTML yang akan kita beri aturan CSS nantinya. Jadi ia adalah perwakilan dari suatu elemen HTML yang nanti akan kita tentukan style padanya.
 
 
**Universal Selector**
 
 
Universal selector merupakan selector yang sering programmer gunakan untuk memilih dan menyeleksi semua elemen pada suatu dokumen HTML.
Contoh:

`
 * {
 
 
    border: 1px dashed black;
    
    
    color: pink;
    
    
}
 `


Kode di atas akan membuat semua elemen HTML memiliki garis tepi patah-patah berwarna hitam dan warna teksnya akan berwarna pink.


 `
 *{
 
 
    padding: 0;
    
    
    margin: 0;
    
    
}
 `


Kode di atas akan menghilangkan semua padding dan margin yang setiap elemen HTML miliki pada berbagai browser.
 
__Tag Selector__
 
 
Sesuai dengan namanya, selektor tag merupakan selektor yang memilih elemen berdasarkan nama tagnya.
Contoh:


`
 h1{


    color: green;
    
    
}
 `


Nama tag h1 mewakili semua elemen `<h1>` dalam dokumen HTML. Jadi kode di atas akan membuat teks pada seluruh elemen `<h1>` berwarna hijau.
 
 
 **Id Selector**
 
 
Selektor id merupakan selektor yang bersifat unik. Artinya, selektor id hanya dapat kita gunakan untuk satu elemen saja. Untuk membuat selector id kita perlu memulainya dengan tanda pagar (#).
Contoh:


 `
 #first-header{
 
 
    background-color: black;
    
    
    color: pink;
    
    
}
`


Karena bersifat unik atau hanya mengizinkan satu elemen saja, maka ketika kita gunakan pada lebih dari satu elemen hasilnya adalah hanya elemen pertama saja yang akan terseleksi dan mengabaikan elemen selanjutnya.
 
 
 **Class Selector**
 
 
Selektor class hampir sama dengan selektor id, bedanya selektor ini tidak bersifat unik dan untuk membuatnya kita memerlukan tanda titik (.)


`
 .btn-primary{


    background-color: lightblue;
    
    
    color: white;
    
    
}
`


Karena tidak bersifat unik seperti selektor id, maka satu selektor class dapat kita gunakan berulang kali pada lebih dari satu elemen HTML.
 
 
 **Atribut Selector**
 

 Atribut Selector merupakan selector yang memilih elemen berdasarkan tag dan atributnya. Jadi selektor ini hampir sama dengan selektor tag hanya saja atribut dari tag yang dipilih ikut didefinisikan.


`<a title="Link Download" href="#">Download</a>`
 
## Steps implementasi

 
 - Kustomisasi tampilan login, register, dan create-task sesuai dengan keinginan dan semenarik mungkin.

 
- Kustomisasi halaman todo list sesuai dengan target soal yaitu dengan menggunakan cards. Dalam tugas 5 ini, satu task dibuat dalam satu card dan diminta membuat hover dengan menambahkan code dibawah ini:
 
 '
  .card:hover{
  transform: scale(1.1);

  }
  .card{
      transition: transform .5s;
  }
'
 
 
- Membuat masing - masing halaman menjadi responsive sesuai kebutuhan.
 
