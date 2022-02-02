"""
Progam perulangan membaca buku dengan For
"""
jumlah_buku = 8
print('Perintah Ibu, "Baca semua bukumu"')

jumlah_buku_yang_dibaca = 0
print(f'jumlah buku yang dibaca {jumlah_buku_yang_dibaca}')

print("dengan For")
for jumlah_buku_yang_dibaca in range(1, jumlah_buku+1):
    print(f"buku ke{jumlah_buku_yang_dibaca} sudah dibaca")

print(f'jumlah buku yang dibaca {jumlah_buku_yang_dibaca}')
