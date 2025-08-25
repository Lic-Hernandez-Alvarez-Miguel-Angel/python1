import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# 1. Cargar los datos mensuales
df = pd.read_csv('ingresos_mensuales.csv')
df['mes'] = pd.to_datetime(df['mes'])

# 2. Crear una variable numérica de tiempo (meses consecutivos)
df['mes_num'] = range(len(df))  # 0, 1, 2, 3...

# 3. Variables para el modelo
X = df[['mes_num']]
y = df['total']

# 4. Crear y entrenar el modelo
modelo = LinearRegression()
modelo.fit(X, y)

# 5. Hacer predicciones sobre los datos existentes
df['predicciones'] = modelo.predict(X)

# 6. Evaluar el modelo
rmse = np.sqrt(mean_squared_error(y, df['predicciones']))
r2 = r2_score(y, df['predicciones'])

print("📊 Evaluación del modelo:")
print(f"  - RMSE: {rmse:.2f}")
print(f"  - R²: {r2:.2f}")

# 7. Predecir ingresos del próximo mes
mes_siguiente = [[len(df)]]
prediccion_futura = modelo.predict(mes_siguiente)[0]
print(f"🔮 Predicción de ingresos para el próximo mes: ${prediccion_futura:.2f}")

# 8. Guardar el modelo entrenado
joblib.dump(modelo, 'modelo_ingresos.pkl')
print("✅ Modelo guardado como 'modelo_ingresos.pkl'")

df_pred = pd.DataFrame({
    'mes': ['2025-01-01'],
    'total': [prediccion_futura]
})
df_pred.to_csv('prediccion_futura.csv', index=False)
