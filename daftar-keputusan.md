# Daftar Keputusan (Decision List) - Tarif Parkir Mall

Program: `parkir.py` | Kriteria: Decision Coverage

## Aturan Program

1. Jenis kendaraan: `motor`, `mobil`. Selain itu -> `ValueError`
2. Durasi parkir (jam) harus lebih dari 0
3. Tarif jam pertama: motor 2.000 | mobil 5.000
4. Jam ke-2 dst per jam: motor 1.000 | mobil 3.000
5. Batas maksimum harian: motor 10.000 | mobil 25.000
6. Akhir pekan (sabtu/minggu) tambahan flat 2.000
7. Member dapat potongan 20% dari total, maksimum potongan 3.000
8. Total bayar = (tarif dasar + tambahan akhir pekan) - potongan member

## Daftar Keputusan

| ID | Baris | Fungsi | Keputusan |
|----|-------|--------|-----------|
| D1 | 30 | `hitung_tarif_dasar` | `jenis_kendaraan not in TARIF` |
| D2 | 32 | `hitung_tarif_dasar` | `jam <= 0` |
| D3 | 38 | `hitung_tarif_dasar` | `total > batas_maksimum` |
| D4 | 45 | `biaya_akhir_pekan` | `hari.lower() in HARI_AKHIR_PEKAN` |
| D5 | 52 | `potongan_member` | `not is_member` |
| D6 | 56 | `potongan_member` | `potongan > MAKS_POTONGAN_MEMBER` |

## Ringkasan

- **6 keputusan** (D1, D2 di fungsi tarif; D3 di fungsi tarif; D4 di fungsi akhir
  pekan; D5, D6 di fungsi potongan)
- 6 keputusan x 2 hasil (True dan False) = **12 cabang** yang harus tercakup
- Test case: **11**
- Semua 6 keputusan punya kedua sisi yang feasible, jadi 100% bisa dicapai

Fungsi `hitung_total_bayar` **tidak punya keputusan** karena isinya hanya
memanggil tiga fungsi lain dan mengurangkan hasilnya. Fungsi itu tetap diuji
(TC11) untuk memastikan integrasinya benar, bukan untuk menutup cabang.

File terkait:

- `test-case.md` - daftar test case (format Myers)
- `matriks-decision-coverage.md` - peta keputusan ke test case
