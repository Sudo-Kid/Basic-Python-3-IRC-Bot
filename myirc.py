import socket

class MyIrc:

    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, server, port, channel, nick):
        self.server = server
        self.port = port
        self.channel = channel
        self.nick = nick
        return

    def getNick(self):
        return self.nick

    def getServer(self):
        return self.server
    
    def getPort(self):
        return self.port

    def decode(self, string):
        string = string.decode("utf-8")
        string = string.strip('\r\n')
        return string

    def encode(self, string):
        string = bytes(string, "utf-8")
        return string

    def ircSend(self, msg):
        msg = "PRIVMSG {0} :{1}\n".format(self.channel, msg)
        msg = self.encode(msg)
        self.irc.send(msg)
        return

    def ircMessage(self, person, msg):
        msg = "PRIVMSG {0} :{1}\n".format(person, msg)
        msg = self.encode(msg)
        self.irc.send(msg)
        return
        
    def ping(self):
        self.irc.send(bytes("PONG :pings\n", "utf-8"))
        return

    def ircConnect(self):
        user = "USER {0} {0} {0}:This is a bot\n".format(self.nick)
        nick = "NICK {0}\n".format(self.nick)
        channel = "JOIN {0}\n".format(self.channel)
        self.irc.connect((self.server, self.port))
        self.irc.send(bytes(user, "utf-8"))
        self.irc.send(bytes(nick, "utf-8"))
        self.irc.send(bytes(channel, "utf-8"))
        return

    def getMsg(self):
        ircmsg = self.irc.recv(2048)
        ircmsg = self.decode(ircmsg)
        print(ircmsg)
        return ircmsg
