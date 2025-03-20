import configparser
config = configparser.RawConfigParser()
config.read("/configs/config.ini")

class login:
    @staticmethod
    def get_base_url():
        url = config.get("login","base_url")
        return url