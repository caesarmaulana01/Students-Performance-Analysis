# Proyek Akhir: Menyelesaikan Permasalahan Universitas Jaya Jaya

## Business Understanding

Universitas Jaya Jaya merupakan salah satu institusi pendidikan tinggi yang telah berdiri sejak tahun 2000. Selama lebih dari dua dekade, universitas ini telah berhasil meluluskan banyak mahasiswa dengan prestasi akademik yang membanggakan.

Namun demikian, dalam perjalanannya, Universitas Jaya Jaya menghadapi tantangan serius terkait tingginya angka mahasiswa yang tidak menyelesaikan studi mereka (dropout). Fenomena ini menjadi perhatian besar karena dapat berdampak buruk terhadap reputasi universitas serta menurunkan tingkat kelulusan secara keseluruhan.

Untuk mengatasi masalah ini, pihak universitas berinisiatif untuk melakukan analisis data terhadap performa akademik mahasiswa. Tujuannya adalah untuk:
- Mendeteksi mahasiswa yang berisiko tinggi mengalami dropout sedini mungkin.
- Memberikan intervensi atau bimbingan akademik yang tepat sasaran.
- Meningkatkan angka retensi dan kelulusan mahasiswa.

Sebagai bagian dari solusi, tim data science diminta untuk menganalisis dataset mahasiswa yang telah disediakan. Selain itu, juga diharapkan untuk membangun sebuah dashboard interaktif yang dapat membantu pihak universitas dalam memahami pola-pola performa mahasiswa serta memantau perkembangan mereka secara berkala.

### Permasalahan Bisnis
Universitas Jaya Jaya menghadapi beberapa **permasalahan bisnis utama** yang perlu diselesaikan, yaitu:
1. **Tingginya angka mahasiswa yang tidak menyelesaikan studi mereka (dropout)**, yang dapat berdampak negatif pada reputasi universitas.
2. **Kurangnya sistem deteksi dini** untuk mengidentifikasi mahasiswa yang berisiko tinggi mengalami dropout.
3. **Tidak adanya mekanisme intervensi yang efektif** untuk membantu mahasiswa yang berisiko agar dapat melanjutkan studi mereka.
4. **Keterbatasan dalam memahami pola-pola performa akademik mahasiswa** secara menyeluruh.
5. **Tidak adanya alat bantu seperti dashboard interaktif** untuk memantau perkembangan mahasiswa secara berkala.

**Solusi yang diharapkan** adalah analisis data yang mendalam dan pengembangan sistem berbasis data untuk mengatasi permasalahan ini.

### Cakupan Proyek

Proyek ini mencakup beberapa langkah utama untuk menyelesaikan permasalahan yang dihadapi Universitas Jaya Jaya, yaitu:

1. **Eksplorasi dan Pembersihan Data**  
    - Mengumpulkan dan memahami dataset mahasiswa yang telah disediakan.  
    - Melakukan pembersihan data untuk memastikan kualitas data yang digunakan dalam analisis.  

2. **Analisis Data**  
    - Melakukan analisis eksplorasi data (EDA) untuk mengidentifikasi pola-pola performa akademik mahasiswa.  
    - Menggunakan teknik statistik dan visualisasi data untuk menemukan faktor-faktor yang berkontribusi terhadap risiko dropout.  

3. **Pengembangan Model Prediktif**  
    - Membangun model machine learning untuk mendeteksi mahasiswa yang berisiko tinggi mengalami dropout.  
    - Melakukan evaluasi model untuk memastikan akurasi dan keandalannya.  

4. **Pembuatan Dashboard Interaktif**  
    - Mengembangkan dashboard berbasis web yang dapat digunakan oleh pihak universitas untuk memantau performa mahasiswa.  
    - Menyediakan fitur-fitur seperti visualisasi data, laporan perkembangan, dan notifikasi risiko dropout.  

5. **Dokumentasi dan Deployment**  
    - Menyusun dokumentasi lengkap terkait proses analisis dan pengembangan sistem.  
    - Melakukan deployment sistem machine learning dan dashboard agar dapat diakses oleh pihak universitas.  

6. **Rekomendasi Action Items**  
    - Memberikan rekomendasi berbasis data untuk intervensi yang efektif.  
    
### Persiapan
**Sumber Data**  
Dataset yang digunakan dalam proyek ini berasal dari [Dicoding Dataset](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md), yang mencakup informasi akademik mahasiswa seperti nilai, kehadiran, aktivitas ekstrakurikuler, dan data demografis. Dataset ini telah dianonimkan untuk menjaga kerahasiaan data pribadi mahasiswa.

**Penjelasan Fitur Dataset**  
Dataset ini terdiri dari beberapa kolom dengan deskripsi sebagai berikut:

