import configparser

config = configparser.RawConfigParser()
#config.read("/Users/daominyang/PycharmProjects/nopcommerceApp/Configurations/config.ini")
config.read("./nopcommerceApp/Configurations/config.ini")
class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password