# Importuojam bibliotekas
import pandas as pd
from sklearn.model_selection import train_test_split # Padalina duomenis i dvi dalis - mokymo ir testavimo
from sklearn.tree import DecisionTreeClassifier, plot_tree # Importuojame sprendimu medi ir plot tree funkcija kuri nupiesia sprendimu medi
from sklearn.metrics import accuracy_score # Tikrina kaip gerai modelis klasifikuoja duomenis?????
import matplotlib.pyplot as plt


# Pasirenkam data faila
df = pd.read_csv('C:/Users/simas/PycharmProjects/miniProject/Duomenys/Isvalyti_failai/knygos_cleaned.csv')

def sprendimo_medzio_funkcija():
    # Priskirsime kainas pagal kategorija
    def kainu_kategorija(kaina):
        if kaina <= 10:
            return 'Pigi'
        elif kaina <= 20:
            return 'Vidutinė'
        else:
            return 'Brangi'

    # Kuriame stulpeli su kainu kategorija
    df['Kainos kategorija'] = df['Kaina €'].apply(kainu_kategorija)

    # Pasirenkame modelius ir tiksla
    X = df[['Reitingas', 'Įvertinimų skaičius']] # Is sukurto naujo DataFrame pasirenka stulpelius/duomenis klasifikavimui
    y = df['Kainos kategorija'] # tikslas kuri bandysime atspeti?

    #  Nurodome kiek modeli apmokinsime ir kiek su juo testuosime
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) # X ir Y train tai skirsime 70% mokymui o testavimui 30%

    # Sukuriam ir apmokome modeli
    model = DecisionTreeClassifier(max_depth=3, random_state=42) # max_depth nustato medzio gyli, kad modelis nepersimokytu, random state padaro duomenis stabilius ir nekintamus
    model.fit(X_train, y_train) # Apdoroja ir apmoko modeli

    # Patikrina modelio tiksluma
    y_pred = model.predict(X_test)
    print(f'Tikslumas: {accuracy_score(y_test, y_pred)}') # Apskaiciuoja kiek % modelis buvo teisingi

    plt.figure(figsize=(12, 6))
    plot_tree(model, feature_names=X.columns, class_names=model.classes_, filled=True) # Featured_names pozymiu pavadinimai, tai bus y pigi vidutine brangi
    plt.title('Kainos kategorijos prognozavimas')
    plt.show()

def main():
    sprendimo_medzio_funkcija()

if __name__ == '__main__':
    main()


