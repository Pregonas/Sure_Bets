from selenium import webdriver
from code.calculadora.calculadora_apuestas import calculadora_tenis
import time
from code.telegram import telegram_bot_sendtext

###betway
chromedriver = "C:/Users/cpreg/OneDrive/Desktop/chromedriver/chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.get('https://sports.betway.es/en/sports/cat/tennis')

time.sleep(10)
partidos = driver.find_elements_by_class_name('oneLineEventItem')

time.sleep(3)

tennis_list = []
for partido in partidos:
    jugadores = partido.find_elements_by_class_name('teamNameEllipsisContainer')
    cuota = partido.find_elements_by_class_name('odds')
    jugadorA = jugadores[0].find_element_by_xpath('.//span').text
    jugadorB = jugadores[1].find_element_by_xpath('.//span').text
    try:
        cuotaA = cuota[0].text
        cuotaB = cuota[1].text
        cuotaA = float(cuotaA)
        cuotaB = float(cuotaB)
        rentable = calculadora_tenis(cuotaA, cuotaB)
    except:
        cuotaA = '-'
        cuotaB = '-'
        rentable = 'Unknown'
        pass
    tennis_list.append([jugadorA, cuotaA, jugadorB, cuotaB, rentable])



#International match
driver.get('https://sports.betway.es/en/sports/grp/tennis/exhibition/international-tennis-series')

time.sleep(5)
partidos = driver.find_elements_by_class_name('oneLineEventItem')

time.sleep(3)

for partido in partidos:
    jugadores = partido.find_elements_by_class_name('teamNameEllipsisContainer')
    cuota = partido.find_elements_by_class_name('odds')
    jugadorA = jugadores[0].find_element_by_xpath('.//span').text
    jugadorB = jugadores[1].find_element_by_xpath('.//span').text
    try:
        cuotaA = cuota[0].text
        cuotaB = cuota[1].text
        cuotaA = float(cuotaA)
        cuotaB = float(cuotaB)
        rentable = calculadora_tenis(cuotaA, cuotaB)
    except:
        cuotaA = '-'
        cuotaB = '-'
        rentable = 'Unknown'
        pass
    tennis_list.append([jugadorA, cuotaA, jugadorB, cuotaB, rentable])
print(tennis_list)
driver.close()

p = 1
for match in tennis_list:
    message = "Partido " + str(p) + ":\nJugador A: " + match[0] + ' -- Cuota A: ' + str(match[1]) + '€\nJugador B: ' + match[2] + ' -- Cuota B: ' + str(match[3]) + '€\n\n'
    telegram_bot_sendtext(message)
    p = p + 1