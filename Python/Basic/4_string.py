print('Arief Ganteng'*5)
nama = 'Arief Rachman Hakim'
print(nama[0]) #pertama
print(nama[-1]) #last

# Built in Function
# split() : memisahkan dengan perantara separator
teks = 'halo, nama saya, arief'
var_split = teks.split(', ')
print(var_split)

# isLower() : mengecek huruf kecil
a = 'Halo'
b = 'halo'

print(a.islower())
print(b.islower())

# count() : menghitung berapa kali muncul
teks = "Halo semuanya, disini saya bersama dengan budi semuanya"
var_count = teks.count('semuanya')
print(var_count)