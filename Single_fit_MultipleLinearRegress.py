import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Wczytaj dane z pliku Excel
df = pd.read_excel('DATA/Copilot_OSA_DB_UPM.xlsx')

# Oblicz BMI i dodaj jako nową kolumnę
df['BMI'] = df['Weight'] / (df['Height'] / 100) ** 2

# Sprawdzenie unikalnych wartości w kolumnie Gender
#print("Unikalne wartości w kolumnie Gender:", df['Gender'].unique())

# Mapowanie kolumny Gender na wartości numeryczne
df['Gender'] = df['Gender'].map({'hombre': 1, 'mujer': 0})

# Usunięcie wierszy z wartościami NaN
df.dropna(inplace=True)

# Zdefiniowanie zmiennych niezależnych i zmiennej docelowej
X = df[['Gender', 'Age', 'BMI', 'Cervical']]
y = df['IAH']

# Podział danych na zbiór treningowy i testowy (80% trening, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Trening modelu regresji liniowej
model = LinearRegression()
model.fit(X_train, y_train)

# Predykcje
y_pred = model.predict(X_test)

# Ocena modelu
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
