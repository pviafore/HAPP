import requests
import pyttsx
import ConfigParser
from selenium import webdriver
class WeatherHandler:
    def __init__(self):
        self.driver = None
        self.config = ConfigParser.ConfigParser()
        self.config.read("config/wunderground.config")

    def display_waff(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://waff.com")

    def exit_browser(self):
        self.driver.close()
        self.driver.quit()

    def get_config_data(self):
        return [self.config.get("Weather Underground", config) for config in ["key", "state", "city"]]

    def get_weather(self):
        config_data = self.get_config_data()
        r = requests.get("http://api.wunderground.com/api/{}/conditions/q/{}/{}.json".format(*config_data))
        return r.json()["current_observation"]['temp_f']

    def speak_current_temperature(self):
        text_to_speech = pyttsx.init()
        text_to_speech.say("The current temperature is {} degrees Farenheit".format(self.get_weather()))
        text_to_speech.runAndWait()
