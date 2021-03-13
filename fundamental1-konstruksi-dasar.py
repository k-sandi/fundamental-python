# KONSTRUKSI DASAR PYTHON
# SEQUENTIAL: Eksekusi Berurutan
print("Hello World!")
print("by Mazkur")
print("Tanggal 13 Maret 2021")
print("-" * 10)

# PERCABANGAN: Eksekusi terpilih
ingin_cepat = False

if ingin_cepat:
    print('jalan lurus aja ya!')
else:
    print('Jalan lain')


# PERULANGAN
jumlah_anak = 4

for index_anak in range(1, jumlah_anak + 1):  # jumlah perulangan = 4 - 1 = 3
    print(f'Halo anak #{index_anak}')
