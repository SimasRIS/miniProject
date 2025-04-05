# Importai
import pandas as pd
import plotly.express as px

# Pasiimame duomenis
df = pd.read_csv('C:/Users/simas/PycharmProjects/miniProject/Duomenys/Isvalyti_failai/knygos_cleaned.csv')



# 1. Kainu pasiskirstymo histograma
fig_hist = px.histogram(
    df, x='Kaina €', nbins=30, # nbins - gali keisti stulpeliu skaiciu
    title='Kainų pasiskirstymas', labels={'Kaina €': 'Kaina €'},
    template='plotly_dark'
)
fig_hist.update_layout(bargap=0.1) # Sumaziname tarpa tarp stulpeliu
fig_hist.show()

# 2. Kainos vs Reitingo sklaidos diagrama
fig_scatter = px.scatter(
    df, x='Kaina €', y='Reitingas', title="Kaina vs Reitingas",
    labels={'Kaina €': 'Kaina €', 'Reitingas': 'Reitingas'},
    template='plotly_dark', hover_data=df.columns
)
fig_scatter.update_traces(marker=dict(size=10, opacity=0.7))
fig_scatter.show()

# 3. Ieskome top 10 geriausiu autoriu knygos.lt puslapyje
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


# 4. Kuriame skrituline diagrama parodancia kokio zanro yra daugiausia autoriu
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

# 5. Ieskome knygu vidutines kainos
# Gruojame pagal zanra ir vidutines kainos apskaiciavima
zanro_vid_kaina = df.groupby('Žanras', as_index=False)['Kaina €'].mean()
print(zanro_vid_kaina)
# Apskaiciuojame bendrai visu knygu vidutine kaina
bendra_vidutine_kaina = df['Kaina €'].mean()

# Ieskome zanro, kurio vidutine kaina yra didziausia (brangiausia)
brangiausias_zanras = zanro_vid_kaina.loc[zanro_vid_kaina['Kaina €'].idxmax()]

# Ieskome zanro, kurio vidutine kaina yra maziausia (pigiausia)
pigiausias_zanras = zanro_vid_kaina.loc[zanro_vid_kaina['Kaina €'].idxmin()]

# Ieskome zanro, kurio vidutine kaina yra artimiausia bendrai vidutinei kainai
zanro_vid_kaina['diff'] = abs(zanro_vid_kaina['Kaina €'] - bendra_vidutine_kaina)
artimiausias_vid_kainai = zanro_vid_kaina.loc[zanro_vid_kaina['diff'].idxmin()]

# Isvedame rezultatus
print("Brangiausias žanras:")
print(brangiausias_zanras.round(2))
print("Pigiausias žanras:")
print(pigiausias_zanras.round(2))
print("Žanras, kurio kaina artimiausia bendrai vidutinei:")
print(artimiausias_vid_kainai.round(2))

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
    x=[brangiausias_zanras['Žanras']],
    y=[brangiausias_zanras['Kaina €']],
    mode='markers',
    marker=dict(color='red', size=12),
    name='Brangiausias žanras'
)
fig.add_scatter(
    x=[pigiausias_zanras['Žanras']],
    y=[pigiausias_zanras['Kaina €']],
    mode='markers',
    marker=dict(color='green', size=12),
    name='Pigiausias žanras'
)
fig.add_scatter(
    x=[artimiausias_vid_kainai['Žanras']],
    y=[artimiausias_vid_kainai['Kaina €']],
    mode='markers',
    marker=dict(color='blue', size=12),
    name='Artimiausias vidutinei kainai'
)
fig.show()

# 6. Ieskome kiek yra pigiu, vidutines kainos ir brangiu knygu

# Priskirsime kainas pagal kategorija
def kainu_kategorija(kaina):
    if kaina <= 10:
        return 'Pigi (0-10 €)'
    elif kaina <= 20:
        return 'Vidutine (10-20 €)'
    else:
        return 'Brangi (>20 €)'

# Kuriame stulpeli su kainu kategorija
df["Kainu Kategorija"] = df["Kaina €"].apply(kainu_kategorija)

# Skaiciuojame kiek yra knygu kiekvienoje kategorijoje
kategoriju_skaicius = df["Kainu Kategorija"].value_counts().reset_index()
kategoriju_skaicius.columns = ['Kainu Kategorija', 'Knygų skaičius']

fig_bar_two = px.bar(
    kategoriju_skaicius, x='Kainu Kategorija',
    y='Knygų skaičius', text='Knygų skaičius',
    title='Kygų skaičius pagal kategorijas',
    labels={'Kainu Kategorija': 'Kainu Kategorija', 'Knygų skaičius':'Knygų skaičius'},
    template='plotly_dark'
)
fig_bar_two.show()
