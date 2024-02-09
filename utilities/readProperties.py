import configparser
config = configparser.RawConfigParser()

config.read("E:\\Automation Project\\HRM\\Configuration\\config.ini")

class Readconfig:

    @staticmethod
    def getURL():
        URL = config.get('Login Data', 'Url')
        return URL

    @staticmethod
    def getUsername():
        username = config.get('Login Data', 'Username')
        return username

    @staticmethod
    def getPassword():
        password  = config.get('Login Data', 'Password')
        return password