# -*- coding: UTF-8
# SI VAS A COPIAR, DAME CREDITOS >:l   BY L.C.A HACK
import requests
import pyfiglet
import os
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
os.system("clear")
baner= pyfiglet.figlet_format("DoxPhone")
print(GREEN+baner)
print(YELLOW+"\nAutor: L.C.A HACK")
print("YouTube: L.C.A HACK")
print("Contactame: https://t.me/LCAHACK576\n\n")
print(GREEN+"escribe el numero de telefono junto\ncon el prefijo, ejemplo: +523313002435\n")
# Información

api_key = '4de874f562aa82abbf9a43d8b8c9b1c3'
number = int(input(GREEN+"Numero de telefono: "+RESET))

data = requests.get("http://apilayer.net/api/validate?access_key=%s&number=%s&country_code&format=1" % (api_key, number))

for key, value in data.json().items():

    print("%s: %s" % (key, value))

