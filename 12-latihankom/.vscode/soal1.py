# pr komparasi dan logika 

# 1.) -------0++++++++5--------8++++++++11----------

# Jawabannya 

# 1.)
inputUser = float(input("masukan angka \n ="))

# lebih dari 0 
isLebihDari0 = inputUser > 0
print("lebih dari 0 =", isLebihDari0)

# kurang dari 5 
isKurangDari5 = inputUser < 5
print("kurang dari 5 =", isKurangDari5)

ishasil1 = isLebihDari0 and isKurangDari5
print("angka yang dimasukan :", ishasil1)

# lebih dari 8
islebihdari8 =inputUser > 8
print("lebih dari 8 =", islebihdari8)

# kurang dari 11 
isKurangDari11 = inputUser < 11
print("kurang dari 11 =", isKurangDari11)


ishasil2 = islebihdari8 and isKurangDari11
print("angka yang dimasukan :", ishasil2)

# disatukannya

iscorrect = ishasil1 or ishasil2
print("angka yang di keluarkan :", iscorrect) 