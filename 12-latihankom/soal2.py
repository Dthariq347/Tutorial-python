# pr komparasi dan logika

# 2.) +++++++0--------5++++++++8--------11++++++++++

# 2.)
inputUser = float(input("masukan angka \n ="))

# lebih dari 0 
isKurangDari0 = inputUser < 0
print("kurang dari 0 =", isKurangDari0)

# kurang dari 5 
isLebihDari5 = inputUser > 5
print("lebih dari 5 =", isLebihDari5)

# lebih dari 8
isKurangDari8 = inputUser < 8
print("kurang dari 8 =", isKurangDari8)

# kurang dari 11 
isLebihDari11 = inputUser > 11
print("lebih dari 11 =", isLebihDari11)

ishasil = isKurangDari0 or (isLebihDari5 and isKurangDari8) or isLebihDari11
print("angka yang dimasukan anda :", ishasil)

