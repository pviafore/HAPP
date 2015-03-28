from speech_recognizer import get_spoken_phrases
from music_player import MusicPlayer
from weather_handler import WeatherHandler

musicPlayer = MusicPlayer()
weatherHandler = WeatherHandler()

class Command():
    def __init__(self, command, context=None):
        self.command = command
        self.context= context if context else {}
        
musicCommands = {
                 "next song" : Command(lambda: musicPlayer.next()),
                 "stop music" : Command(lambda: musicPlayer.exit())
                }
                
weatherCommands = {
                    "all clear" : Command(lambda: weatherHandler.exit_browser())
                  }
rootCommands = {
                   "start music" : Command(lambda: musicPlayer.play_music(), musicCommands ),
                   "tornado warning" : Command(lambda: weatherHandler.display_waff(), weatherCommands ),
                   "whats the temp" : Command(lambda: weatherHandler.speak_current_temperature())
               }

contextStack = []
context = rootCommands

def process_command(command):
    print "Matched command: {}".format(phrase)
    command.command()
    global context
    if command.context:
        contextStack.append(context)
        context = command.context
    if command == 'stop music':
        context = contextStack.pop()
    
print "Launching HAPP, talk to get going!"

for phrase in get_spoken_phrases():
    print phrase
    for expectedPhrase, command in context.items():
        if phrase == expectedPhrase:
            process_command(command)
            break
