# Ticket BUS
Ticket Bus merupakan suatu aplikasi web berupa pelayanan pemesanan ticket bus 

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Feature Aplikasi
- Memiliki 3 jenis bus (Eksekutif, Bisnia, Ekonomi)
- Memberikan informasi tentang jenis bus
- Memberikan form pemesanan ticket. 

## Tech
Aplikasi ini dibangun dengan menggunakan:
- [HTML] - Bahasa standar pemrograman yang digunakan untuk membuat halaman website
- [Visual Studio Code] - sebuah text editor gratis yang bisa dijalankan di perangkat dekstop berbasis windows, Linux, dan MacOs. 
- [XAMPP] - perangkat lunak berbasis web serber yang bersifat open source serta mendukung di berbagai sistem operasi
- [PHP] - bahasa pemrograman server-side, sehingga script dari php nantinya akna diproses pada server
- [JavaScript] - bahasa pemrograman yang digunakan untuk membuat situs dengan konten website yang dinamis. 
- [MySql] - sebuah DBMS (Database Management System) menggunakan perintah SQL (structured Query Laguange) yang banyak digunakan dalam pembuatan aplikasi berbasis website. 
- [CSS] - cascading style sheets yang digunakan untuk menentukan tampilan dan format halaman website
- [Bootstrap] - framework HTML, CSS, dan Javascript yang berfungsi untuk mendesain website responsive dengan cepat dan mudah. 

## Requirement
- XAMPP v3.2.4
- PHP version 7.4.10
- Boostrap 5

## Sctruture
C:.
│   booking.php
│   index.html
│   koneksi.php
│   pricelist.html
│   style.css
│
└───asset
        378c9-04_fr.ia.02-tugas-praktik-demonstrasi_v_feb_2022_bv2.pdf
        bus ekonomi.jfif
        buslucu.jpg
        download.jfif
        kabin bisnis.jfif
        kabin ekonomi.jpeg
        kabin eksekutif.jfif
        
## Installation
Install webserver dan extract pada folder xampp/htdocs
```sh
cd :/xampp/htdocs
```

## Usage
- Pada menu booking user akan melihat form pemesanan 
- masukkan nama lengkap, nomor identitas berupa nomor NIK, nomor handhpone, kelas penumpang (eksekutif, bisnis, ekonomi), tanggal keberangkatan, jumlah penumpang dewasa dan lansia. 
- apabila user ingin mengetahui jumlah harga yang harus dibayar maka klik total bayar
- apabila user ingin melakukan proses pembayaran maka klik bayar
- aoabila user ingin menghapus isi dari form maka klik cancel. 




