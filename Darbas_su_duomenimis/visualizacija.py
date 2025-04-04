# Importai
import pandas as pd
import plotly.express as px

# Pasiimame duomenis
df = pd.read_csv('C:/Users/simas/PycharmProjects/miniProject/Duomenys/Isvalyti_failai/knygos_cleaned.csv')



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

# Nusakome minimalu ivertinomo skaiciu
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
    template='plotly_dark',
    color='Autorius'
)
fig_bar_top.show()


# Kuriame skrituline diagrama parodancia kokio zanro yra daugiausia autoriu
# Su GROUP BY suskaiciuojame kiek zanruose yra unikaliu autoriu.
zanro_autoriai = df.groupby('Žanras')['Autorius'].nunique()
zanro_autoriai = zanro_autoriai.reset_index(name="Autorių skaičius") # Pakeiciame stulpelio pavadinima
print(zanro_autoriai)
# Kuriame skrituline diagrama
fig_pie = px.pie(
    zanro_autoriai,
    names='Žanras',
    values="Autorių skaičius",
    title='Autorių skaičius pagal žanrą',
    template='plotly_dark'
)
fig_pie.show()

# Kainu pasiskirstymo histograma
fig_hist = px.histogram(
    df, x='Kaina €', nbins=30, # nbins - gali keisti stulpeliu skaiciu
    title='Kainų pasiskirstymas', labels={'Kaina €': 'Kaina €'},
    template='plotly_dark'
)
fig_hist.update_layout(bargap=0.1) # Sumaziname tarpa tarp stulpeliu
fig_hist.show()

# Kainos vs Reitingo sklaidos diagrama
fig_scatter = px.scatter(
    df, x='Kaina €', y='Reitingas', title="Kaina vs Reitingas",
    labels={'Kaina €': 'Kaina €', 'Reitingas': 'Reitingas'},
    template='plotly_dark', hover_data=df.columns
)
fig_scatter.update_traces(marker=dict(size=10, opacity=0.7))
fig_scatter.show()

# Grupavimas pagal zanra ir vidutines kainos apskaiciavimas
zanro_vid_kaina = df.groupby('Žanras', as_index=False)['Kaina €'].mean()

# Apskaiciuojame bendrai visų knygu vidutine kaina
overall_mean = df['Kaina €'].mean()

# Randame zanra, kurio vidutine kaina yra didziausia (brangiausios)
most_expensive_genre = zanro_vid_kaina.loc[zanro_vid_kaina['Kaina €'].idxmax()]

# Randame zanra, kurio vidutine kaina yra maziausia (pigiausios)
cheapest_genre = zanro_vid_kaina.loc[zanro_vid_kaina['Kaina €'].idxmin()]

# Randame zanra, kurio vidutine kaina yra artimiausia bendrai vidutinei
zanro_vid_kaina['diff'] = abs(zanro_vid_kaina['Kaina €'] - overall_mean)
closest_to_overall = zanro_vid_kaina.loc[zanro_vid_kaina['diff'].idxmin()]

# Isvedame rezultatus
print("Brangiausias žanras:")
print(most_expensive_genre.round(2))
print("\nPigiausias žanras:")
print(cheapest_genre.round(2))
print("\nŽanras, kurio kaina artimiausia bendrai vidutinei:")
print(closest_to_overall.round(2))

# Vizualizacija: vidutines kainos pagal zanrus
fig = px.bar(
    zanro_vid_kaina,
    x='Žanras',
    y='Kaina €',
    title='Vidutinė kaina pagal žanrus',
    labels={'Kaina €': 'Vidutinė kaina', 'Žanras': 'Žanras'},
    template='plotly_dark'
)

# Pazymime svarbiausias reiksmes: brangiausias, pigiausias ir artimiausias bendrai vidutinei
fig.add_scatter(
    x=[most_expensive_genre['Žanras']],
    y=[most_expensive_genre['Kaina €']],
    mode='markers',
    marker=dict(color='red', size=12),
    name='Brangiausias žanras'
)
fig.add_scatter(
    x=[cheapest_genre['Žanras']],
    y=[cheapest_genre['Kaina €']],
    mode='markers',
    marker=dict(color='green', size=12),
    name='Pigiausias žanras'
)
fig.add_scatter(
    x=[closest_to_overall['Žanras']],
    y=[closest_to_overall['Kaina €']],
    mode='markers',
    marker=dict(color='blue', size=12),
    name='Artimiausias bendrai vidutinei'
)

fig.show()