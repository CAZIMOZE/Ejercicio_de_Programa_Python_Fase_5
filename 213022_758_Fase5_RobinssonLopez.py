#Nombre del estudiante   :   Robinsson Jair López García
#Grupo                   :   (213022_758)
#Programa                :   Fundamentos de programación (Ingeniería en Sistemas)
#Código fuente           :   Autoría propia

# ==========================================
# 1. SE DEFINE LA FUNCION PARA CALCULAR LA CANTIDAD A PEDIR
# ==========================================
def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    """
    Esta Función aplica la lógica de negocio para determinar
    la cantidad exacta de unidades a solicitar.
    """
    if stock_actual < stock_minimo:
        cantidad_a_pedir = stock_minimo - stock_actual
    else:
        cantidad_a_pedir = 0
        
    return cantidad_a_pedir


# ==========================================
# 2. SE ESTABLECE LAESTRUCTURA DE DATOS (MATRIZ)
# ==========================================
inventario = [
    ["ART001", "Guitarra electrica", 7, 5],
    ["ART002", "Bajo electrico", 3, 10],
    ["ART003", "Bateria acustica", 2, 8],
    ["ART004", "Guitarra acustica", 15, 15],
    ["ART005", "Microfonos", 4, 10]
]


# ==========================================
# 3. MENSAJES EN PANTALLA (TITULOS)
# ==========================================
print("==================================================")
print("   REPORTE DE AUDITORÍA DE INVENTARIO Y PEDIDOS")
print("==================================================")
print("ARTÍCULO | CANTIDAD A PEDIR")
print("-" * 50)

# Recorremos la matriz fila por fila
for articulo in inventario:
    
    # --------------------------------------------------------
    # EXTRACCIÓN DE DATOS CON LOS ÍNDICES CORRESPONDIENTES
    # --------------------------------------------------------
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]
    
    # Se usa la funcion para calcular cuantas unidades se deben pedir
    unidades_a_pedir = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
    
    # Impresión de los resultados en pantalla
    if unidades_a_pedir > 0:
        print(f"{nombre} | unidades a pedir: {unidades_a_pedir}")
    else:
        print(f"{nombre} | Stock al día ")

print("==================================================")