# operasi logika atau boolean 

# not, or, and, xor

# not 
print('====NOT====') 
a = False
c = not a
print('nilai dari =', a)
print('---------- NOT')
print('data c =',c)

# OR (jika salah satu nya adalah True, maka hasilnya akan True)
print('====OR ====') 
a = False
b = False
c = a or b 
print(a,'OR',b,'=',c)
a = False
b = True
c = a or b 
print(a,'OR',b,'=',c)
a = True
b = False
c = a or b 
print(a,'OR',b,'=',c)
a = True
b = True
c = a or b 
print(a,'OR',b,'=',c)

# and (jika salah satunya False, maka hasilnya akan false)
print('====and====') 
a = False
b = False
c = a and b 
print(a,'and',b,'=',c)
a = False
b = True
c = a and b 
print(a,'and',b,'=',c)
a = True
b = False
c = a and b 
print(a,'and',b,'=',c)
a = True
b = True
c = a and b 
print(a,'and',b,'=',c)

# XOR (akan True jika salah satunya True, sisanya adalah False)
print('====XOR====') 
a = False
b = False
c = a ^ b 
print(a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b 
print(a,'XOR',b,'=',c)
a = True
b = False
c = a ^ b 
print(a,'XOR',b,'=',c)
a = True
b = True
c = a ^ b 
print(a,'XOR',b,'=',c)
