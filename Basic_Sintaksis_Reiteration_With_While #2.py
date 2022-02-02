"""
Progam perulangan membaca buku dengan While
"""
jumlah_buku = 10
print('Perintah Ibu,"baca semua bukumu"')

jumlah_buku_yang_sudah_dibaca_dan_sudah_dipahami = 0
print(f'Jumlah buku yang sudah dibaca dan dipahami {jumlah_buku_yang_sudah_dibaca_dan_sudah_dipahami}')

while jumlah_buku_yang_sudah_dibaca_dan_sudah_dipahami < jumlah_buku:
    jumlah_buku_yang_sudah_dibaca_dan_sudah_dipahami = jumlah_buku_yang_sudah_dibaca_dan_sudah_dipahami + 1
    if jumlah_buku_yang_sudah_dibaca_dan_sudah_dipahami == 10:
        print(f"buku ke {jumlah_buku_yang_sudah_dibaca_dan_sudah_dipahami} belum paham")
    print(f"buku ke {jumlah_buku_yang_sudah_dibaca_dan_sudah_dipahami} sudah dibaca dan dipahami")

print(f'Jumlah buku yang sudah dibaca dan dipahami {jumlah_buku_yang_sudah_dibaca_dan_sudah_dipahami}')