import re
import pyperclip

def split_text(text):
    # Utiliza re.split con el patrón \s+ para separar por cualquier tipo de espacio en blanco
    return re.split(r'\s+', text)

def copy_to_clipboard(text):
    # Une el texto con un espacio entre cada palabra y lo copia al portapapeles
    pyperclip.copy(' '.join(text))

# Ejemplo de uso
text = """Este es un texto de
prueba con varias  separaciones\tincluyendo
espacios, tabs, y saltos de línea."""
result = split_text(text)

# Copiar el resultado al portapapeles
copy_to_clipboard(result)

print("Texto procesado y copiado al portapapeles:", result)
