from code.calculadora.calculadora_apuestas import calculadora_tenis
from code.telegram import telegram_bot_sendtext
import requests
from bs4 import BeautifulSoup

def sure_bets():
    web_url= requests.get('https://oddspedia.com/es/surebets/')

    web_soup= BeautifulSoup(web_url.text, 'html.parser')
    partidos = web_soup.find_all('div', class_="btools-match")

    for partido in partidos:
        try:
            time = partido.find("div", class_="btools-match-time").find("span").text
            equips = partido.find("div", class_="btools-match-teams").find("p").find("a").text
            equip = list(equips.split("\t"))
            equipA = equip[5].strip()
            equipB = equip[10].strip()
            aposta = str(partido.find("div", class_="btools-match-teams").find("span").text)
            cuotes = partido.find_all('div', class_="odd-primary-mini__link")
            list_cuotes = []
            for cuota in cuotes:
                xifra = cuota.find("div", class_="odd-primary-mini__value").find("span").text
                casa = cuota.find("div", class_="odd-primary-mini__logo").find("img")["data-src"]
                filename = casa.split('/')[-1].split('.')[0]
                list_cuotes.append(xifra)
                list_cuotes.append(filename)

            print(list_cuotes)

        except:
            pass

if __name__ == "__main__":
    sure_bets()
