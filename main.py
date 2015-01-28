#!/usr/bin/env python3

import sys
from bot import Bot

ircServer = "YOUR SERVER"
ircPort = 6667
ircChannel = "#CHANNEL NAME"
botNick = "BOT NAME HERE"

bot = Bot(ircServer, ircPort, ircChannel, botNick)
bot.ircConnect()

while True:

    message = bot.getMsg()
    message = message.lower()

    if message.find("ping :") != -1:
        bot.ping()

   if message.find(":Hello {0}".format(botNick)) != -1 or message.find(":Hello bot"):
       bot.hello()
