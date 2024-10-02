# Escritura de Archivo de Texto
with open('my_notes.txt', 'w') as file:
    # Escribiendo notas personales en el archivo
    file.write("Nota 1: Recordar estudiar para el examen.\n")
    file.write("Nota 2: Comprar víveres.\n")
    file.write("Nota 3: Llamar a mamá.\n")

# Lectura de Archivo de Texto
with open('my_notes.txt', 'r') as file:
    # Leyendo el contenido línea por línea
    for line in file:
        print(line.strip())  # Mostrar cada línea en la consola

# El archivo se cierra automáticamente al salir del bloque 'with'
