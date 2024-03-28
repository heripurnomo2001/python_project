# Input nama teman, urutkan dan cetak

# Siapkan data type 'list'
daftar_teman = []

# Form input
nama=''
while nama not in ['selesai']:
    nama = str(input("Masukkan nama teman : "))
    if nama != 'selesai':
        daftar_teman.append(nama)

daftar_teman.sort()  #urut ascendeing
print("Urut dari a-z :" , daftar_teman)

daftar_teman.sort(reverse=True)  #urut descending
print("Urut dari z-a :" , daftar_teman)

daftar_teman.sort()  #urut ascendeing
print("Urut dari a-z dengan menggabungkan isi list daftar_teman :" , ', ' .join(daftar_teman))














