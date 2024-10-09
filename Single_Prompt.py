import pandas as pd

# Read the Excel file
file_path = 'DATA/Info_BDApnea_QuironMalaga.xlsx'
df = pd.read_excel(file_path)

# Select the required columns
df = df[['Patient', 'Gender', 'Edad', 'Talla', 'Peso', 'IAH', 'PerCervical']]

# Rename the columns
df.rename(columns={
    'Edad': 'Age',
    'Talla': 'Height',
    'Peso': 'Weight',
    'PerCervical': 'Cervical'
}, inplace=True)

# Convert Weight column to float
df['Weight'] = pd.to_numeric(df['Weight'], errors='coerce')

# Remove rows with non-numerical values and rows with -1 or NaN
df = df.dropna()
df = df[(df != -1).all(axis=1)]

# Save the resulting data frame to a new Excel file
output_path = 'DATA/Copilot_OSA_DB_UPM.xlsx'
df.to_excel(output_path, index=False)