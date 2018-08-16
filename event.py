# import command

class Event:
    def __init__(self, bot):
        self.bot = bot
        self.command_loaded = False
        self.command = None
        try:
            import bot_command
            self.command_loaded = True
            self.command = bot_command.Command()
        except:
            print("ERROR loading command module!")
            self.command = None

    def wait_for_event(self):
        events = self.bot.slack_client.rtm_read()

        if events and len(events) > 0:
            for event in events:
                if 'user' in event:
                    # No endless loops, PLEASE
                    if event['user'] != self.bot.bot_id:
                        self.parse_event(event)
                else:
                    # Hey, wasn't from anyone, so no need to make sure it wasn't from ME
                    self.parse_event(event)

    def parse_event(self, event):
        if event and 'text' in event:
            if self.bot.bot_id in event['text']:
                self.handle_event(event['user'], event['text'].split(self.bot.bot_id)[1].strip().lower(), event['channel'])
            elif event['text'][0] == self.bot.bot_cmdchar:
                self.handle_event(event['user'], event['text'].split(self.bot.bot_cmdchar)[1].strip().lower(), event['channel'])

    def handle_event(self, user, cmd, channel):
        if cmd and channel:
            print "Received command: " + cmd + " in channel: " + channel + " from user: " + user
            if cmd == "reload":
                # Reload and reinstantiate the Command object
                # TODO: Flip this inside out, now that we're importing before reloading
                if self.command_loaded:
                    try:
                        self.command = None
                        # We want to reload it, but it's out of scope,
                        # So import it first
                        import bot_command
                        reload(bot_command)
                        self.command_loaded = True
                        self.command = bot_command.Command()
                    except:
                        print("Failed to reload Command module.")
                        self.command = None
                else:
                    try:
                        import bot_command
                        self.command_loaded = True
                        self.command = bot_command.Command()
                    except:
                        print("Failed to load Command module.")
                        self.command = None
            if self.command:
                response = self.command.handle_command(user, cmd)
                self.bot.slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)
            else:
                print("ERROR: command module not loaded!")
                self.bot.slack_client.api_call("chat.postMessage", channel=channel, text="ERROR: Command module not loaded! Try `!reload`", as_user=True)
