# Importuojam bibliotekas
import requests
from bs4 import BeautifulSoup
import re
import csv

# Klase skirta tinklapio duomenu isgavimui
class WebScraper:
    def __init__(self, url):
        self.url = url # Issaugome svetaines URL
        self.knygu_duomenenys = [] # Sukuriame sarasa duomenims saugoti


    def fetch_html(self):
        # Si funkcija siuncia HTTP GET uzklausa i nurodyta URL
        response = requests.get(self.url, headers={'User-Agent': 'Mozilla/5.0'})
        response.encoding = 'utf-8' # Skaitytu lietuviskas raides
        if response.status_code == 200: # tikriname ar sekmingai pasiekiame puslapi
            return response.text # Grazina puslapio turini kaip teksta
        else:
            # Jei nepasiekia puslapio spausdina klaida ir grazina None
            print(f'Klaida: negalima pasiekti svetaines{self.url}')
            return None

    def parse_html(self, html): # Funkcija kuri inicijuoja puslapio analizavima
        raise NotImplementedError("Sis metodas turi buti perrasytas kitoje klaseje")

    def scraper(self): # Inicijuoja visa scrapinimo procesa
        html = self.fetch_html()  # Kviecia fetch_html() funkcija, kad gautume HTML turini
        if html:
            self.parse_html(html) # Gauta HTML apdorojame su parse_html() funkcija

# Uzsienio autoriu romanu duomenu isgavimas
class UzsienioAutoriuRomanai(WebScraper):
    def parse_html(self, html): # Apdoroja gauta HTML ir istraukia reikiamus duomenis
        soup = BeautifulSoup(html, 'html.parser')
        knygu_info = soup.find_all('div', class_='product') # Susirandame visas knygas
        knygu_scrape_info = [] # Saugome knygu duomenis
        for knyga in knygu_info: # Einame po visas knygu_info eilutes atskirai
            # Ieskome knygos pavadinimo
            knygos_pavadinimas_el = knyga.find('img', class_='swiper-lazy lazy-compact')
            if knygos_pavadinimas_el:
                knygos_pavadinimas = knygos_pavadinimas_el.get('title')
            # Ieskome knygos autoriu
            autorius_el = knyga.find('span', class_='book-properties book-author')
            if autorius_el:
                autorius = autorius_el.text.strip()
            else:
                autorius = "Nezinomas autorius"
            # Ieskome knygos kainos
            kaina_div = knyga.find_all('div', class_='product-price')
            if len(kaina_div) > 1:
                kaina_div_el = kaina_div[1]
            else:
                kaina_div_el = kaina_div[0]
            kaina_el = kaina_div_el.text.strip()
            # Isvalome visus nereikalingus duomenis
            match = re.search(r'(\d+\,\d+)', kaina_el)
            if match:
                kaina = match.group(1).replace(',','.')
            else:
                kaina = kaina_el
            # Ieskome ivertinimo/reitingo
            zvaigzdutes = knyga.select('.book-stars i:not(.empty)')
            reitingas=len(zvaigzdutes)
            # Ieskome zmoniu ivertinimo skaiciaus
            ivertinimo_el = knyga.find('span', class_='badge badge-secondary ml-1')
            # Tikriname ar elementas egzistuoja ir ar jo tekstas nera tuscias
            if ivertinimo_el and ivertinimo_el.text.strip():
                ivertinimas = ivertinimo_el.text.strip()
            else:
                ivertinimas = 0

            knygu_scrape_info.append((knygos_pavadinimas, autorius, kaina, reitingas, ivertinimas))

        self.knygu_duomenenys = knygu_scrape_info

