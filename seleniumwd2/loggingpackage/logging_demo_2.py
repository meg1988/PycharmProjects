import logging
from loggingpackage import custom_logger as cl

class LoggingDemo2():
    log = cl.customLogger(logging.DEBUG)

    def test1(self):

        self.log.debug("Debug message")
        self.log.info("info message")
        self.log.warn("warning message")
        self.log.error("error message")
        self.log.critical("critical message")

    def test2(self):
        m2log = cl.customLogger(logging.INFO)
        m2log.debug("Debug message")
        m2log.info("info message")
        m2log.warn("warning message")
        m2log.error("error message")
        m2log.critical("critical message")

    def test3(self):
        m3log = cl.customLogger(logging.WARN)
        m3log.debug("Debug message")
        m3log.info("info message")
        m3log.warn("warning message")
        m3log.error("error message")
        m3log.critical("critical message")

demo = LoggingDemo2()
demo.test1()
demo.test2()
demo.test3()