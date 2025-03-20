import configparser
config = configparser.RawConfigParser()
config.read("configs/config.ini")

class login_config:
    @staticmethod
    def get_base_url():
        url = config.get("login_config","base_url")
        return url

    @staticmethod
    def get_phone_number_location():
        location = config.get("login_config","phone_number_location")
        return location

    @staticmethod
    def get_phone_number_data():
        data = config.get("login_config", "phone_number_data")
        return data

    @staticmethod
    def get_otp_location():
        location = config.get("login_config", "otp_location")
        return location

    @staticmethod
    def get_otp_data():
        data = config.get("login_config", "otp_data")
        return data

    @staticmethod
    def get_submit_phone_number_location():
        button = config.get("login_config", "submit_phone_number_location")
        return button

    @staticmethod
    def get_otp_submit_button_location():
        button = config.get("login_config", "otp_submit_button_location")
        return button
