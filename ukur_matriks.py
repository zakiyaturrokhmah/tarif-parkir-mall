"""Ukur per-test-case: keputusan (D) mana yang dieksekusi dan bernilai apa.

Cara: tiap test dijalankan satu-satu dengan sys.settrace, lalu diperiksa
"setelah baris keputusan X, eksekusi lompat ke baris berapa" -> itu yang
menentukan keputusannya True atau False. Hasilnya dipakai untuk mengisi
matriks D <-> TC di matriks-decision-coverage.md.

Jalankan: python ukur_matriks.py
"""
import io
import os
import sys
import unittest

BASE = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(BASE, "parkir.py")
TARGET = os.path.realpath(FILE)

# baris -> (ID, baris tujuan kalau True, baris tujuan kalau False)
DECISION = {
    30: ("D1", 31, 32),
    32: ("D2", 33, 35),
    38: ("D3", 39, 40),
    45: ("D4", 46, 47),
    52: ("D5", 53, 55),
    56: ("D6", 57, 58),
}
TEKS = {
    "D1": "jenis_kendaraan not in TARIF",
    "D2": "jam <= 0",
    "D3": "total > batas_maksimum",
    "D4": "hari.lower() in HARI_AKHIR_PEKAN",
    "D5": "not is_member",
    "D6": "potongan > MAKS_POTONGAN_MEMBER",
}


def lacak(fn):
    jejak = []

    def local_trace(frame, event, arg):
        if event == "line":
            jejak.append(frame.f_lineno)
        return local_trace

    def global_trace(frame, event, arg):
        if frame.f_code.co_filename and os.path.realpath(frame.f_code.co_filename) == TARGET:
            return local_trace
        return None

    sys.settrace(global_trace)
    try:
        fn()
    finally:
        sys.settrace(None)
    return jejak


def nilai_keputusan(jejak):
    kena = {}
    for i, baris in enumerate(jejak):
        if baris not in DECISION:
            continue
        did, ke_true, ke_false = DECISION[baris]
        berikut = jejak[i + 1] if i + 1 < len(jejak) else -1
        if berikut == ke_true:
            kena.setdefault(did, set()).add("T")
        elif berikut == ke_false:
            kena.setdefault(did, set()).add("F")
    return {d: "".join(sorted(v)) for d, v in kena.items()}


def iter_tes(suite):
    for t in suite:
        if isinstance(t, unittest.TestSuite):
            yield from iter_tes(t)
        else:
            yield t


hasil = {}
for tes in iter_tes(unittest.TestLoader().loadTestsFromName("test_parkir")):
    nama = tes.id().split(".")[-1]
    tc = nama.split("_")[1]
    r = unittest.TextTestRunner(stream=io.StringIO(), verbosity=0).run(
        unittest.TestSuite([tes]))
    if not r.wasSuccessful():
        raise SystemExit("TEST GAGAL: " + nama)
    hasil[tc] = nilai_keputusan(lacak(tes))

print("=" * 108)
print("PETA TEST -> KEPUTUSAN  (T = jadi True, F = jadi False)")
print("=" * 108)
for tc in sorted(hasil):
    isi = ", ".join(f"{d}({v})" for d, v in sorted(hasil[tc].items()))
    print(f"  {tc:<5} {isi or '-'}")

print()
print("=" * 108)
print("PETA KEPUTUSAN -> TEST")
print("=" * 108)
print(f"  {'ID':<4} {'Keputusan':<32} {'True oleh':<16} {'False oleh':<24} Status")
print("  " + "-" * 104)
ringkas = {}
for baris, (did, _, _) in sorted(DECISION.items()):
    ts = sorted(tc for tc, k in hasil.items() if "T" in k.get(did, ""))
    fs = sorted(tc for tc, k in hasil.items() if "F" in k.get(did, ""))
    st = "OK (kedua sisi)" if ts and fs else ("hanya True" if ts else ("hanya False" if fs else "NOL"))
    ringkas[did] = (ts, fs)
    print(f"  {did:<4} {TEKS[did]:<32} {(','.join(ts) or '-'):<16} {(','.join(fs) or '-'):<24} {st}")

ok = sum(1 for v in ringkas.values() if v[0] and v[1])
print(f"\n  Keputusan diperiksa : {len(DECISION)}")
print(f"  Kedua sisi tercakup : {ok}/{len(DECISION)}")
print(f"  Total cabang        : {len(DECISION)*2}")
