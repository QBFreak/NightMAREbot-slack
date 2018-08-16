class Command(object):
    def __init__(self):
        self.version = 0.5
        self.commands = {
            "jump" : self.jump,
            "ping" : self.ping,
            "quit" : self.quit,
            "reload" : self.reload,
            "help" : self.help
        }

    def handle_command(self, user, command):
        response = "<@" + user + ">: "

        if command in self.commands:
            response += self.commands[command]()
        else:
            response += "Sorry I don't understand the command: " + command + ". " + self.help()

        return response

    def jump(self):
        return "How high?"

    def ping(self):
        return "Pong!"

    def reload(self):
        return "Command handler version {0} loaded".format(self.version)

    def quit(self):
        exit()

    def help(self):
        response = "Currently I support the following commands:\r\n"

        for command in self.commands:
            response += command + "\r\n"

        return response
