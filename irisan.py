# Menampilkan irisan dari dua buah set

validasi_input = set()
for i in range(0,1000):
    validasi_input.add(i)

print("Ini adalah program untuk menampilkan irisan dari dua set angka. Pisahkan dengan tanda ','")

set_pertama = set()
set_kedua = set()
while True:
    input_user1 = input("Masukkan set angka pertama Ketik 'selesai' jika sudah.: ")
    if input_user1.lower() == 'selesai':
        print("Selesai dah.")
        break
    else:
        try:
            set_pertama.update(set(map(int, input_user1.split(','))))                
            print(set_pertama)
            if set_pertama.issubset(validasi_input):
                print('Set angka pertama : ', set_pertama)
            else:
                print("Set yang anda masukkan tidak valid!")
        except ValueError:
            print("Input yang anda masukkan tidak valid! Harap masukkan angka yang sesuai.")        


while True:
    input_user2 = input("Masukkan set angka ke dua. Ketik 'selesai' jika sudah.: ")
    if input_user2.lower() == 'selesai':
        print("Selesai dah.")
        break
    else:
        try:
            set_kedua.update(set(map(int, input_user2.split(','))))
            print(set_kedua)
            if set_kedua.issubset(validasi_input):
                print('Set angka ke dua : ', set_kedua)
            else:
                print("Set yang anda masukkan tidak valid!")
        except ValueError:
            print("Input yang anda masukkan tidak valid! Harap masukkan angka yang sesuai.")        

hasil = set_pertama.intersection(set_kedua)
print("Element-element yang terdapa pada dua set di atas adalah : ", hasil)



