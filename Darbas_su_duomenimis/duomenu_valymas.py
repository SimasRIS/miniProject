# Importuojame biblioteka
import pandas as pd

# Ikeliame CSV faila
df = pd.read_csv('C:/Users/simas/PycharmProjects/miniProject/Duomenys/Isvalyti_failai/knygos.csv')

# Pasaliname pasikartojancius knygu pavadinimus
df = df.drop_duplicates(subset=['Knygos pavadinimas'])

df['Kaina €'] = pd.to_numeric(df['Kaina €'], errors='coerce')
df['Reitingas'] = pd.to_numeric(df['Reitingas'], errors='coerce')
df['Įvertinimų skaičius'] = pd.to_numeric(df['Įvertinimų skaičius'], errors='coerce')
df = df.dropna(subset=['Kaina €', 'Reitingas', 'Įvertinimų skaičius'])

# Issaugome isvalyta CSV faila
df.to_csv('C:/Users/simas/PycharmProjects/miniProject/Duomenys/Isvalyti_failai/knygos_cleaned.csv', index=False, encoding='utf-8')

print("Isvalytas CSV failas!")