#Nombre: Diana Carolina Díaz GarcÍa
#Grupo: 702
#Programa: Ingeniería de Sistemas
#Codigo fuente: Autoría propia
#Problema elegido: 5

# Definición de la matriz con 4 recursos y horas de Lunes a Viernes
# Formato: [Nombre, Lunes, Martes, Miércoles, Jueves, Viernes]
equipo_trabajo = [
    ["Thomas", 8, 8, 9, 8, 8],
    ["Andres", 10, 10, 10, 10, 10],
    ["Carolina", 7, 7, 7, 7, 7],
    ["Diana", 8, 9, 8, 9, 8]
]

def calcular_jornadas(matriz):
    print(f"{'Nombre':<10} | {'Total Horas':<12} | {'Clasificacion'}")
    print("-" * 40)
    
    for recurso in matriz:
        nombre = recurso[0]

        # Sumar las horas de los índices 1 al 5 (Lunes a Viernes)
        total_horas = sum(recurso[1:])
        
        # Lógica de negocio para clasificar
        if total_horas > 40:
            clasificacion = "Sobretiempo"
        else:
            clasificacion = "Horario Estandar"
            
        print(f"{nombre:<10} | {total_horas:<12} | {clasificacion}")

# Ejecución de la función
calcular_jornadas(equipo_trabajo)
