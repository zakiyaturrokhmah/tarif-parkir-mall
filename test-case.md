# Test Case - Tarif Parkir Mall

Format Myers: **Test case | Input | Expected output**

Program: `parkir.py` | Kriteria: Decision Coverage | Total: **11 test case**

Pemetaan tiap test case ke keputusan yang ditutupnya ada di
`matriks-decision-coverage.md`.

## Fungsi 1: `hitung_tarif_dasar(jenis_kendaraan, jam)`

| Test case | Input | Expected output | Keputusan dicakup |
|-----------|-------|-----------------|-------------------|
| TC01 | `("motor", 1)` | `2000` | D1 F, D2 F, D3 F |
| TC02 | `("motor", 9)` | `10000` | D3 False (boundary tepat di batas) |
| TC03 | `("mobil", 8)` | `25000` | D3 True (kena batas maksimum) |
| TC04 | `("sepeda", 2)` | `ValueError` | D1 True |
| TC05 | `("motor", 0)` | `ValueError` | D2 True |

## Fungsi 2: `biaya_akhir_pekan(hari)`

| Test case | Input | Expected output | Keputusan dicakup |
|-----------|-------|-----------------|-------------------|
| TC06 | `"sabtu"` | `2000` | D4 True |
| TC07 | `"senin"` | `0` | D4 False |

## Fungsi 3: `potongan_member(total, is_member)`

| Test case | Input | Expected output | Keputusan dicakup |
|-----------|-------|-----------------|-------------------|
| TC08 | `(2000, False)` | `0` | D5 True |
| TC09 | `(2000, True)` | `400` | D5 False, D6 False |
| TC10 | `(27000, True)` | `3000` | D6 True (kena batas potongan) |

## Fungsi 4: `hitung_total_bayar(jenis_kendaraan, jam, hari, is_member)`

| Test case | Input | Expected output | Keputusan dicakup |
|-----------|-------|-----------------|-------------------|
| TC11 | `("mobil", 8, "sabtu", True)` | `24000` | D3 True, D4 True, D5 False, D6 True |

## Alasan tiap expected output

| TC | Alasan |
|----|--------|
| TC01 | Jam pertama = tarif dasar, belum ada tambahan jam. 2.000 + 0 x 1.000 = 2.000. |
| TC02 | **Boundary value.** 2.000 + 8 x 1.000 = 10.000, TEPAT sama dengan batas harian. Kode memakai `>` bukan `>=`, jadi tidak dipotong. Kalau ditulis `>=`, sisi True D3 jadi mustahil dicapai lewat motor. |
| TC03 | 5.000 + 7 x 3.000 = 26.000 > 25.000 -> dipotong jadi 25.000. |
| TC04 | Jenis tidak dikenal harus ditolak, bukan diam-diam dihitung nol. Satu-satunya cara membuat D1 True. |
| TC05 | Durasi 0 tidak masuk akal - negative testing. Satu-satunya cara membuat D2 True. |
| TC06 | Sabtu termasuk himpunan akhir pekan -> tambahan flat 2.000. |
| TC07 | Senin bukan akhir pekan -> 0. Sisi False D4. |
| TC08 | Non-member langsung `return 0` tanpa menghitung 20%. Satu-satunya cara membuat D5 True. |
| TC09 | 2.000 x 20% = 400, masih di bawah batas 3.000. |
| TC10 | 27.000 x 20% = 5.400 > 3.000 -> dipotong jadi 3.000. Nilai 27.000 diambil dari total maksimum yang mungkin (25.000 batas mobil + 2.000 akhir pekan). |
| TC11 | 25.000 (kena batas harian) + 2.000 (akhir pekan) = 27.000; 27.000 x 20% = 5.400 -> dibatasi 3.000; 27.000 - 3.000 = 24.000. Satu pemanggilan menutup D3 True, D4 True, D5 False, D6 True sekaligus - sekalian menguji integrasi keempat fungsi. |
