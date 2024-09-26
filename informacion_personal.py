# Crear un diccionario con información personal ficticia
informacion_personal = {
    "nombre": "Juan",
    "edad": 23,
    "ciudad": "Ambato, Ecuador",
    "profesion": "Ingeniero en Informática"
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Quito, Ecuador"  # Cambiamos a Quito

# Agregar una nueva clave-valor para el "telefono"
informacion_personal["telefono"] = "0987654321"  # Número de teléfono ficticio

# Verificar si la clave "telefono" existe, y si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"  # Este paso es redundante porque ya se agregó

# Eliminar la clave "edad" del diccionario
del informacion_personal["edad"]

# Imprimir el diccionario resultante
print(informacion_personal)

