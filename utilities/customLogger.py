import logging

class logGen:
    @staticmethod
    def loggen():
        #Somehow the logging.basicConfig() didn't work for me in this project
        # logging.basicConfig(filename = "./nopcommerceApp/Logs/test.log",
        #                     filemode = "w",
        #                     formate = '%(asctime)s: %(levelname)s: %(message)s',
        #                     datafmt = '%m%d%Y %I:%M:%S %p'
        #                     )
        logger = logging.getLogger("Tester")
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler('./nopcommerceApp/Logs/test.log')
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger

    @staticmethod
    def loglevel(self, level):
        self.logger.setlevel(logging.level)