import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

longitud_contraseña = int(input("Introduce la longitud de la contraseña: "))

contraseña = ""

for i in range(longitud_contraseña):
    contraseña += random.choice(caracteres)

print("Contraseña generada:", contraseña)
