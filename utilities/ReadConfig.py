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

class inventory_config:

    @staticmethod
    def get_url():
        url = config.get("inventory_config", "url")
        return url

    @staticmethod
    def get_add_material_button_location():
        location = config.get("inventory_config", "add_material_button_location")
        return location

    @staticmethod
    def get_new_material_button_location():
        location = config.get("inventory_config", "new_material_button_location")
        return location

    @staticmethod
    def get_input_name_location():
        location = config.get("inventory_config", "input_name_location")
        return location

    @staticmethod
    def get_uom_input_location():
        location = config.get("inventory_config", "uom_input_location")
        return location

    @staticmethod
    def get_save_create_new_location():
        location = config.get("inventory_config", "save_create_new_location")
        return location

    @staticmethod
    def get_add_new_material_cross_button():
        location = config.get("inventory_config", "add_new_material_cross_button")
        return location

    @staticmethod
    def get_select_material_cross_button():
        location = config.get("inventory_config", "select_material_cross_button")
        return location

    @staticmethod
    def get_Added_materials_location():
        location = config.get("inventory_config", "Added_materials_location")
        return location

