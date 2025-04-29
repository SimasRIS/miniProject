# Užduotis:

Sukurti sistemą, kuri surenka informaciją apie produktus iš el. parduotuvės (naudojant BeautifulSoup), analizuoja duomenis (pandas), vizualizuoja rezultatus (matplotlib) ir klasifikuoja ar grupuoja produktus pagal savybes (naudojant KMeans, DBSCAN ar DecisionTreeClassifier).

# Reikalavimai:

1. **Bibliotekos**
- pandas – duomenų analizė
- bs4 (BeautifulSoup) – duomenų nuskaitymas iš HTML
- matplotlib – duomenų vizualizavimas
- sklearn – klasifikacijos ir grupavimo algoritmai (KMeans, DBSCAN, DecisionTreeClassifier)
2. **Funkcionalumas**
- Duomenų surinkimas( <5000 duomenų)
- Naudojant BeautifulSoup, nuskaityti produktų duomenis (pavadinimas, kaina, reitingas, aprašymas)
iš el. parduotuvės HTML puslapio.
    
**Duomenų apdorojimas**
-    Sukurti DataFrame su pandas.
-    Atlikti duomenų valymą (trūkstamų reikšmių tvarkymas, tipų keitimas).
    
**Vizualizacijos**
-    Sukurti bent 2 vizualizacijas su matplotlib:
-    Kainų pasiskirstymo histograma.
-    Kainos vs reitingas sklaidos diagrama.
    
**Klasifikavimas ar grupavimas**
-    Pritaikyti vieną iš algoritmų:
-    KMeans – grupuoti produktus pagal kainą ir reitingą.
-    DBSCAN – ieškoti natūralių grupių.
-    DecisionTreeClassifier – klasifikuoti produktus pagal nurodytas kategorijas.
    
3. **Papildomai**
- Pridėti produkto kategorijos analizę.
- Nustatyti, kokios savybės turi įtakos produkto kainai.
- Sukurti paprastą vartotojo sąsają.

# miniProject

## Diegimas ir paleidimas

### Būtinos sąlygos

- **Python ≥ 3.9**
- **Git**

### Įdiegimo ir paleidimo žingsniai

```
# 1. Klonuokite saugyklą iš GitHub
git clone https://github.com/SimasRIS/miniProject.git
cd miniProject

# 2. (Rekomenduojama) sukurkite ir aktyvuokite virtualią aplinką
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 3. Įdiekite priklausomybes
pip install -r requirements.txt

# 4. Paleiskite programą
python main.py
```

### Programos naudojimas

Paleidus `main.py`, terminale matysite šias parinktis:

1. Duomenų nuskaitymas (web scraping)
2. Duomenų valymas
3. Vizualizacijos
4. KMeans grupavimas
5. DBSCAN grupavimas
6. Sprendimo medžio klasifikacija
7. Išeiti

Pasirinkite norimą veiksmą įvesdami atitinkamą skaičių.


## Projekto apžvalga

