# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut adalah salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000 dan mencetak banyak lulusan dengan reputasi yang sangat baik. Namun, terdapat banyak siswa yang tidak menyelesaikan pendidikannya (dropout). Jumlah dropout yang tinggi tentunya menjadi masalah besar untuk sebuah institusi pendidikan. Masalah ini dianggap serius bagi institusi pendidikan karena berdampak pada efektivitas pendidikan dan reputasi institusi tersebut.

### Permasalahan Bisnis
Permasalahan bisnis yang muncul adalah tingginya angka dropout. Institut juga membutuhkan deteksi dini dengan tujuan mendeteksi siswa yang berisiko dropout secepat mungkin agar dapat diberikan bimbimngan khusus. Selain itu, akan dibuat dashboard untuk monitoring performa mahasiswa secara menyeluruh.

### Cakupan Proyek
Proyek ini akan diharapkan menjawab:
1. Bagaimana pengaruh kondisi keuangan mahasiswa terhadap status akhir mereka (Dropout vs Graduate)?
2. Apakah jejak pendidikan seperti jumlah SKS dan nilai dapat menjadi indikator utama untuk memprediksi siswa yang berisiko dropout lebih awal?
3. Apakah faktor usia saat mendaftar atau status beasiswa memiliki korelasi signifikan terhadap kecenderungan mahasiswa untuk menyelesaikan pendidikannya?

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance

Setup environment:
```bash
pip install -r requirements
```

Masuk ke metabase:
```bash

docker-compose up -d

```

Buka browser dan akses metabase:
```
http://localhost:3000

```
Gunakan credentials berikut:

- **Email:** `root@mail.com`
- **Password:** *root123*

## Business Dashboard
Dashboard yang dibuat adalah dashboard untuk monitoring mahasiswa dari segi ekonomi dan juga faktor pendidikan. Dashboard ini mencakup:
1. Total mahasiswa. Total mahasiswa sangatlah penting untuk mengetahui seberapa banyak mahasiswa yang masuk dalam daftar pendidikan.
2. Persentase Dropout. Dengan mengetahui persentase Dropout, institut diharapkan mampu mengurangi persentase dropout lebih dini.
3. Unemployment rate, inflation rate, scholarship dan GDP atau Gross Dosmetic Product. TIngkat pengangguran dan juga tingkat inflasi dapat menjadi pemicu utama ekonomi mahasiswa melemah sehingga berpotensi mengganggu fokus pendidikan. GDP juga menjadi faktor untuk memperkuat argumen apakah mahasiswa mengalami kelemahan ekonomi karena adanya krisis ekonomi atau tidak berpengaruh. Selain itu, pemberian beasiswa juga menjadi faktor penting untuk membantu ekonomi mahasiswa.
4. Nilai semester 1 dan semester 2. Meskipun hanya 2 semester, tetapi 2 semester inilah menjadi pondasi awal motivasi mahasiswa melakukan dropout atau tidak. Dengan menurunnya nilai semester, artinya mahasiswa masih kurang mampu dalam segi pendidikan sehingga membutuhkan perhatian khusus

## Menjalankan Sistem Machine Learning
Untuk menjalankan prototype sistem machine learning, dapat mengakses link berikut:
```
https://submission-rqliaz6rjjwjzcbmd5w32z.streamlit.app/
```

Setelah itu masukkan data-data mahasiswa yang nantinya akan masuk ke dalam tabel tersebut.Setelah itu, tekan prediksi. Setelah melalui proses singkat, akan muncullah prediksi statusnya. Selain itu, tabel untuk prosesnya juga ada yaitu tabel PCA (Principal Component ANalysis)

## Conclusion
Berdasarkan analisis data dan pengembangan model machine learning, dapat disimpulkan bahwa:
1. Faktor Finansial adalah Penentu Utama: Mahasiswa yang terlambat membayar UKT (Tuition fees up to date = 0) dan memiliki status hutang (Debtor) memiliki kecenderungan dropout yang sangat tinggi. Hal itu diperkuat dengan keadaan ekonomi menggunakan parameter Inflation rate, Unemployment rate, dan GDP.
2. Performa Akademik sebagai Alarm Dini: Jumlah mata kuliah yang lulus di semester 1 dan 2 merupakan prediktor paling akurat. Penurunan jumlah kelulusan SKS di awal masa perkuliahan menjadi sinyal kuat bahwa mahasiswa tersebut akan berhenti di tengah jalan.
3. Dukungan Institusi Berpengaruh Positif: Mahasiswa penerima beasiswa memiliki tingkat kelulusan yang jauh lebih stabil. Sebaliknya, mahasiswa yang mendaftar di usia lebih tua (non-traditional students) memiliki risiko dropout yang lebih tinggi, kemungkinan karena tekanan ekonomi atau tanggung jawab luar kampus.
4. Efektivitas Model: Model machine learning yang dikembangkan telah mampu membedakan karakteristik mahasiswa dropout, enrolled, dan graduate dengan baik, sehingga siap digunakan sebagai sistem peringatan dini (Early Warning System).

### Rekomendasi Action Items
Untuk menekan angka dropout, Jaya Jaya Institut disarankan untuk melakukan langkah-langkah berikut:
1. Intervensi Finansial Proaktif: Memberikan skema cicilan atau bantuan keuangan khusus bagi mahasiswa yang memiliki utang atau belum melunasi UKT sebelum mereka memutuskan untuk berhenti.
2. Program Mentoring Akademik: Mengadakan program pendampingan (tutorial) khusus bagi mahasiswa yang gagal lulus lebih dari 2 mata kuliah atau memiliki nilai yang kurang di semester pertama untuk menjaga motivasi dan performa akademik mereka.
3. Optimalisasi Kuota Beasiswa: Memperluas jangkauan beasiswa atau bantuan biaya hidup, terutama bagi mahasiswa usia dewasa yang berprestasi namun terkendala secara ekonomi, karena data menunjukkan bantuan finansial berbanding lurus dengan angka kelulusan.
