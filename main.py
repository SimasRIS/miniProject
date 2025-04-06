# Importuojame bibliotekas, ir savo failus
from Darbas_su_duomenimis import visualizacija, KMeans, DBscan, decision_tree, duomenu_valymas, web_scrapinimas


def pagrindinis_meniu():
    print("\nPasirinkite veiksmą:")
    print("1. Duomenų nuskaitymas (web scraping)")
    print("2. Duomenų valymas")
    print("3. Visualizacijos")
    print("4. KMeans grupavimas")
    print("5. DBSCAN grupavimas")
    print("6. Sprendimo medžio klasifikacija")
    print("7. Išeiti")
    pasirinkimas = input("Įveskite pasirinkimo numerį (1-7)")
    return pasirinkimas

def puslapio_nuskaitymas():
    print("\nVykdomas web scraping...")
    web_scrapinimas.main()
    print("Puslapis nuskaitytas!")

def duomenu_valymas_funkcija():
    print("\nVykdomas duomenų valymas...")
    duomenu_valymas.main()
    print("Duomenys isvalyti!")

def vizualizacija_duomenu():
    print("\nVykdoma duomenu visualizacija...")
    visualizacija.main()
    print("Duomenu visualizacija pabaigta!")

def kmeans_grupavimas():
    print("\nVykdomas duomenu grupavimas su KMeans...")
    KMeans.main()
    print("Duomenu grupavimas baigtas!")

def dbscan_grupavimas():
    print("\nVykdomas duomenu grupavimas su DBSCAN...")
    DBscan.main()
    print("Duomenu grupavimas baigtas!")

def sprendimo_medis():
    print("\nVykdomas duomenu klasifikavimas su DecisionTreeClassifier...")
    decision_tree.main()
    print("Duomenu grupavimas baigtas!")

def main():
       while True:
        pasirinkimas = pagrindinis_meniu()
        if pasirinkimas == "1":
            puslapio_nuskaitymas()
        elif pasirinkimas == "2":
            duomenu_valymas_funkcija()
        elif pasirinkimas == "3":
            vizualizacija_duomenu()
        elif pasirinkimas == "4":
            kmeans_grupavimas()
        elif pasirinkimas == "5":
            dbscan_grupavimas()
        elif pasirinkimas == "6":
            sprendimo_medis()
        elif pasirinkimas == "7":
            print("Programa baigta. Iki kitų kartų!")
            break
        else:
            print("Neteisingas pasirinkimas. Bandykite dar kartą.")

if __name__ == '__main__':
    main()