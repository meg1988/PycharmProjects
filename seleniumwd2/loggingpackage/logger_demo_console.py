import logging

class LoggerDemoConsole():

    def testLog(self):

        logger = logging.getLogger(LoggerDemoConsole.__name__)
        logger.setLevel(logging.DEBUG)

        chandler = logging.StreamHandler()
        chandler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        chandler.setFormatter(formatter)

        logger.addHandler(chandler)


        logger.debug("Debug message")
        logger.info("info message")
        logger.warn("warning message")
        logger.error("error message")
        logger.critical("critical message")

demo = LoggerDemoConsole()
demo.testLog()