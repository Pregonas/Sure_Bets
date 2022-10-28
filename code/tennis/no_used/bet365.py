from selenium import webdriver
from code.calculadora.calculadora_apuestas import calculadora_tenis
import time


chromedriver = "C:/Users/cpreg/OneDrive/Desktop/chromedriver/chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.get('https://www.bet365.com/')

time.sleep(5)
partidos = driver.find_elements_by_class_name('sgl-ParticipantFixtureDetails_LhsContainer')
partidos_principales = driver.find_element_by_class_name('sgl-MarketOddsExpand.gl-Market_General.gl-Market_General-columnheader ')

bet365_list = []
for partido in partidos:
    jugadores = partido.find_elements_by_class_name('sgl-ParticipantFixtureDetails_Team ')
    try:
        jugadorA = jugadores[0].text
        jugadorB = jugadores[1].text

    except:
        jugadorA = '-'
        jugadorB = '-'

    bet365_list.append([jugadorA, jugadorB])

cuotass = []
cuotaA = partidos_principales.find_elements_by_class_name('sgl-ParticipantOddsOnly80_Odds')
for cuota in range(len(cuotaA)):
    try:
        cuotass.append(cuotaA[cuota].text)
    except:
        bet365_list.pop(cuota)
        pass


print(bet365_list)
print(cuotass)


