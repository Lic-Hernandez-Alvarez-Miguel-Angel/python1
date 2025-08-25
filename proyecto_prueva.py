import pandas as pd
import random
from datetime import datetime, timedelta

# Configuración
productos = ['Producto A', 'Producto B', 'Producto C', 'Producto D']
categorias = ['Categoría 1', 'Categoría 2']
num_datos = 100
fecha_inicial = datetime(2022, 1, 1)

# Lista para almacenar los datos
datos = []

for i in range(num_datos):
    fecha = fecha_inicial + timedelta(days=i)
    producto = random.choice(productos)
    categoria = random.choice(categorias)
    precio = round(random.uniform(5, 100), 2)
    cantidad = random.randint(1, 10)
    total = round(precio * cantidad, 2)

    datos.append([fecha.strftime("%Y-%m-%d"), producto, categoria, precio, cantidad, total])

# Crear DataFrame
df = pd.DataFrame(datos, columns=['fecha', 'producto', 'categoria', 'precio', 'cantidad', 'total'])

# Guardar como CSV
df.to_csv('ventas_historicas.csv', index=False)

print("✅ Archivo 'ventas_historicas.csv' creado con 100 registros.")
