# Test Case Design - Tarif Parkir Mall

Kriteria: **Decision Coverage** (Myers, 2012).

Dokumen ini dipisah menjadi tiga berkas, mengikuti struktur
**Daftar Keputusan -> Test Case -> Matriks**:

| Berkas | Isi |
|--------|-----|
| [`daftar-keputusan.md`](daftar-keputusan.md) | Daftar 6 keputusan (D1-D6) pada program |
| [`test-case.md`](test-case.md) | Daftar 11 test case, format Myers (Test case, Input, Expected output) |
| [`matriks-decision-coverage.md`](matriks-decision-coverage.md) | Matriks keputusan ke test case + hasil tool coverage |

## Ringkasan

- Program: `parkir.py` (4 fungsi, logikanya fungsi murni tanpa `input()`/`print()`)
- Keputusan: **6**
- Cabang yang harus tercakup: **12** (6 keputusan x 2)
- Test case: **11** (minimal yang dibutuhkan: 7)
- Hasil: semua test lulus, **decision coverage 100%**

## Cara Menjalankan

    python -m unittest -v test_parkir
    python -m pip install coverage
    python -m coverage run --branch -m unittest test_parkir
    python -m coverage report -m --include=parkir.py

Hasil:

    Name        Stmts   Miss Branch BrPart  Cover   Missing
    -------------------------------------------------------
    parkir.py      29      0     12      0   100%
