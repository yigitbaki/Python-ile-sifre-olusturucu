import random
import string

rakamlar = string.digits
buyuk_harfler = string.ascii_uppercase
kucuk_harfler = string.ascii_lowercase
semboller = string.punctuation

rakam, b_harf, k_harf,sembol = True, True, True, True

sifre = ""

if rakam:
    sifre += rakamlar
if b_harf:
    sifre += buyuk_harfler
if k_harf:
    sifre += kucuk_harfler
if sembol:
    sifre += semboller 

lenght = 12

sifre = "".join(random.sample(sifre, lenght))

print(sifre)



