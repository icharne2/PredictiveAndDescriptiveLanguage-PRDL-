import pandas as pd
import seaborn as sns

# Read the Excel file
df = pd.read_excel('DATA/Copilot_OSA_DB_UPM.xlsx')

# Calculate BMI and add it as a new column
df['BMI'] = df['Weight'] / (df['Height'] / 100) ** 2

# Display the first few rows of the dataframe to verify
print(df.head())

# Perform EDA
import matplotlib.pyplot as plt

# Pairplot to see the relationships
sns.pairplot(df.drop(columns=['Patient']), diag_kind='kde')
plt.show()

# Correlation matrix
corr_matrix = df.drop(columns=['Patient']).corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.show()

# Distribution of IAH
sns.histplot(df['IAH'], kde=True)
plt.show()

# Boxplots to see the distribution of features with respect to IAH
features = df.columns.drop(['Patient', 'IAH'])
for feature in features:
    sns.boxplot(x='IAH', y=feature, data=df)
    plt.show()