class Fantastika(WebScraper):
    def parse_html(self, html): # Apdoroja gauta HTML ir istraukia reikiamus duomenis
        soup = BeautifulSoup(html, 'html.parser')
        knygu_info = soup.find_all('div', class_='product') # Susirandame visas knygas
        knygu_scrape_info = [] # Saugome knygu duomenis
        for knyga in knygu_info: # Einame po visas knygu_info eilutes atskirai
            # Ieskome knygos pavadinimo
            knygos_pavadinimas_el = knyga.find('img', class_='swiper-lazy lazy-compact')
            if knygos_pavadinimas_el:
                knygos_pavadinimas = knygos_pavadinimas_el.get('title')
            # Ieskome knygos autoriu
            autorius_el = knyga.find('span', class_='book-properties book-author')
            if autorius_el:
                autorius = autorius_el.text.strip()
            else:
                autorius = "Nezinomas autorius"
            # Ieskome knygos kainos
            kaina_div = knyga.find_all('div', class_='product-price')
            if len(kaina_div) > 1:
                kaina_div_el = kaina_div[1]
            else:
                kaina_div_el = kaina_div[0]
            kaina_el = kaina_div_el.text.strip()
            # Isvalome visus nereikalingus duomenis
            match = re.search(r'(\d+\,\d+)', kaina_el)
            if match:
                kaina = match.group(1).replace(',','.')
            else:
                kaina = kaina_el
            # Ieskome ivertinimo/reitingo
            zvaigzdutes = knyga.select('.book-stars i:not(.empty)')
            reitingas=len(zvaigzdutes)
            # Ieskome zmoniu ivertinimo skaiciaus
            ivertinimo_el = knyga.find('span', class_='badge badge-secondary ml-1')
            # Tikriname ar elementas egzistuoja ir ar jo tekstas nera tuscias
            if ivertinimo_el and ivertinimo_el.text.strip():
                ivertinimas = ivertinimo_el.text.strip()
            else:
                ivertinimas = 0

            knygu_scrape_info.append((knygos_pavadinimas, autorius, kaina, reitingas, ivertinimas))

        self.knygu_duomenenys = knygu_scrape_info

class DetektyvaiTrileriai(WebScraper):
    def parse_html(self, html): # Apdoroja gauta HTML ir istraukia reikiamus duomenis
        soup = BeautifulSoup(html, 'html.parser')
        knygu_info = soup.find_all('div', class_='product') # Susirandame visas knygas
        knygu_scrape_info = [] # Saugome knygu duomenis
        for knyga in knygu_info: # Einame po visas knygu_info eilutes atskirai
            # Ieskome knygos pavadinimo
            knygos_pavadinimas_el = knyga.find('img', class_='swiper-lazy lazy-compact')
            if knygos_pavadinimas_el:
                knygos_pavadinimas = knygos_pavadinimas_el.get('title')
            # Ieskome knygos autoriu
            autorius_el = knyga.find('span', class_='book-properties book-author')
            if autorius_el:
                autorius = autorius_el.text.strip()
            else:
                autorius = "Nezinomas autorius"
            # Ieskome knygos kainos
            kaina_div = knyga.find_all('div', class_='product-price')
            if len(kaina_div) > 1:
                kaina_div_el = kaina_div[1]
            else:
                kaina_div_el = kaina_div[0]
            kaina_el = kaina_div_el.text.strip()
            # Isvalome visus nereikalingus duomenis
            match = re.search(r'(\d+\,\d+)', kaina_el)
            if match:
                kaina = match.group(1).replace(',','.')
            else:
                kaina = kaina_el
            # Ieskome ivertinimo/reitingo
            zvaigzdutes = knyga.select('.book-stars i:not(.empty)')
            reitingas=len(zvaigzdutes)
            # Ieskome zmoniu ivertinimo skaiciaus
            ivertinimo_el = knyga.find('span', class_='badge badge-secondary ml-1')
            # Tikriname ar elementas egzistuoja ir ar jo tekstas nera tuscias
            if ivertinimo_el and ivertinimo_el.text.strip():
                ivertinimas = ivertinimo_el.text.strip()
            else:
                ivertinimas = 0

            knygu_scrape_info.append((knygos_pavadinimas, autorius, kaina, reitingas, ivertinimas))

        self.knygu_duomenenys = knygu_scrape_info

