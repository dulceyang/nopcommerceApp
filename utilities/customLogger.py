import logging

class logGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="/Users/daominyang/PycharmProjects/nopcommerceApp/Logs/testlog.log",
                            filemode="w",
                            formate = '%(asctime)s: %(levelname)s: %(message)s',
                            datafmt = '%m%d%Y %I:%M:%S %p'
                            )
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

    @staticmethod
    def loglevel(self, level):
        self.logger.setlevel(logging.level)