Šis projektas analizuoja elektronines knygas iš [Knygos.lt](http://Knygos.lt) svetainės. Jis renka, tvarko ir analizuoja informaciją apie knygas.

1. **Duomenų rinkimas** - Programa `web_scrapinimas.py` automatiškai surenka informaciją apie knygas iš keturių kategorijų:
• Užsienio romanai
• Fantastika
• Detektyvai ir trileriai
• Poezija, drama ir esė
Programa išsaugo knygų pavadinimus, autorius, kainas, įvertinimus ir atsiliepimų skaičių į failą `knygos.csv`.
2. **Duomenų tvarkymas** - Programa `duomenu_valymas.py` sutvarko surinktą informaciją: pašalina besikartojančias knygas, paverčia tekstą į skaičius ir pašalina neišsamius įrašus. Rezultatai išsaugomi faile `knygos_cleaned.csv`.
3. **Duomenų analizė** - Kelios programos (`visualizacija.py`, `KMeans.py`, `DBscan.py` ir `decision_tree.py`) sukuria 9 skirtingų grafikų ir diagramų, kurie parodo įdomius knygų duomenų ryšius.
4. **Programos valdymas** - Programa `main.py` leidžia lengvai valdyti visą procesą per paprastą meniu: nuo duomenų rinkimo iki analizės.

---

### 1. Kainų pasiskirstymo histograma

**Failas:** `visualizacija.py`

**Kas rodoma:** Diagrama, kuri rodo, kiek knygų yra skirtingose kainų grupėse. X ašyje matome kainas eurais, o Y ašyje - knygų kiekį.

**Ką galima pastebėti:** Kainos pasiskirsto varpo formos kreive - daugiausia knygų kainuoja nuo 9 iki 12 eurų. Beveik visos knygos kainuoja mažiau nei 20 eurų, nors yra ir keletas brangesnių.ių.

### 2. Kainos ir įvertinimų palyginimo diagrama

**Failas:** `visualizacija.py` 

**Kas rodoma:** Grafikas, kuriame kiekviena knyga pavaizduota kaip taškas. Horizontalioje ašyje matoma knygos kaina, o vertikalioje - knygos įvertinimas žvaigždutėmis.

**Įžvalgos:** Tyrime paaiškėjo, kad knygos kaina beveik nesusijusi su jos įvertinimu. Tai reiškia, kad brangesnės knygos nebūtinai yra geriau vertinamos skaitytojų - žmonės vertina knygą pagal jos turinį, o ne pagal kainą.

### 3. Populiariausių 10 autorių diagrama

**Failas:** `visualizacija.py`

**Ką parodo:** Skaičiuoja autorių populiarumo balą, kuris įvertina ir knygų įvertinimus, ir atsiliepimų skaičių. Naudojama panaši sistema kaip IMDB filmų vertinime.

**Kas rodoma:** Stulpelinė diagrama, kur:
- X ašyje - autorių vardai
- Y ašyje - jų populiarumo balas
- Virš kiekvieno stulpelio rodomas, kiek žmonių įvertino autoriaus knygas

**Įžvalgos:** Ši diagrama padeda tiksliau nustatyti populiariausius autorius. Ji neišskiria autorių vien dėl kelių gerų įvertinimų - reikia ir pakankamai daug skaitytojų atsiliepimų.

### 4. Skritulinė diagrama: Kiek autorių rašo skirtinguose žanruose

**Failas:** `visualizacija.py` 

**Ką matome:** Apvali diagrama, kuri parodo, kiek rašytojų rašo kiekviename knygų žanre.

**Įžvalgos:** Diagrama aiškiai parodo, kuriuose žanruose rašo daugiau autorių, o kuriuose mažiau.

### 5. Vidutinės knygų kainos pagal žanrus

**Failas:** `visualizacija.py` 

**Kas rodoma:** Stulpelinė diagrama, kuri rodo vidutinę knygų kainą kiekviename žanre. Diagramoje yra pažymėti trys svarbūs taškai:
- Brangiausias žanras (raudonas taškas)
- Pigiausias žanras (žalias taškas)
- Vidutinės kainos žanras (mėlynas taškas)

**Įžvalgos:** Ši diagrama parodo, kuriuose žanruose knygos yra brangiausios ir pigiausios, bei kuris žanras geriausiai atspindi vidutinę knygų kainą rinkoje.

### 6. Kaip knygos pasiskirsto pagal kainas

**Failas:** `visualizacija.py`

**Kas rodoma:** Paprasta diagrama su trimis stulpeliais, kuri rodo, kiek yra knygų kiekvienoje kainų grupėje:
- Pigios knygos (iki 10 €)
- Vidutinės kainos knygos (10-20 €)
- Brangios knygos (daugiau nei 20 €)

**Įžvalgos:** Ši diagrama padeda suprasti, kokios kainos yra įprastos knygyne, ir palengvina sprendimą, kiek pinigų skirti knygai.

### 7. Knygų grupavimas pagal kainas ir įvertinimus

**Failas:** `KMeans.py`

**Ką analizuojame:** Knygų kainas, įvertinimus ir atsiliepimų skaičių. Visos knygos suskirstytos į tris grupes.

**Ką matome diagramoje:** Grafikas, kuris rodo knygų kainas ir įvertinimus. Skirtingos knygų grupės pažymėtos skirtingomis spalvomis.

**Ką sužinojome:**

- **Pirmoji grupė:** Pigesnės knygos su žemesniais įvertinimais.
- **Antroji grupė:** Vidutinės kainos knygos, kurios turi daug gerų įvertinimų - tai populiariausios knygos.
- **Trečioji grupė:** Brangesnės knygos su įvairiais įvertinimais - tai specializuotos arba prabangesnės knygos.

Šis suskirstymas padeda geriau suprasti knygų rinką ir gali padėti nustatyti tinkamas knygų kainas.

### 8. Knygų žanrų grupavimas pagal kainą ir įvertinimus

**Failas:** `DBscan.py`

**Ką analizuojame:** Skaičiuojame kiekvieno knygų žanro vidutinę kainą ir įvertinimą. Naudojame DBSCAN metodą, kuris padeda sugrupuoti panašius žanrus.

**Kaip atrodo:** Diagramoje matome taškus, kur kiekvienas taškas yra atskiras knygų žanras. Prie taško užrašytas žanro pavadinimas. Panašūs žanrai pažymėti ta pačia spalva.

**Ką sužinome:** Ši diagrama mums parodo, kurie knygų žanrai yra panašūs pagal kainą ir skaitytojų įvertinimus. Taip pat matome, kurie žanrai išsiskiria iš kitų savo kainomis ar įvertinimais.

### 9. Kainų numatymo modelis

**Failas:** `decision_tree.py`

**Kaip veikia:** Programa naudoja sprendimų medį, kuris padeda numatyti, ar knyga bus pigi, vidutinės kainos ar brangi. Sprendimas priimamas remiantis dviem dalykais:
• Knygos įvertinimu žvaigždutėmis
• Atsiliepimų skaičiumi

**Ką matome:** Programa sukuria aiškų medžio vaizdą, kuriame spalvomis pažymėta, kaip priimami sprendimai apie knygos kainą.

**Ką sužinome:** Programa parodo, kokie knygų įvertinimai ir atsiliepimų skaičiai dažniausiai lemia knygos kainą. Pavyzdžiui, jei knyga turi daugiau nei 4 žvaigždutes ir daugiau nei 15 atsiliepimų, ji greičiausiai bus brangesnė. Programa taip pat parodo, kaip tiksliai ji gali atspėti knygų kainas.