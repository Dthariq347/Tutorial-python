# latihan komparasi dan logika

# membuat gabuangan area rentang dari angka

inputUser = float(input("masukan angka yang bernilai kurang dari 3 atau lebih dari 10 \n ="))

# +++++++3--------------
#memeriksa angka kurang dari 3 

isKurangDari = (inputUser < 3)
print ("nilai kurang dari 3 = ", isKurangDari)

# ----------3++++++++++++
# memeriksa angka lebih dari 10 

isLebihDari = (inputUser > 10)
print("nilai lebih dari 10 =", isLebihDari)

# +++++++++3----------10++++++++

ishasil = isKurangDari or isLebihDari
print("angka yang anda masukan :", ishasil)

# ----------3+++++++++10---------
# operasi irisan

print("\n",10*"-","\n")

inputUser = float(input("masukan angka lebih dari 3 dan kurang dari 10 \n ="))

#-------3+++++++++++
# lebih dari 3

isLebihDari = inputUser > 3
print("lebih dari 3 =", isLebihDari)

# ++++++++10---------
# kurang dari 10 

isKurangDari = inputUser < 10
print("kurang dari 10 =", isKurangDari)

# ----------3+++++++++10---------

ishasil = isLebihDari and isKurangDari
print("angka yang dimasukan anda :", ishasil)
