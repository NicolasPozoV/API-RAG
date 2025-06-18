import re

def validar_nombre(nombre):
    return len(nombre) >= 2

def validar_telefono(telefono):
    return telefono.isdigit() and 8 <= len(telefono) <= 15

def validar_correo(correo):
    return re.match(r"[^@]+@[^@]+\.[^@]+", correo)
