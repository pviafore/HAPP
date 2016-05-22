import pyaudio
import speech_recognition as sr
from threading import Thread

def load_speech_recognizer(queue):
    def get_user_input():
        for phrase in get_spoken_phrases():
            queue.put(phrase)
    thread = Thread(target=get_user_input)
    thread.daemon = True
    thread.start()
    return thread


def get_spoken_phrases():
    r = sr.Recognizer()
    r.pause_threshold = 0.5
    r.quiet_threshold = 0.1
    r.energy_threshold = 500
    print "Listening for phrase"
    while True:
        try:
            with sr.Microphone() as source:                # use the default microphone as the audio source
                audio = r.listen(source)
            print "Audio data captured"
            yield r.recognize_google(audio)
        except LookupError:
            pass
        except Exception as e:
            print e
