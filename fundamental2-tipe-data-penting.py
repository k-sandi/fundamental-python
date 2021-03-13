# Tipe data skalar => tipe data sederhana
anak1 = 'Eko'
anak2 = 'Dwi'
anak3 = 'Tri'
anak4 = 'catur'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

print('\ntipe data list/daftar/array')
anak = ['Eko', 'Dwi', 'Tri', 'Catur']
print(anak)
anak.append('Limo')
print(anak)

print('\nanak ke-2')
print(f'Hai {anak[1]}!')

print('\nsapa semua anak')
for a in anak:
    print((f'Hai {a}!'))

print('\nsapa semua anak: cara ribet')
for a in range(0, len(anak)):
    print(f'{a+1}. Hai {anak[a]}!')