| **Kolom**                                   | **Deskripsi**                                                                                     | **Keterangan Nilai**                                                                                   |
|---------------------------------------------|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Marital_status                              | Status pernikahan mahasiswa. (Kategorikal)                                                       | 1 = single, 2 = married, 3 = widower, 4 = divorced, 5 = facto union, 6 = legally separated             |
| Application_mode                            | Metode aplikasi yang digunakan oleh mahasiswa. (Kategorikal)                                     | 1 = Tahap pertama - kontingen umum, 2 = Peraturan No. 612/93, 5 = Tahap pertama - kontingen khusus (Pulau Azores), 7 = Pemegang gelar pendidikan tinggi lainnya, 10 = Peraturan No. 854-B/99, 15 = Mahasiswa internasional (sarjana), 16 = Tahap pertama - kontingen khusus (Pulau Madeira), 17 = Tahap kedua - kontingen umum, 18 = Tahap ketiga - kontingen umum, 26 = Peraturan No. 533-A/99, item b2) (Rencana Berbeda), 27 = Peraturan No. 533-A/99, item b3 (Institusi Lain), 39 = Usia di atas 23 tahun, 42 = Transfer, 43 = Perubahan program studi, 44 = Pemegang diploma spesialisasi teknologi, 51 = Perubahan institusi/program studi, 53 = Pemegang diploma siklus pendek, 57 = Perubahan institusi/program studi (Internasional) |
| Application_order                           | Urutan aplikasi mahasiswa. (Numerikal)                                                          | Nilai antara 0 (pilihan pertama) hingga 9 (pilihan terakhir)                                           |
| Course                                      | Program studi yang diambil oleh mahasiswa. (Kategorikal)                                         | 33 = Teknologi Produksi Bahan Bakar Nabati, 171 = Desain Animasi dan Multimedia, 8014 = Pelayanan Sosial (kelas malam), 9003 = Agronomi, 9070 = Desain Komunikasi, 9085 = Keperawatan Hewan, 9119 = Teknik Informatika, 9130 = Equinkultur, 9147 = Manajemen, 9238 = Pelayanan Sosial, 9254 = Pariwisata, 9500 = Keperawatan, 9556 = Kebersihan Mulut, 9670 = Manajemen Periklanan dan Pemasaran, 9773 = Jurnalisme dan Komunikasi, 9853 = Pendidikan Dasar, 9991 = Manajemen (kelas malam) |
| Daytime_evening_attendance                  | Kehadiran mahasiswa (siang/malam). (Kategorikal)                                                 | 1 = siang, 0 = malam                                                                                  |
| Previous_qualification                      | Kualifikasi pendidikan sebelumnya. (Kategorikal)                                                | 1 = Pendidikan menengah, 2 = Pendidikan tinggi - gelar sarjana muda, 3 = Pendidikan tinggi - gelar sarjana, 4 = Pendidikan tinggi - gelar magister, 5 = Pendidikan tinggi - gelar doktor, 6 = Frekuensi pendidikan tinggi, 9 = Tahun ke-12 pendidikan sekolah - belum selesai, 10 = Tahun ke-11 pendidikan sekolah - belum selesai, 12 = Lainnya - Tahun ke-11 pendidikan sekolah, 14 = Tahun ke-10 pendidikan sekolah, 15 = Tahun ke-10 pendidikan sekolah - belum selesai, 19 = Pendidikan dasar siklus ke-3 (tahun ke-9/ke-10/ke-11) atau setara, 38 = Pendidikan dasar siklus ke-2 (tahun ke-6/ke-7/ke-8) atau setara, 39 = Kursus spesialisasi teknologi, 40 = Pendidikan tinggi - gelar sarjana (siklus pertama), 42 = Kursus teknis profesional tingkat tinggi, 43 = Pendidikan tinggi - gelar magister (siklus kedua) |
| Previous_qualification_grade                | Nilai kualifikasi pendidikan sebelumnya. (Numerikal)                                            | Nilai antara 0 hingga 200                                                                             |
| Nationality                                 | Kewarganegaraan mahasiswa. (Kategorikal)                                                        | 1 = Portugis, 2 = Jerman, 6 = Spanyol, 11 = Italia, 13 = Belanda, 14 = Inggris, 17 = Lituania, 21 = Angola, 22 = Tanjung Verde, 24 = Guinea, 25 = Mozambik, 26 = Sao Tome, 32 = Turki, 41 = Brasil, 62 = Rumania, 100 = Moldova (Republik), 101 = Meksiko, 103 = Ukraina, 105 = Rusia, 108 = Kuba, 109 = Kolombia |
| Mothers_qualification                       | Kualifikasi pendidikan ibu mahasiswa. (Kategorikal)                                             | 1 = Pendidikan Menengah - Tahun ke-12 Sekolah atau Setara, 2 = Pendidikan Tinggi - Gelar Sarjana Muda, 3 = Pendidikan Tinggi - Gelar Sarjana, 4 = Pendidikan Tinggi - Gelar Magister, 5 = Pendidikan Tinggi - Gelar Doktor, 6 = Frekuensi Pendidikan Tinggi, 9 = Tahun ke-12 Sekolah - Belum Selesai, 10 = Tahun ke-11 Sekolah - Belum Selesai, 11 = Tahun ke-7 (Lama), 12 = Lainnya - Tahun ke-11 Sekolah, 14 = Tahun ke-10 Sekolah, 18 = Kursus perdagangan umum, 19 = Pendidikan Dasar Siklus ke-3 (Tahun ke-9/ke-10/ke-11) atau Setara, 22 = Kursus teknis-profesional, 26 = Tahun ke-7 Sekolah, 27 = Siklus ke-2 dari kursus sekolah menengah umum, 29 = Tahun ke-9 Sekolah - Belum Selesai, 30 = Tahun ke-8 Sekolah, 34 = Tidak Diketahui, 35 = Tidak Bisa Membaca atau Menulis, 36 = Bisa Membaca Tanpa Memiliki Tahun ke-4 Sekolah, 37 = Pendidikan
| Fathers_qualification                       | Kualifikasi pendidikan ayah mahasiswa. (Kategorikal)                                            | 1 = Secondary Education - 12th Year of Schooling or Eq., 2 = Higher Education - Bachelor's Degree, 3 = Higher Education - Degree, 4 = Higher Education - Master's, 5 = Higher Education - Doctorate, 6 = Frequency of Higher Education, 9 = 12th Year of Schooling - Not Completed, 10 = 11th Year of Schooling - Not Completed, 11 = 7th Year (Old), 12 = Other - 11th Year of Schooling, 13 = 2nd year complementary high school course, 14 = 10th Year of Schooling, 18 = General commerce course, 19 = Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv., 20 = Complementary High School Course, 22 = Technical-professional course, 25 = Complementary High School Course - not concluded, 26 = 7th year of schooling, 27 = 2nd cycle of the general high school course, 29 = 9th Year of Schooling - Not Completed, 30 = 8th year of schooling, 31 = General Course of Administration and Commerce, 33 = Supplementary Accounting and Administration, 34 = Unknown, 35 = Can't read or write, 36 = Can read without having a 4th year of schooling, 37 = Basic education 1st cycle (4th/5th year) or equiv., 38 = Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv., 39 = Technological specialization course, 40 = Higher education - degree (1st cycle), 41 = Specialized higher studies course, 42 = Professional higher technical course, 43 = Higher Education - Master (2nd cycle), 44 = Higher Education - Doctorate (3rd cycle) |
| Mothers_occupation                          | Pekerjaan ibu mahasiswa. (Kategorikal)                                                          | 0 = Student, 1 = Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers, 2 = Specialists in Intellectual and Scientific Activities, 3 = Intermediate Level Technicians and Professions, 4 = Administrative staff, 5 = Personal Services, Security and Safety Workers and Sellers, 6 = Farmers and Skilled Workers in Agriculture, Fisheries and Forestry, 7 = Skilled Workers in Industry, Construction and Craftsmen, 8 = Installation and Machine Operators and Assembly Workers, 9 = Unskilled Workers, 10 = Armed Forces Professions, 90 = Other Situation, 99 = (blank), 122 = Health professionals, 123 = teachers, 125 = Specialists in information and communication technologies (ICT), 131 = Intermediate level science and engineering technicians and professions, 132 = Technicians and professionals, of intermediate level of health, 134 = Intermediate level technicians from legal, social, sports, cultural and similar services, 141 = Office workers, secretaries in general and data processing operators, 143 = Data, accounting, statistical, financial services and registry-related operators, 144 = Other administrative support staff, 151 = personal service workers, 152 = sellers, 153 = Personal care workers and the like, 171 = Skilled construction workers and the like, except electricians, 173 = Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like, 175 = Workers in food processing, woodworking, clothing and other industries and crafts, 191 = cleaning workers, 192 = Unskilled workers in agriculture, animal production, fisheries and forestry, 193 = Unskilled workers in extractive industry, construction, manufacturing and transport, 194 = Meal preparation assistants |
| Fathers_occupation                          | Pekerjaan ayah mahasiswa. (Kategorikal)                                                         | 0 = Student, 1 = Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers, 2 = Specialists in Intellectual and Scientific Activities, 3 = Intermediate Level Technicians and Professions, 4 = Administrative staff, 5 = Personal Services, Security and Safety Workers and Sellers, 6 = Farmers and Skilled Workers in Agriculture, Fisheries and Forestry, 7 = Skilled Workers in Industry, Construction and Craftsmen, 8 = Installation and Machine Operators and Assembly Workers, 9 = Unskilled Workers, 10 = Armed Forces Professions, 90 = Other Situation, 99 = (blank), 101 = Armed Forces Officers, 102 = Armed Forces Sergeants, 103 = Other Armed Forces personnel, 112 = Directors of administrative and commercial services, 114 = Hotel, catering, trade and other services directors, 121 = Specialists in the physical sciences, mathematics, engineering and related techniques, 122 = Health professionals, 123 = teachers, 124 = Specialists in finance, accounting, administrative organization, public and commercial relations, 131 = Intermediate level science and engineering technicians and professions, 132 = Technicians and professionals, of intermediate level of health, 134 = Intermediate level technicians from legal, social, sports, cultural and similar services, 135 = Information and communication technology technicians, 141 = Office workers, secretaries in general and data processing operators, 143 = Data, accounting, statistical, financial services and registry-related operators, 144 = Other administrative support staff, 151 = personal service workers, 152 = sellers, 153 = Personal care workers and the like, 154 = Protection and security services personnel, 161 = Market-oriented farmers and skilled agricultural and animal production workers, 163 = Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence, 171 = Skilled construction workers and the like, except electricians, 172 = Skilled workers in metallurgy, metalworking and similar, 174 = Skilled workers in electricity and electronics, 175 = Workers in food processing, woodworking, clothing and other industries and crafts, 181 = Fixed plant and machine operators, 182 = assembly workers, 183 = Vehicle drivers and mobile equipment operators, 192 = Unskilled workers in agriculture, animal production, fisheries and forestry, 193 = Unskilled workers in extractive industry, construction, manufacturing and transport, 194 = Meal preparation assistants, 195 = Street vendors (except food) and street service providers |
| Admission_grade                             | Nilai penerimaan mahasiswa. (Numerikal)                                                         | Nilai antara 0 hingga 200                                                                             |
| Displaced                                   | Apakah mahasiswa berasal dari luar daerah. (Kategorikal)                                        | 1 = yes, 0 = no                                                                                       |
| Educational_special_needs                   | Apakah mahasiswa memiliki kebutuhan pendidikan khusus. (Kategorikal)                            | 1 = yes, 0 = no                                                                                       |
| Debtor                                      | Apakah mahasiswa memiliki tunggakan. (Kategorikal)                                              | 1 = yes, 0 = no                                                                                       |
| Tuition_fees_up_to_date                     | Apakah pembayaran biaya kuliah mahasiswa sudah lunas. (Kategorikal)                             | 1 = yes, 0 = no                                                                                       |
| Gender                                      | Jenis kelamin mahasiswa. (Kategorikal)                                                          | 1 = male, 0 = female                                                                                   |
| Scholarship_holder                          | Apakah mahasiswa adalah penerima beasiswa. (Kategorikal)                                        | 1 = yes, 0 = no                                                                                       |
| Age_at_enrollment                           | Usia mahasiswa saat mendaftar. (Numerikal)                                                      | Nilai numerikal                                                                                        |
| International                               | Apakah mahasiswa adalah mahasiswa internasional. (Kategorikal)                                  | 1 = yes, 0 = no                                                                                       |
| Curricular_units_1st_sem_credited           | Jumlah mata kuliah yang diakui pada semester pertama. (Numerikal)                               | Nilai numerikal                                                                                        |
| Curricular_units_1st_sem_enrolled           | Jumlah mata kuliah yang diambil pada semester pertama. (Numerikal)                              | Nilai numerikal                                                                                        |
| Curricular_units_1st_sem_evaluations        | Jumlah mata kuliah yang dievaluasi pada semester pertama. (Numerikal)                           | Nilai numerikal                                                                                        |
| Curricular_units_1st_sem_approved           | Jumlah mata kuliah yang disetujui pada semester pertama. (Numerikal)                            | Nilai numerikal                                                                                        |

Dengan tabel di atas, setiap fitur dataset dijelaskan secara rinci, termasuk keterangan nilai kategorikal untuk mempermudah pemahaman.

## Business Dashboard
Jelaskan tentang business dashboard yang telah dibuat. Jika ada, sertakan juga link untuk mengakses dashboard tersebut.

## Menjalankan Sistem Machine Learning
Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.

```

```

## Conclusion
Jelaskan konklusi dari proyek yang dikerjakan.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- action item 1
- action item 2
