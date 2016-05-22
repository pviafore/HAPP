from speech_recognizer import load_speech_recognizer
from music_player import MusicPlayer
from weather_handler import WeatherHandler
from command_queue import *
from text_input import load_text_input
from configuration_options import ConfigOptions
import sys
musicPlayer = MusicPlayer()
weatherHandler = WeatherHandler()

class Action():
    def __init__(self, action, context=None):
        self.action = action
        self.context= context if context else {}

    def perform(self):
        self.action()


musicCommands = {
                 "next song" : Action(lambda: musicPlayer.next()),
                 "stop music" : Action(lambda: musicPlayer.exit())
                }

weatherCommands = {
                    "all clear" : Action(lambda: weatherHandler.exit_browser())
                  }
rootCommands = {
                   "start music" : Action(lambda: musicPlayer.play_music(), musicCommands ),
                   "tornado warning" : Action(lambda: weatherHandler.display_waff(), weatherCommands ),
  "what's the temp" : Action(lambda: weatherHandler.speak_current_temperature())
               }

contextStack = []
context = rootCommands

def process_action(action):
    action.perform()
    global context
    if action.context:
        contextStack.append(context)
        context = action.context

def main_run_loop(options):
    print "Launching HAPP, talk to get going!"
    global context
    load_speech_recognizer(get_command_queue())
    load_text_input(get_command_queue())
    for command in get_input_commands():
        print "Recognized: " + command
        if command == "exit":
            break
        for expectedCommand, action in context.items():
            if command == 'stop music':
                context = contextStack[-1]
                contextStack.pop()
            if command == expectedCommand:
                print "Matched command: {}".format(command)
                process_action(action)
                break


if __name__ == "__main__":
    config_file_name = sys.argv[1] if len(sys.argv) > 1 else "default.ini"
    main_run_loop(ConfigOptions(config_file_name))
