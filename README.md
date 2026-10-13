# Tarif Parkir Mall (Python)

Mini program untuk Tugas Pertemuan 4 - Analisis dan Pengujian Sistem (High Order
Testing): Unit Testing dan Test Case Design dengan kriteria **Decision Coverage**.

## Aturan Program

- Jenis kendaraan: `motor`, `mobil`. Selain itu -> `ValueError`
- Durasi parkir (jam) harus lebih dari 0
- Tarif jam pertama: motor 2.000 | mobil 5.000
- Jam ke-2 dst per jam: motor 1.000 | mobil 3.000
- Batas maksimum harian: motor 10.000 | mobil 25.000
- Akhir pekan (sabtu/minggu) tambahan flat 2.000
- Member dapat potongan 20% dari total, maksimum potongan 3.000
- Total bayar = (tarif dasar + tambahan akhir pekan) - potongan member

## Fungsi

| Fungsi | Isi | Keputusan |
|--------|-----|-----------|
| `hitung_tarif_dasar(jenis_kendaraan, jam)` | tarif dasar + batas maksimum harian | D1, D2, D3 |
| `biaya_akhir_pekan(hari)` | tambahan flat 2.000 untuk sabtu/minggu | D4 |
| `potongan_member(total, is_member)` | potongan 20% dibatasi 3.000 | D5, D6 |
| `hitung_total_bayar(jenis_kendaraan, jam, hari, is_member)` | gabungan ketiga fungsi di atas | - (integrasi) |

## Unit Test

    python -m unittest -v test_parkir

Hasil: 11 test, semua lulus.

## Cek Decision Coverage

    python -m pip install coverage
    python -m coverage run --branch -m unittest test_parkir
    python -m coverage report -m --include=parkir.py

Hasil:

    Name        Stmts   Miss Branch BrPart  Cover   Missing
    -------------------------------------------------------
    parkir.py      29      0     12      0   100%

6 keputusan x 2 hasil = 12 cabang, semuanya tercakup.

## Struktur

Test Case Design dipisah menjadi tiga berkas: **Daftar Keputusan -> Test Case -> Matriks**.

| Berkas | Isi |
|--------|-----|
| `parkir.py` | Program (4 fungsi, logikanya fungsi murni tanpa input/print) |
| `test_parkir.py` | 11 unit test (semua lulus) |
| `daftar-keputusan.md` | Daftar 6 keputusan (D1-D6) pada program |
| `test-case.md` | Daftar 11 test case, format Myers + alasan tiap expected output |
| `matriks-decision-coverage.md` | Matriks keputusan ke test case + hasil tool coverage |
| `test-case-design.md` | Ringkasan + penunjuk ke tiga berkas di atas |
| `ukur_matriks.py` | Alat bantu: mengukur per test case keputusan mana yang kena True/False |
| `Presentasi-Tugas-Pertemuan-4.pptx` | Slide presentasi |
| `bikin_ppt.py` | Script pembuat slide (kalau mau diedit lalu dibangun ulang) |

## Kenapa program ini gampang diuji

- Semua logika ada di fungsi murni: input angka/teks -> output angka, **tanpa**
  `input()` dan tanpa `print()`, jadi tidak perlu mocking sama sekali
- Hanya 6 keputusan dengan kondisi yang jelas, masing-masing punya kedua sisi
  yang feasible (tidak ada cabang mati)
- Batas-batasnya angka nyata, sehingga boundary value testing (TC02: tepat di
  batas 10.000) langsung kelihatan gunanya
- 11 test case cukup, dan minimalnya 7 - lihat `matriks-decision-coverage.md`
