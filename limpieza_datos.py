import pandas as pd

# 1. Cargar los datos
df = pd.read_csv('ventas_historicas.csv')

# 2. Asegurar que la columna 'fecha' sea tipo datetime
df['fecha'] = pd.to_datetime(df['fecha'])

# 3. Verificar si hay valores nulos
print("Valores nulos por columna:\n", df.isnull().sum())

# 4. Crear columna 'mes' para agrupar ingresos por mes
df['mes'] = df['fecha'].dt.to_period('M')  # ejemplo: 2022-01

# 5. Agrupar por mes y sumar total de ingresos
ingresos_mensuales = df.groupby('mes')['total'].sum().reset_index()

# Convertir 'mes' a tipo datetime para usarlo en gráficos
ingresos_mensuales['mes'] = ingresos_mensuales['mes'].dt.to_timestamp()

# 6. Guardar archivo limpio para análisis y Power BI
ingresos_mensuales.to_csv('ingresos_mensuales.csv', index=False)

print("✅ Limpieza completada. Archivo 'ingresos_mensuales.csv' creado.")
print(ingresos_mensuales.head())
