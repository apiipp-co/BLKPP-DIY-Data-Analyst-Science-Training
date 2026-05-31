# 🎬 DVD Rental Data Analysis Project

## 📌 Project Overview
Project ini bertujuan untuk menganalisis performa bisnis DVD Rental menggunakan data transaksi penyewaan film. Analisis dilakukan melalui proses SQL JOIN, Data Cleaning, Exploratory Data Analysis (EDA), dan Data Visualization untuk menghasilkan insight bisnis yang dapat membantu perusahaan memahami perilaku pelanggan, performa penjualan, serta faktor-faktor yang memengaruhi pendapatan.

Dataset yang digunakan merupakan DVD Rental Database yang terdiri dari beberapa tabel relasional seperti customer, payment, rental, inventory, film, category, store, city, dan country.

## 👥 Team Members
**👨‍💻 Kelompok 1 — DVD Rental Data Analysis Project**
| Name |
|------|
| Afif |
| Dewi |
| Aini |

## 📂 Dataset
Project ini menggunakan **DVD Rental Database**, yaitu dataset relasional yang mensimulasikan operasional bisnis penyewaan DVD. Dataset terdiri dari beberapa tabel yang saling terhubung melalui primary key dan foreign key sehingga memungkinkan analisis bisnis yang komprehensif.

### Tabel yang Digunakan
| Tabel | Deskripsi |
|---------|---------|
| actor | Data aktor yang bermain dalam film |
| address | Informasi alamat pelanggan, staf, dan toko |
| category | Kategori atau genre film |
| city | Data kota |
| country | Data negara |
| customer | Data pelanggan |
| film | Informasi detail film |
| film_actor | Relasi antara film dan aktor |
| film_category | Relasi antara film dan kategori |
| film_text | Deskripsi teks film |
| inventory | Data stok DVD yang tersedia di toko |
| language | Bahasa film |
| payment | Data pembayaran pelanggan |
| rental | Data transaksi penyewaan film |
| staff | Data staf toko |
| store | Data toko DVD Rental |

### Tabel Utama Analisis
Dalam project ini, analisis berfokus pada tabel:

- Payment
- Rental
- Customer
- Film
- Category
- Film Category
- Inventory
- Store
- Staff
- City
- Country

Tabel-tabel tersebut digabungkan menggunakan SQL JOIN untuk menghasilkan dataset analisis yang digunakan pada proses EDA dan visualisasi.

## 🎯 Business Problem
Perusahaan DVD Rental ingin memahami faktor-faktor yang memengaruhi pendapatan bisnis serta perilaku pelanggan agar dapat meningkatkan profitabilitas dan efektivitas operasional.

Beberapa pertanyaan bisnis yang dianalisis dalam project ini meliputi:

1. Bagaimana tren pendapatan DVD Rental dari waktu ke waktu?
2. Bagaimana performa penjualan masing-masing toko?
3. Genre film apa yang menghasilkan pendapatan terbesar?
4. Apakah rating film memengaruhi durasi rental pelanggan?
5. Rating film mana yang memberikan kontribusi revenue terbesar?
6. Di negara atau kota mana basis pelanggan terbesar berada?
7. Bagaimana distribusi revenue pelanggan?
8. Apakah terdapat hubungan antara keterlambatan pengembalian film dan total denda yang dibayarkan pelanggan?
