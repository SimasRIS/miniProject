# Importuojame bibliotekas
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Pasirenkam data faila
df = pd.read_csv('C:/Users/simas/PycharmProjects/miniProject/Duomenys/Isvalyti_failai/knygos_cleaned.csv')

def kmeans_funkcija():
    # Ieskome kaip knygos skirstomos pagal kaina, reitinga ir ivertinimu skaiciu

    X = df[['Kaina €', 'Reitingas', 'Įvertinimų skaičius']] # Pasirenkam stulpelius/duomenis klasterizacijai

    # Duomenu normalizavimas
    scaler = StandardScaler() # Sukuria objekta, kuris skirtas normalizuoti duomenis
    X= scaler.fit_transform(X) # Apskaiciuoja vidurki ir standartini nuokripi kiekvienam pozymiui ir normalizuoja duomenis

    # Kuriame KMeans
    kmeans = KMeans(n_clusters=3, random_state=42) # Sukuriame KMeans objekta, nurodome klasteriu skaiciu "3", ???
    df['Cluster'] = kmeans.fit_predict(X) # Kiekvienam duomenu irasui priskiria klasterio numeri

    # Pradedam vizualizacija
    plt.figure(figsize = (12,6)) # Nusako diagramos dydi
    plt.scatter(df['Kaina €'], df['Reitingas'], c=df['Cluster'], cmap='viridis', alpha=0.6) # Imame X tada Y tada c/parametra, spalvas, apha permatomumas
    plt.xlabel('Kaina €')
    plt.ylabel('Reitingas')
    plt.title('Knygų skirstymas pagal kaina, reitinga ir įvertinimų skaičių')
    plt.show()

def main():
    kmeans_funkcija()

if __name__ == '__main__':
    main()