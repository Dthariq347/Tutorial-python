# tugas konversi suhu
print("\n....FAHRENHEIT KE KELVIN....\n")

fahrenheit = float(input("masukan nilai fahrenheit :"))
print("suhu adalah", fahrenheit, "fahrenheit")

kelvin = (5/9) * (fahrenheit-32) + 273
print("suhu dalam kelvin adalah", kelvin, "kelvin")

print("\n....KELVIN KE FAHRENHEIT....\n")

kelvin = float(input("masukan nilai kelvin :"))
print("suhu adalah", kelvin, "kelvin")

fahrenheit = ((9/5) * (kelvin-273) +  2)
print("suhu adalah", fahrenheit, "kelvin")


