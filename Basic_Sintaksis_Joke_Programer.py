"""
Semua sintacsis dasar bahasa pemrogman terdiri dari:
1. Skuensial : Langkah berurutan
2. Percobaan : Langkah melompat jika kondisi terpenuhi
3. Perulangan : Mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""

# Sekuensial
print('ibu berkata "Tolong ke warung belikan satu botol susu dan jika ada telur,beli 6 butir telur"')
print('Budi menjawab"Siap,Bu"')
print("Budi menuju ke warung")
print('"Permisi, apakah ada susu?"')
print("susu ada. Budi menghitung uang, cukup")
print('"ada telur? sekalian kalo ada bu, 6 butir."')
print("ada.")
print("Budi pun membeli satu botol susu dan 6 butir telur, kemudian Ia pulang.")
print("Budi pun pulang menyampaikan hasilnya kepada Ibunya.")

#Percabangan
jumlah_botol_susu = 75
jumlah_telur = 150
print(f"Jumlah botol susu {jumlah_botol_susu} botol")
print(f"jumlah telur {jumlah_telur} butir")

if jumlah_botol_susu > 0:
    print("budi menghitung uang dan ternyata cukup")
    print("budi membeli satu botol susu")
else:
    print("Budi tidak jadi membeli satu botol susu")

print("Budi pulang ke rumah")
print("Meyapaikan hasinya kepada Ibu.")
