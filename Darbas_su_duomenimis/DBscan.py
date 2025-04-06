# Importuojame bibliotekas
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

# Pasirenkam data faila
df = pd.read_csv('C:/Users/simas/PycharmProjects/miniProject/Duomenys/Isvalyti_failai/knygos_cleaned.csv')

# Apskaiciuoti vidutines reiksmes kiekvienam zanrui,naudoti DBSCAN, kad suskirtytume zanrus i grupes
def dbscan_funkcija():
    bendri_zanrai = df.groupby('Žanras').agg({ # Grupuoja duomenis pagal zanra
        'Kaina €' : 'mean',  # Apskaiciuoja vidutine kaina kiekvienam zanrui
        'Reitingas': 'mean' # Apskaiciuoja vidutini reitinga kiekvienam zanrui
    }).reset_index()

    X = bendri_zanrai[['Kaina €', 'Reitingas']] # Is sukurto naujo DataFrame pasirenka stulpelius/duomenis klasterizavimui

    # Nuormakizuoja duomenis
    X = StandardScaler().fit_transform(X)

    # Imame DBSCAN
    dbscan = DBSCAN(eps=0.5, min_samples=2) # eps - maksimalus atstumas, kad taskai butu laikomi gretimais, min_samples min skaicius klasterio centrui?
    bendri_zanrai['Cluster'] = dbscan.fit_predict(X)

    # Vizualizacija
    plt.figure(figsize = (12,6))
    plt.scatter(bendri_zanrai['Kaina €'], bendri_zanrai['Reitingas'], c=bendri_zanrai['Cluster'], # X asis, Y asis,
                 s=100) # s nustato tasku dydi
    for i, zanras in enumerate(bendri_zanrai['Žanras']): # Perziuri kiekvieno zanro pavadinima is bendru zanru df
        plt.annotate(zanras, (bendri_zanrai['Kaina €'].iloc[i], bendri_zanrai['Reitingas'].iloc[i]), # annotate prideda teksto etiketes, prie kiekvieno tasko
                     textcoords='offset points', xytext=(5,5), fontsize=8) # Tekstas bus siek tiek paslinktas nuo tasko
    plt.xlabel('Vidutinė Kaina €')
    plt.ylabel('Vidutinis Reitingas')
    plt.title('Vidutinės reikšmės kiekvienam žanrui')
    plt.show()

def main():
    dbscan_funkcija()

if __name__ == '__main__':
    main()