class PoezijaDramaEse(WebScraper):
    def parse_html(self, html): # Apdoroja gauta HTML ir istraukia reikiamus duomenis
        soup = BeautifulSoup(html, 'html.parser')
        knygu_info = soup.find_all('div', class_='product') # Susirandame visas knygas
        knygu_scrape_info = [] # Saugome knygu duomenis
        for knyga in knygu_info: # Einame po visas knygu_info eilutes atskirai
            # Ieskome knygos pavadinimo
            knygos_pavadinimas_el = knyga.find('img', class_='swiper-lazy lazy-compact')
            if knygos_pavadinimas_el:
                knygos_pavadinimas = knygos_pavadinimas_el.get('title')
            # Ieskome knygos autoriu
            autorius_el = knyga.find('span', class_='book-properties book-author')
            if autorius_el:
                autorius = autorius_el.text.strip()
            else:
                autorius = "Nezinomas autorius"
            # Ieskome knygos kainos
            kaina_div = knyga.find_all('div', class_='product-price')
            if len(kaina_div) > 1:
                kaina_div_el = kaina_div[1]
            else:
                kaina_div_el = kaina_div[0]
            kaina_el = kaina_div_el.text.strip()
            # Isvalome visus nereikalingus duomenis
            match = re.search(r'(\d+\,\d+)', kaina_el)
            if match:
                kaina = match.group(1).replace(',','.')
            else:
                kaina = kaina_el
            # Ieskome ivertinimo/reitingo
            zvaigzdutes = knyga.select('.book-stars i:not(.empty)')
            reitingas=len(zvaigzdutes)
            # Ieskome zmoniu ivertinimo skaiciaus
            ivertinimo_el = knyga.find('span', class_='badge badge-secondary ml-1')
            # Tikriname ar elementas egzistuoja ir ar jo tekstas nera tuscias
            if ivertinimo_el and ivertinimo_el.text.strip():
                ivertinimas = ivertinimo_el.text.strip()
            else:
                ivertinimas = 0

            knygu_scrape_info.append((knygos_pavadinimas, autorius, kaina, reitingas, ivertinimas))

        self.knygu_duomenenys = knygu_scrape_info

if __name__ == '__main__':
    # Kuriame sarasa kuriame yra nurodyta klase, URL ir zanras
    grozine_literatura =[(UzsienioAutoriuRomanai, 'https://www.knygos.lt/lt/elektronines-knygos/zanras/uzsienio-proza/?psl={}', 'Užsienio romanai'),
                         (Fantastika, 'https://www.knygos.lt/lt/elektronines-knygos/zanras/fantastika-ir-fantasy/?psl={}', 'Fantastika'),
                         (DetektyvaiTrileriai, 'https://www.knygos.lt/lt/elektronines-knygos/zanras/detektyvai-trileriai/?psl={}', 'Detektyvai/Trileriai'),
                         (PoezijaDramaEse, 'https://www.knygos.lt/lt/elektronines-knygos/zanras/poezija-drama-ese/?psl={}', ' Poezija/Drama/Ese')]

    visi_duomenys = [] # Saugosime visus musu duomenis

    # Darome for cikla, kad eitu per grozines literaturos klases ir URL
    for scraper_klase, url_puslapis, zanras in grozine_literatura:
        # Kuriame cikla kuris eitu per puslapius nuo 1 iki 100
        for puslapis in range(1, 101):
            url = url_puslapis.format(puslapis)
            print(f'Apdorojamas puslapis: {url}')
            scraper_psl = scraper_klase(url)
            scraper_psl.scraper()
            # Jei puslapyje yra duomenu, tada duomenis prides i "visus duomenis"
            if scraper_psl.knygu_duomenenys:
                for eilute in scraper_psl.knygu_duomenenys:
                    zanro_eilute = eilute + (zanras,)
                    visi_duomenys.append(zanro_eilute)
            else:
                break


    print(len(visi_duomenys))
    print(visi_duomenys)

with open("../Duomenys/Isvalyti_failai/knygos.csv", "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Knygos pavadinimas", "Autorius", "Kaina €",
                     "Reitingas", "Įvertinimų skaičius", "Žanras"])

    for row in visi_duomenys:
        writer.writerow(row)