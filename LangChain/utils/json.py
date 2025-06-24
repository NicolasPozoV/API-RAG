import re

def extraer_json_del_texto(texto):
    patron = r"```json\s*(\{.*?\})\s*```"
    match = re.search(patron, texto, re.DOTALL)
    return match.group(1) if match else None