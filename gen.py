#!/usr/bin/python3
import random
password = ""
for chars in range(65, 91):#A TO Z uppercase characters from ascii
    password += chr(chars)
for chars in range(97, 123):
    """a to z lowercase chars from ascii"""
    password += chr(chars)

symbols = ["!","@","#","$","%","^","&","*","_"]

password = random.sample(password, k=5)#samples chars

password += random.sample(symbols, k=3)#samples symbols

random.shuffle(password)#shuffles both chars and symbols

password = "".join(password)#joins symbols with chars to generate 8 char password

print(password)
