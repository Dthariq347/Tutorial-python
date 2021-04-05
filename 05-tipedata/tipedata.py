#  a = 10, a adalah cariabel dengan nilai 10

# tipe data: Angka satuan yang gaada koma nya (intenger)
data_int =1 
print("nilai data :", data_int)
print("-bertipe :", type(data_int))

# tipe data: angka dengan koma (float)
data_float =1.5
print("nilai data :", data_float)
print("-bertipe :", type(data_float))

# tipe data: kumpulan dari beberapa karakter (sting)
data_string = "bertus"
print("nilai data :", data_string)
print("-bertipe :", type(data_string))

# tipe data: biner True/False (boolean)
data_bool = True
print("nilai data :", data_bool)
print("-bertipe :", type(data_bool))

##tipe data khusus

# bilanagan kompleks 
data_complex = complex(5,6)
print("nilai data :", data_complex)
print("-bertipe :", type(data_complex))

# tipe data dari bahasa c 

from ctypes import c_double #banyak lagi yang bisa digunakan dari bahasa c

data_c_double = c_double(10.5)
print("nilai data :", data_c_double)
print("-bertipe :", type(data_c_double))