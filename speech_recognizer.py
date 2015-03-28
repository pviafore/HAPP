import pyaudio
import speech_recognition as sr
 
def get_spoken_phrases():
    r = sr.Recognizer()
    r.pause_threshold = 0.5
    r.quiet_threshold = 0.1
    r.energy_threshold = 50
    while True:
        with sr.Microphone() as source:                # use the default microphone as the audio source
            audio = r.listen(source)
        try:
            yield r.recognize(audio)
        except LookupError:
            pass
        