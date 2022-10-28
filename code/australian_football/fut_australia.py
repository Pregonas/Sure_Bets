from code.calculadora.calculadora_apuestas import calculadora_tenis
from code.telegram import telegram_bot_sendtext
import requests
from bs4 import BeautifulSoup

def fut_australia():
    web_url= requests.get('https://oddspedia.com/es/futbol-australiano/')

    web_soup= BeautifulSoup(web_url.text, 'html.parser')
    partidos = web_soup.find_all('tr', class_="match-data")


    for partido in partidos:
        try:
            time = partido.find("span", class_="min_time").text
            jugadores = partido.find_all("span", class_='match-name')
            jugadorA = jugadores[0].text
            jugadorB = jugadores[1].text
            cuotas = partido.find_all("div", class_='relative z-index-5')
            cuotaA = cuotas[0].text
            cuotaB = cuotas[1].text
            casaA = partido.find("td", class_="relative val_1").find("a").get('title')
            casaB = partido.find("td", class_="relative val_2").find("a").get('title')
            algoritme = calculadora_tenis(float(cuotaA), float(cuotaB))
            rentable = algoritme[0]
            x = algoritme[1]
            y = algoritme[2]
            Ganancia_x = algoritme[3]
            Ganancia_y = algoritme[4]
            y_max = algoritme[5]
            y_min = algoritme[6]

            if rentable == True:

                message = 'Fut. Australia : (' + time + ')\nJugador A: ' + jugadorA + ' -- ' + casaA + ' : ' + str(cuotaA) + '€\nJugador B: ' \
                          + jugadorB + ' -- ' + casaB + ' : ' + str(cuotaB) + '€\nApuesta en A : ' + str(x) + '\nApuesta en B entre : ' \
                          + str(y_min) + ' - ' + str(y_max) + '\nEj. Apuesta B = ' + str(y) +'\nGanancia si gana A : ' + str(Ganancia_x) + \
                          '€\nGanancia si gana B : ' + str(Ganancia_y) + '€\n\n'
                telegram_bot_sendtext(message, '-474719636')

        except:
            pass

if __name__ == "__main__":
    fut_australia()