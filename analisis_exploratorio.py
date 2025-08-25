import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Estilo visual
sns.set(style="whitegrid")

# 1. Cargar los ingresos mensuales limpios
df = pd.read_csv('ingresos_mensuales.csv')

# 2. Convertir 'mes' a tipo fecha si no lo está
df['mes'] = pd.to_datetime(df['mes'])

# 3. Visualizar ingresos mes a mes
plt.figure(figsize=(12, 6))
sns.lineplot(x='mes', y='total', data=df, marker='o')
plt.title("📈 Ingresos Mensuales de la Microempresa", fontsize=14)
plt.xlabel("Mes")
plt.ylabel("Total de ingresos")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()

# 4. Estadísticas básicas
print("\n📊 Estadísticas de los ingresos mensuales:")
print(df['total'].describe())
