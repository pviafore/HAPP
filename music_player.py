from selenium import webdriver

class MusicPlayer:
    def __init__(self):
        self.driver = None
        
    def play_music(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.pandora.com/station/play/2581296460843162042")
        
    def exit(self):
        self.driver.close()
        self.driver.quit()
        
    def next(self):
        self.driver.find_element_by_class_name("skipButton").find_element_by_tag_name("a").click()