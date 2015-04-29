from ConfigParser import SafeConfigParser

class ConfigOptions():
    def __init__(self, config_file_name):
        config = SafeConfigParser()
        config.read(config_file_name)
        self.__initialize_defaults()
        if config.has_section("Input Methods"):
            self.allow_text_input = config.get("Input Methods", "text") == "True"
            self.allow_voice_input = config.get("Input Methods", "text") == "True"

    def __initialize_defaults(self):
        self.allow_text_input = True
        self.allow_voice_input = True
