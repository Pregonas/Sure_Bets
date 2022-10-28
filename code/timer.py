from datetime import datetime
from code.telegram import telegram_bot_sendtext

def timer():
    now = datetime.now()

    print("now =", now)

    dia = now.strftime("%d/%m/%Y")
    hora = now.strftime("%H:%M")

    message = dia + ' - ' + hora
    telegram_bot_sendtext(message, '-474719636')

