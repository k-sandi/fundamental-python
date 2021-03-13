"""
Tipe data dictionary sekedar menguhubungkan antara KEY dan VAVLUE
KVP = Key Value Pair
dictionary = kamus
"""

kamus_in_eng = {'anak': 'son', 'istri': 'wife', 'ibu': 'mother', 'ayah': 'father'}

print(kamus_in_eng)
print(kamus_in_eng['ayah'])
print(kamus_in_eng['ibu'])

print('Data ini dikirimkan oleh server gojek untuk memberikan info driver di sekitar user.')
data_dari_server_gojek = {
    'tanggal': '2021-03-13',
    'driver_list': [
        {
            'nama': 'Eko',
            'jarak': 10
        },
        {
            'nama': 'Dwi',
            'jarak': 20
        },
        {
            'nama': 'Tri',
            'jarak': 30
        },
        {
            'nama': 'Catur',
            'jarak': 40
        }
    ]
}

print(data_dari_server_gojek)
print(f"\nDriver di sekitar sini {data_dari_server_gojek['driver_list']}")
print(f"Driver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"Driver #4 {data_dari_server_gojek['driver_list'][3]}")
print(f"\nDriver terdekat berjarak {data_dari_server_gojek['driver_list'][0]['jarak']} meter")
