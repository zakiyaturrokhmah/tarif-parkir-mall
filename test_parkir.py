"""Unit test + Decision Coverage untuk Tarif Parkir Mall (versi ringkas).

Jalankan:
    python -m unittest -v test_parkir

Cek decision coverage:
    python -m coverage run --branch -m unittest test_parkir
    python -m coverage report -m --include=parkir.py

Nama tiap test memuat ID test case (TC) dan keputusan (D) yang ditutupnya.
"""
import unittest

from parkir import (
    hitung_tarif_dasar,
    biaya_akhir_pekan,
    potongan_member,
    hitung_total_bayar,
)


class TestHitungTarifDasar(unittest.TestCase):
    """D1 (jenis dikenal), D2 (jam > 0), D3 (kena batas maksimum)"""

    def test_TC01_jam_pertama_tarif_dasar(self):
        """D1 F, D2 F, D3 F"""
        self.assertEqual(hitung_tarif_dasar("motor", 1), 2000)

    def test_TC02_D3_false_boundary_tepat_di_batas(self):
        """Boundary value: 2000 + 8 x 1000 = 10000, TEPAT sama dengan batas.
        Kode memakai '>' bukan '>=', jadi tidak dipotong."""
        self.assertEqual(hitung_tarif_dasar("motor", 9), 10000)

    def test_TC03_D3_true_mobil_kena_batas_maksimum(self):
        """5000 + 7 x 3000 = 26000 > 25000 -> dipotong jadi 25000"""
        self.assertEqual(hitung_tarif_dasar("mobil", 8), 25000)

    def test_TC04_D1_true_jenis_kendaraan_tidak_dikenal(self):
        with self.assertRaises(ValueError):
            hitung_tarif_dasar("sepeda", 2)

    def test_TC05_D2_true_jam_nol(self):
        with self.assertRaises(ValueError):
            hitung_tarif_dasar("motor", 0)


class TestBiayaAkhirPekan(unittest.TestCase):
    """D4 (hari akhir pekan)"""

    def test_TC06_D4_true_sabtu(self):
        self.assertEqual(biaya_akhir_pekan("sabtu"), 2000)

    def test_TC07_D4_false_hari_kerja(self):
        self.assertEqual(biaya_akhir_pekan("senin"), 0)


class TestPotonganMember(unittest.TestCase):
    """D5 (member), D6 (batas potongan)"""

    def test_TC08_D5_true_bukan_member(self):
        self.assertEqual(potongan_member(2000, False), 0)

    def test_TC09_D5_false_D6_false_potongan_normal(self):
        """2000 x 20% = 400, masih di bawah batas 3000"""
        self.assertEqual(potongan_member(2000, True), 400)

    def test_TC10_D6_true_potongan_kena_batas(self):
        """27000 x 20% = 5400 > 3000 -> dipotong jadi 3000"""
        self.assertEqual(potongan_member(27000, True), 3000)


class TestHitungTotalBayar(unittest.TestCase):
    """Integrasi keempat fungsi"""

    def test_TC11_total_mobil_akhir_pekan_member(self):
        """25000 (kena batas harian) + 2000 (akhir pekan) - 3000 (kena batas potongan)"""
        self.assertEqual(hitung_total_bayar("mobil", 8, "sabtu", True), 24000)


if __name__ == "__main__":
    unittest.main(verbosity=2)
