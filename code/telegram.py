import requests


"""
Per obtenir els chat_id, has de copiar el següent link al navegador i enviar un missatge al bot desde telegram (del movil).
Despres actualitzes el navegador i llest.

https://api.telegram.org/bot1258791685:AAEJdT8SUkseRehqBY5RkglWNQFkMKp63WU/getUpdates?offset=0

chats_id:

- RobinBets: -407749047
- Proxims Partits: -474719636
- Partits en Directe: -444457993
- Privat: 465046322
- Tennis Directe: -466433553 

"""

def telegram_bot_sendtext(bot_message, bot_chatID):
    bot_token = '1258791685:AAEJdT8SUkseRehqBY5RkglWNQFkMKp63WU'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)

    return response.json()

