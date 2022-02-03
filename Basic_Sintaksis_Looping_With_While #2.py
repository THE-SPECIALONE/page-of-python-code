"""
Progam perulangan membaca buku dengan While
"""
buku = 10
print('Perintah Ibu,"baca semua bukumu"')
jumlah_baca = 0

buku_yang_sudah_dibaca_dan_dipahami = 0
print(f'Jumlah buku yang sudah dibaca dan dipahami {buku_yang_sudah_dibaca_dan_dipahami}')

while jumlah_baca < buku * 2:
    jumlah_baca = jumlah_baca + 1
    if buku_yang_sudah_dibaca_dan_dipahami == 9:
        print(f"buku ke {buku_yang_sudah_dibaca_dan_dipahami + 1} belum paham")
    else:
        buku_yang_sudah_dibaca_dan_dipahami = buku_yang_sudah_dibaca_dan_dipahami + 1
        print(f"buku ke {buku_yang_sudah_dibaca_dan_dipahami} sudah dibaca dan dipahami")
    print(f'jumlah buku yang sudah dibaca dan dipahami {buku_yang_sudah_dibaca_dan_dipahami}')
    if buku_yang_sudah_dibaca_dan_dipahami == buku:
        print('"Bu, semua buku sudah dibaca dan dipahami"')
else:
    print(f'"Bu, tidak semua buku bisa dipahami. '
          f'Budi hanya bisa memahami {buku_yang_sudah_dibaca_dan_dipahami} buku"')