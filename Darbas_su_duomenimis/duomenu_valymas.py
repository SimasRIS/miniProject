# Importuojame biblioteka
import pandas as pd

# Ikeliame CSV faila
df = pd.read_csv('C:/Users/simas/PycharmProjects/miniProject/Duomenys/Isvalyti_failai/knygos.csv')

# Pasaliname pasikartojancius knygu pavadinimus
df_isvalytas = df.drop_duplicates(subset=['Knygos pavadinimas'])

# Issaugome isvalyta CSV faila
df_isvalytas.to_csv('C:/Users/simas/PycharmProjects/miniProject/Duomenys/Isvalyti_failai/knygos_cleaned.csv', index=False, encoding='utf-8')

print("Isvalytas CSV failas!")