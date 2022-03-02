# operasi komparasi 

# setiap hasil dari operasi komparasi adalah boolean 

# <,>,>=,<=,==,!=,is,is not

a = 5
b = 3 

# lebih besar dari >
print("------lebih besar dari (>)")
hasil = a > 3
print(a, '>', 3, '=', hasil)
hasil = b > 3
print(b, '>', 3, '=', hasil)
hasil = b > 5
print(b, '>', 5, '=', hasil)

# lebih besar dari >
print("------kurang dari (<)")
hasil = a < 3
print(a, '<', 3, '=', hasil)
hasil = b < 3
print(b, '<', 3, '=', hasil)
hasil = b < 5
print(b, '<', 5, '=', hasil)

# lebih dari sama dengan >
print("------lebih dari sama dengan (>=)")
hasil = a >= 3
print(a, '>=', 3, '=', hasil)
hasil = b >= 3
print(b, '>=', 3, '=', hasil)
hasil = b >= 5
print(b, '>=', 5, '=', hasil)

# kurang dari sama dengan >
print("------kurang dari sama dengan (<=)")
hasil = a <= 3
print(a, '<=', 3, '=', hasil)
hasil = b <= 3
print(b, '<=', 3, '=', hasil)
hasil = b <= 5
print(b, '<=', 5, '=', hasil)

# sama dengan >
print("------sama dengan (==)")
hasil = a == 3
print(a, '==', 3, '=', hasil)
hasil = b == 3
print(b, '==', 3, '=', hasil)
hasil = b == 5
print(b, '==', 5, '=', hasil)

# tidak sama dengan >
print("------tidak sama dengan (!=)")
hasil = a != 3
print(a, '!=', 3, '=', hasil)
hasil = b != 3
print(b, '!=', 3, '=', hasil)
hasil = b != 5
print(b, '!=', 5, '=', hasil)

# 'is' sebagai komparasi object identity
print("------object udentity (is)")
x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',x,',id = ',hex(id(y)))
hasil = x is y 
print('x is y', hasil)

# 'is not' sebagai komparasi object  identity
print("------object udentity (i not)")
x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',x,',id = ',hex(id(y)))
hasil = x is y 
print('x is y', hasil)