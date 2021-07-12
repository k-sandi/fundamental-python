# Tipe data skalar
anak1 = 'Eko'
anak2 = 'Dwi'
anak3 = 'Tri'
anak4 = 'Catur'

#print(anak1)
#print(anak1)
#print(anak1)
#print(anak1)

# Tipe data list/daftar/array
#anak = []
#anak.append('Eko')
#anak.append('Dwi')
#print(anak)

anak = ['One', 'Two', 'Three']
print(anak)
anak.append('Four')
print(anak)

print('\nsapa anak ke-2')
print(f'Hai {anak[1]}!')

print('\nSapa semua anak')
for a in anak:
    print(f'Hai {a}!')


print('\nSapa semua anak: cara ribet')
for a in range(0, len(anak)):
    print(f'{a+1}. Hai {anak[a]}')