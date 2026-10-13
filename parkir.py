"""Tarif Parkir Mall - mini program untuk Tugas Pertemuan 4 (versi ringkas).

Aturan program
--------------
1. Jenis kendaraan: "motor", "mobil". Selain itu            -> ValueError
2. Durasi parkir (jam) harus lebih dari 0
3. Tarif jam pertama     : motor 2.000 | mobil 5.000
4. Jam ke-2 dan seterusnya: motor 1.000 | mobil 3.000 per jam
5. Batas maksimum harian : motor 10.000 | mobil 25.000
6. Akhir pekan (sabtu/minggu) tambahan flat 2.000
7. Member dapat potongan 20% dari total, maksimum potongan 3.000
8. Total bayar = (tarif dasar + tambahan akhir pekan) - potongan member

Semua logika ada di fungsi murni (input -> output angka), tanpa input()/print(),
jadi tidak perlu mocking saat diuji.
"""
TARIF = {
    # jenis: (tarif jam pertama, tarif per jam berikutnya, batas maksimum harian)
    "motor": (2000, 1000, 10000),
    "mobil": (5000, 3000, 25000),
}
HARI_AKHIR_PEKAN = {"sabtu", "minggu"}
TAMBAHAN_AKHIR_PEKAN = 2000
PERSEN_MEMBER = 0.20
MAKS_POTONGAN_MEMBER = 3000


def hitung_tarif_dasar(jenis_kendaraan, jam):
    """Tarif dasar sebelum tambahan dan potongan member."""
    if jenis_kendaraan not in TARIF:                    # D1
        raise ValueError("Jenis kendaraan tidak dikenal")
    if jam <= 0:                                        # D2
        raise ValueError("Durasi parkir harus lebih dari 0 jam")

    tarif_pertama, tarif_per_jam, batas_maksimum = TARIF[jenis_kendaraan]
    total = tarif_pertama + (jam - 1) * tarif_per_jam

    if total > batas_maksimum:                          # D3
        return batas_maksimum
    return total


def biaya_akhir_pekan(hari):
    """Tambahan flat kalau parkir di hari sabtu atau minggu."""
    if hari.lower() in HARI_AKHIR_PEKAN:                # D4
        return TAMBAHAN_AKHIR_PEKAN
    return 0


def potongan_member(total, is_member):
    """Potongan 20% untuk member, dibatasi 3.000."""
    if not is_member:                                   # D5
        return 0

    potongan = total * PERSEN_MEMBER
    if potongan > MAKS_POTONGAN_MEMBER:                 # D6
        return MAKS_POTONGAN_MEMBER
    return potongan


def hitung_total_bayar(jenis_kendaraan, jam, hari="senin", is_member=False):
    """Total bayar = tarif dasar + tambahan akhir pekan - potongan member."""
    total = hitung_tarif_dasar(jenis_kendaraan, jam) + biaya_akhir_pekan(hari)
    return total - potongan_member(total, is_member)
