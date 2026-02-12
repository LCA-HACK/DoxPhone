# -*- coding: utf-8 -*-
# DOXPHONE OFFLINE PRO
# BY L.C.A HACK

import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import pyfiglet
import os
import time
from datetime import datetime

# ====== COLORES ======
GREEN = '\033[32m'
YELLOW = '\033[33m'
CYAN = '\033[36m'
RED = '\033[31m'
MAGENTA = '\033[35m'
RESET = '\033[39m'

os.system("clear")

# ====== BANNER HACKER ======
banner = pyfiglet.figlet_format("DOXPHONE", font="slant")
print(MAGENTA + banner)
print(GREEN + ">> OFFLINE EDITION")
print(YELLOW + ">> BY L.C.A HACK")
print(CYAN + "----------------------------------------")
print(GREEN + "Ingresa el número con prefijo internacional")
print("Ejemplo: +523313002435\n")

numero = input(CYAN + "TARGET >> " + RESET)

# ====== ANIMACIÓN ======
print(YELLOW + "\n[+] Iniciando escaneo...")
time.sleep(1)
print("[+] Analizando estructura...")
time.sleep(1)
print("[+] Consultando base de datos local...")
time.sleep(1)

try:
    parsed = phonenumbers.parse(numero)

    valido = phonenumbers.is_valid_number(parsed)
    posible = phonenumbers.is_possible_number(parsed)
    pais = geocoder.description_for_number(parsed, "es")
    operador = carrier.name_for_number(parsed, "es")
    zona = ", ".join(timezone.time_zones_for_number(parsed))

    tipo_num = phonenumbers.number_type(parsed)

    resultado = f"""
========================================
        DOXPHONE OFFLINE REPORT
========================================
Numero ingresado: {numero}
Numero formateado: {phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}

Es valido: {valido}
Es posible: {posible}
Pais / Region: {pais}
Operador: {operador}
Zona horaria: {zona}
Tipo: {tipo_num}

Escaneo completado: {datetime.now()}
========================================
"""

    print(GREEN + "\n[+] ESCANEO COMPLETADO\n")
    print(resultado)

    # ====== GUARDAR RESULTADO ======
    if not os.path.exists("results"):
        os.makedirs("results")

    fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f"results/{numero}_{fecha}.txt".replace("+", "")

    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(resultado)

    print(CYAN + f"[+] Reporte guardado en: {nombre_archivo}")

except phonenumbers.NumberParseException:
    print(RED + "\n[-] Numero invalido o mal formateado.")