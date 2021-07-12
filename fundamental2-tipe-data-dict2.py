"""
Tipe data dictionary sekedar menghubungkan antara Key dan Valur
KVP = Key Value Pair
dictionary = kamus
"""

# Cara pertama
kamus_ind_eng = {}
kamus_ind_eng['satu'] = 'one'
kamus_ind_eng['dua'] = 'two'
kamus_ind_eng['tiga'] = 'three'
kamus_ind_eng['empat'] = 'four'

# cara kedua
kamus_ind_eng = {'satu': 'one', 'dua': 'two', 'tiga': 'three', 'empat': 'four'}

print(kamus_ind_eng)
print(kamus_ind_eng['tiga'])

print('\nData ini dikirimkan oleh server Gojek, untuk memberikan info driver di sekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal': '2020-06-10',
    'driver_list': [
        {
            'nama': 'sandi',
            'jarak': 10
        },
        {
            'nama': 'riki',
            'jarak': 30
        },
        {
            'nama': 'fahmy',
            'jarak': 100
        }
    ]
}

print(data_dari_server_gojek)
print(f"\nDriver disekitar sini {data_dari_server_gojek['driver_list']}")
print(f"\nDriver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"Driver #1 {data_dari_server_gojek['driver_list'][2]}")

# Mengubah sekedar kata-kata menjadi dictionary
print(f"\nDriver terdekat berjarak {data_dari_server_gojek['driver_list'][0]['jarak']} meter")