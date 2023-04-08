nombres = '''
'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista',
'CAROLINA', 'CESAR', 'David','Diego', 'Dolores',
'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 
'Gregorio', 'Ignacio', 'Jonathan','Joaquina', 
'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 
'Julieta', 'Luciana','LAUTARO', 'Leonel', 'Luisa', 
'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 
'Sabrina', 'Tomás', 'Ulises',
'Yanina'
'''

notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42,
           16, 3, 35, 67, 10, 57, 11, 69, 12, 77, 13, 86, 48,
           65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 85, 73, 37,
           42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]

notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11,
           58, 10, 13, 34, 96, 71, 86, 37, 64, 13, 8, 87, 14,
           14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
           95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]


# Inciso A

# Limpiar el string de nombres
for caracter in [' ', "'", '\n']:
    nombres = nombres.replace(caracter, '')

# Capitalizar nombres
lista_nombres = [nombre.capitalize() for nombre in nombres.split(',')]

# Crear diccionario de nombres relacionados con sus notas
dicc_alumnos = {
    alum[0]: [alum[1], alum[2]] 
    for alum in zip(lista_nombres, notas_1, notas_2)}


# Inciso B

# Calcular el promedio de notas de cada alumno
dicc_promedios = {}
for alum, notas in dicc_alumnos.items():
    dicc_promedios[alum] = sum(notas) / len(notas)


# Inciso C

# Calcular el promedio general del curso
prom_general = sum(dicc_promedios.values()) / len(dicc_promedios)


# Inciso D

# Obtener el promedio máximo y almacenar el nombre
nombre_prom_max = max(dicc_promedios, key=dicc_promedios.get)


# Inciso E

# Crear un diccionario con las menores notas
dicc_menores_notas = {alum[0]: min(alum[1]) for alum in dicc_alumnos.items()}

# Obtener el alumno con la nota más baja
nombre_nota_min = min(dicc_menores_notas, key=dicc_menores_notas.get)


# Imprimir resultados
print(f'B: El promedio de cada alumno es:')
for alum, prom in dicc_promedios.items():
    print('   ' + alum + ': ' + str(prom))

print(f'C: El promedio general del curso es de {prom_general}')

print(f'D: El alumno con el mayor promedio es {nombre_prom_max}')

print(f'E: El alumno con la menor nota es {nombre_nota_min}')
