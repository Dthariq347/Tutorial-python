# casting
# merubah data dari sati data ke data yang lain
# tipe data = int, string, float, bool

## INTNGER
print("=====INTENGER=====")
data_int = 9
print("nilai data =", data_int, ", type =", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) #akan false jika nilai int = 0
print("nilai data =", data_float, ", type =", type(data_float))
print("nilai data =", data_str, ", type =", type(data_str))
print("nilai data =", data_bool, ", type =", type(data_bool))

## FLOAT
print("=====FLOAT=====")
data_float = 9.8
print("nilai data =", data_float, ", type =", type(data_float))

data_int = int(data_float) #akan di bulatkan kebawah
data_str = str(data_float)
data_bool = bool(data_float) #akan false jika nilai float = 0
print("nilai data =", data_int, ", type =", type(data_int))
print("nilai data =", data_str, ", type =", type(data_str))
print("nilai data =", data_bool, ", type =", type(data_bool))

## BOOLEAN
print("=====BOOLEAN=====")
data_bool = True
print("nilai data =", data_bool, ", type =", type(data_bool))

data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool) 
print("nilai data =", data_int, ", type =", type(data_int))
print("nilai data =", data_str, ", type =", type(data_str))
print("nilai data =", data_float, ", type =", type(data_float))

## STRING
print("=====STRING=====")
data_str = "10"
print("nilai data =", data_str, ", type =", type(data_str))

data_int = int(data_str)
data_bool = bool(data_str) #agar false stringnya harus kosong
data_float = float(data_str) 
print("nilai data =", data_int, ", type =", type(data_int))
print("nilai data =", data_bool, ", type =", type(data_bool))
print("nilai data =", data_float, ", type =", type(data_float))