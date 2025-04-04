# Importai
import pandas as pd
import plotly.express as px

# Pasiimame duomenis
df = pd.read_csv('C:/Users/simas/PycharmProjects/miniProject/Duomenys/Isvalyti_failai/knygos.csv')

# Skaiciuojame knygu skaiciu kiekviename zanre
zanro_skaicius = df['Žanras'].value_counts().reset_index()
zanro_skaicius.columns = ['Žanras', 'Knygų skaičius']

# Ieskome top 10 geriausiu autoriu knygos.lt puslapyje
"""
Weighted rating (WR) = (v ÷ (v+m)) × R + (m ÷ (v+m)) × C , where:

* R = average for the movie (mean) = (Rating)
* v = number of votes for the movie = (votes)
* m = minimum votes required to be listed in the Top 250 (currently 25,000)
* C = the mean vote across the whole report (currently 6.9)
"""

autoriaus_vid_ivertinimas = df.groupby("Autorius").agg({
    'Reitingas': 'mean', # Apskaiciuojame vidutini reitinga (R)
    "Įvertinimų skaičius" : 'sum' # Susumuojame visus ivertinimus (v)
}).reset_index()

# Kuriame bendra visu autoriu vidutini reitinga
C =  autoriaus_vid_ivertinimas['Reitingas'].mean()

m = 12
# Apskaiciuojame reitingo svori
autoriaus_vid_ivertinimas['Reitingo svoris'] = ((autoriaus_vid_ivertinimas["Įvertinimų skaičius"] /
                                                (autoriaus_vid_ivertinimas["Įvertinimų skaičius"] + m)) *
                                                autoriaus_vid_ivertinimas["Reitingas"] +
                                                (m / (autoriaus_vid_ivertinimas["Įvertinimų skaičius"] + m)) * C)

# Imame Top 10 Autoriu
top_autoriai = autoriaus_vid_ivertinimas.sort_values(by=['Reitingo svoris'], ascending=False).head(10).reset_index(drop=True)

print(top_autoriai.round(2))
# Kuriame stulpeline diagrama
fig_bar_top = px.bar(
    top_autoriai,
    x="Autorius", y='Reitingo svoris',
    text="Įvertinimų skaičius" ,
    title='Top 10 Autorių Knygos.lt Svetainėje',
    labels={"Reitingo svoris": "Reitingo svoris", "Autorius": "Autorius"},
    template='plotly_white',
    color='Autorius'
)
fig_bar_top.show()

# Kuriame burbuline diagrama
fig_bubble = px.scatter(df, x='Kaina €', y='Reitingas', size='Įvertinimų skaičius',
                        color='Žanras', hover_name='Knygos pavadinimas',
                        title='Burbulinė diagrama: Kaina vs Reitingas',size_max=150,
                        template='plotly_white')
fig_bubble.show()


