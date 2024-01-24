import random
import string

rakamlar = string.digits
buyuk_harfler = string.ascii_uppercase
kucuk_harfler = string.ascii_lowercase
semboller = string.punctuation
tum_karakterler = [rakamlar,buyuk_harfler,kucuk_harfler,semboller]

sifre = ""

for j in range (4):
    for i in range (2):
        sifre += tum_karakterler[j][random.randint(0,9)]

sifre = list(sifre)
random.shuffle(sifre)

yeni_sifre = ""
sifre = yeni_sifre.join(sifre)

print(sifre)
