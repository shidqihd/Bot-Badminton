from telethon import TelegramClient, events

#import library untuk konfigurasi
from dotenv import dotenv_values

env = dotenv_values(".env")
bot = TelegramClient("test", env['API_ID'], env['API_HASH']).start(bot_token=env['BOT_TOKEN'])

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.reply('Halo WELCOME to Bot Badminton Indonesia. Silahkan pilih cup Badminton yang dijalani timnas indonesia:\n1. Swiss Open\n2. Indonesia Open\nPilih dengan template /pilih - No Cup Badminton')

def run():
    print('Aplikasi telethon berjalan')
    bot.run_until_disconnected()

