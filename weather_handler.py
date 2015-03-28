from selenium import webdriver
import pyttsx
class WeatherHandler:
    def __init__(self):
        self.driver = None
        
    def display_waff(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://waff.com")
    
    def exit_browser(self):
        self.driver.close()
        self.driver.quit()
        
    def speak_current_temperature(self):
        tempDriver = webdriver.PhantomJS(executable_path="phantomjs.exe")
        tempDriver.get("http://www.wunderground.com/cgi-bin/findweather/hdfForecast?query=35758")
        weather = tempDriver.find_element_by_id("curTemp").find_element_by_class_name("wx-value").text
        text_to_speech = pyttsx.init()
        text_to_speech.say("The current temperature is {} degrees Farenheit".format(weather))
        text_to_speech.runAndWait()
        tempDriver.close()
        tempDriver.quit()