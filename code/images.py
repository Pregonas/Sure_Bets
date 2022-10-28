from code.telegram import telegram_bot_sendtext

message = "https://cdn.oddspedia.com/images/bookmakers/dark/marathonbet.png"

filename = message.split('/')[-1].split('.')[0]

print(filename)