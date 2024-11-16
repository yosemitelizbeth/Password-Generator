import random

print("Hello World!")

characters="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
passwordlength=int(input("Pon la longitud para tu contraseña: "))
password=""

for _ in range(passwordlength):
    password += random.choice(characters)

print("Tu contraseña es:", password)
