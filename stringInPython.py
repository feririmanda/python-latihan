#   STRING IN PYTHON
# --------------------------

text = "selamat pagi, feri rimanda";
print(text)

# STRING MULTIBARIS
# ---------------------------
multiLine = """Hello my name is feri, you can call me feri, today i will to try 
learn python, according to me python is good programming languange, simple, faster and beginner friendly
"""
print(multiLine)

# STRING ADALAH ARRAY
# ----------------------------
# Seperti banyak bahasa pemograman populer lainnya, string dalam python adalah array byte yang mewakili
# karakter unicode, tanda kurung siku dapat digunakan untuk mengakses element string
a = "hello world"
print(a[0]);
#output h

# LOOPING MELALUI STRING
# -------------------------
for x in 'feri rimanda':
    print(x)
#output
#f
#e
#r
#i

#r
#i
#m
#a  
#n
#d
#a

# STRING LENGTH
# --------------------------
# fungsi len() digunakan untuk menghitung panjang
name =  'feri rimanda'
print(len(name))
#output 12

# CEK STRING
# --------------------------------
# untuk memeriksa apakah ada frasa atau karakter tertentu dalam sebuah string, kita dapat menggunakan 
# kata kunci in
txtString = 'pasir ganting adalah sebuah desa di kecamatan air pura'
print('pasir' in txtString)
#output True

# gunakan if dalam pernyataan 
if 'pasir' in txtString:
    print("Ya, 'pasir' ada")
    
# sebaliknya, kita juga dapat menggunakan kata kunci not in, untuk mencari karakter
# yang tidak ada dalam sebuah string
if 'feri' not in txtString:
    print("'feri' tidak ada")

# SLICING STRING (memotong string)
# --------------------------------
# Kita dapat mengembalikan serangkaian karakter dengan sintaksis slicing
# dengan cara menentukan indeks awal dan indeks akhir, dipisahkan dengan titik dua, untuk mengembalikan
# bagian dari string, contoh
print(txtString[6:13])
# output 'ganting'

# slicing dari awal string, hingga posisi 13
print(txtString[:13])
#output 'pasir ganting'

# slicing sampai akhir, dapatkan karakter dari posisi 6, dengan mengabaikan indeks akhir
print(txtString[6:])
#output 'ganting adalah sebuah desa di kecamatan air pura'

# slicing dengan indeks negatif
# gunakan indeks negatif untuk mulai mengembalikan nilai dari akhir string
print(txtString[-13:-6])
#output 'atan ai'

# MODIFY STRING (memodifikasi string)
# --------------------------------

# ubah string jadi huruf kapital, upper()
print(txtString.upper())
# output 'PASIR GANTING ADALAH SEBUAH DESA DI KECAMATAN AIR PURA'

# ubah string jadi huruf kecil, lower()
print(txtString.lower())
# output 'pasir ganting adalah sebuah desa di kecamtan air pura

# remove whitespace (hapus spasi putih), stript()
txt_to_modif = 'Feri Rimanda  '
print(txt_to_modif.strip())
# output 'Feri Rimanda'

# ganti string, replace()
print(txt_to_modif.replace('Feri', 'Joko'))
# output 'Joko Rimanda'

# memisahkan string menjadi list, split()
txt_split = 'feri, rimanda'
print(txt_split.split(','))
# output ['feri', ' rimanda']

# String method referensi disini : https://www.w3schools.com/python/python_ref_string.asp

# menggabungkan dua string,kita dapat menggunakan operator +
txt1 = 'feri'
txt2 = 'rimanda'
print(txt1 + txt2)
# output 'feririmanda'

# memberikan spasi pada string yang digabung
print(txt1 + " " + txt2)
# output 'feri rimanda'



