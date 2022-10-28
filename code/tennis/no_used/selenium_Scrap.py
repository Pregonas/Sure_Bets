
from selenium import webdriver
from code.calculadora.calculadora_apuestas import calculadora_tenis
from code.telegram import telegram_bot_sendtext

def tennis_match():
    import time
    chromedriver = "C:/Users/cpreg/OneDrive/Desktop/chromedriver/chromedriver"
    driver = webdriver.Chrome(chromedriver)
    driver.get('https://oddspedia.com/es/tenis/')

    time.sleep(5)
    partidos = driver.find_elements_by_class_name('match-data')



    for partido in partidos:
        try:
            time = partido.find_element_by_class_name('min_time').text
            jugadores = partido.find_elements_by_class_name('match-name')
            jugadorA = jugadores[0].text
            jugadorB = jugadores[1].text
            valA = partido.find_element_by_css_selector('.relative.val_1')
            casaA = valA.find_element_by_xpath('.//a').get_attribute('title')
            cuotaA = valA.find_element_by_xpath('.//a/div[1]').text
            valB = partido.find_element_by_css_selector('.relative.val_2')
            casaB = valB.find_element_by_xpath('.//a').get_attribute('title')
            cuotaB = valB.find_element_by_xpath('.//a/div[1]').text


            try:
                algoritme = calculadora_tenis(float(cuotaA), float(cuotaB))
                rentable = algoritme[0]
                x = algoritme[1]
                y = algoritme[2]
                Ganancia_x = algoritme[3]
                Ganancia_y = algoritme[4]

                if rentable == True:
                    message = 'Tennis ' + str(p) + ': (' + time + ')\nJugador A: ' + jugadorA + ' -- ' + casaA + ' : ' + str(cuotaA) + '€\nJugador B: ' \
                              + jugadorB + ' -- ' + casaB + ' : ' + str(cuotaB) + '€\nApuesta en A : ' + str(x) + '\nApuesta en B : ' \
                              + str(y) + '\nGanancia si gana A : ' + str(Ganancia_x) + '€\nGanancia si gana B : ' + str(Ganancia_y) + '€\n\n'
                    telegram_bot_sendtext(message)

            except:
                pass

        except:
            pass

    driver.close()

if __name__ == "__main__":
    tennis_match()
