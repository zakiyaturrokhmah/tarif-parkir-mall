# Matriks Decision Coverage - Tarif Parkir Mall

Program: `parkir.py` | Kriteria: Decision Coverage

Daftar keputusan: `daftar-keputusan.md` | Daftar test case: `test-case.md`

## Matriks Keputusan -> Test Case

Diukur otomatis per test case: tiap test dijalankan satu-satu dengan
`sys.settrace`, lalu dicatat cabang mana yang diambil (`python ukur_matriks.py`).

| Keputusan | True dicakup oleh | False dicakup oleh |
|-----------|-------------------|--------------------|
| D1 `jenis_kendaraan not in TARIF` | TC04 | TC01, TC02, TC03, TC05, TC11 |
| D2 `jam <= 0` | TC05 | TC01, TC02, TC03, TC11 |
| D3 `total > batas_maksimum` | TC03, TC11 | TC01, TC02 |
| D4 `hari.lower() in HARI_AKHIR_PEKAN` | TC06, TC11 | TC07 |
| D5 `not is_member` | TC08 | TC09, TC10, TC11 |
| D6 `potongan > MAKS_POTONGAN_MEMBER` | TC10, TC11 | TC09 |

**Semua 12 cabang (6 keputusan x 2) tercakup oleh 11 test case.**

## Peta balik: test case mana mengeksekusi keputusan apa

| Test case | Keputusan yang dieksekusi |
|-----------|---------------------------|
| TC01 | D1(F), D2(F), D3(F) |
| TC02 | D1(F), D2(F), D3(F) |
| TC03 | D1(F), D2(F), D3(T) |
| TC04 | D1(T) |
| TC05 | D1(F), D2(T) |
| TC06 | D4(T) |
| TC07 | D4(F) |
| TC08 | D5(T) |
| TC09 | D5(F), D6(F) |
| TC10 | D5(F), D6(T) |
| TC11 | D1(F), D2(F), D3(T), D4(T), D5(F), D6(T) |

## Hasil tool

```
$ python -m unittest test_parkir
Ran 11 tests in 0.001s

OK

$ python -m coverage run --branch -m unittest test_parkir
$ python -m coverage report -m --include=parkir.py
Name        Stmts   Miss Branch BrPart  Cover   Missing
-------------------------------------------------------
parkir.py      29      0     12      0   100%
```

- `Branch 12` = 6 keputusan x 2
- `BrPart 0` = tidak ada cabang yang setengah jalan
- `Missing` kosong = tidak ada baris/cabang yang terlewat

## Berapa test case minimalnya

Dari peta di atas, ada 12 cabang yang harus dicakup dan satu test case bisa
menutup beberapa cabang sekaligus. Himpunan test case paling kecil yang sudah
menutup semuanya adalah **7 test case**: TC01, TC04, TC05, TC07, TC08, TC09, TC11.

```
TC01 -> D1 F, D2 F, D3 F
TC04 -> D1 True
TC05 -> D2 True
TC07 -> D4 False
TC08 -> D5 True
TC09 -> D5 F, D6 F
TC11 -> D1 F, D2 F, D3 True, D4 True, D5 F, D6 True
        = 12 cabang, lengkap
```

Jadi 11 test case yang ditulis menyisakan **4 test case cadangan**: TC02, TC03,
TC06, TC10. Cadangan ini bukan pemborosan, masing-masing punya alasan:

- **TC02** menguji boundary value: 10.000 tepat sama dengan batas harian motor,
  jadi membuktikan kode memakai `>` dan bukan `>=`.
- **TC03** menguji cabang pemotongan langsung di `hitung_tarif_dasar`, tanpa
  lewat `hitung_total_bayar`.
- **TC06** menguji tambahan akhir pekan langsung, tanpa lewat integrasi.
- **TC10** menguji batas potongan member langsung, tanpa lewat integrasi.
