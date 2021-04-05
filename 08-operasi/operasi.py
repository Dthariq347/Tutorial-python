# operasi bilangan pada python

a = 10
b = 4

# operasi pertambahan + 
hasil = a + b 
print(a, '+', b, '=', hasil)

# operasi pengurangan -
hasil = a - b
print(a, '-', b, '=', hasil)

#operasi perkalian *
hasil = a * b
print(a, '*', b, '=', hasil)

# operasi pembagian /
hasil = a / b
print(a, '/', b, '=', hasil)

# operasi eksponen (pangkat) **
hasil = a ** b
print(a, '**', b, '=', hasil)

# operasi modulus %
hasil = a % b
print(a, '%', b, '=', hasil)

# operasi floor division
hasil = a // b
print(a, '//', b, '=', hasil)
 

# Prioritas operasi, operational precendence 

# contoh 1
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x, '**' ,y, '*' ,z, '+' ,x, '/' ,y, '-' ,y, '%' ,z, '//' ,x, '=', hasil)

# contoh 2
hasil = x + y * z 
print("hasil dari.... ",x, '+', y, '*', z, '=', hasil  )