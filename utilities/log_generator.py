import logging

class loggen:
    @staticmethod
    def create_log():
        logging.basicConfig(filename="logs/testcase.log", format="%(asctime)s: %(levelname)s: %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p", force=True)
        log=logging.getLogger()
        log.setLevel(logging.INFO)
        return log
