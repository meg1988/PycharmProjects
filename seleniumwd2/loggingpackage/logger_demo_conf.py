import logging
import logging.config

class LoggerDemoConfig():
    def conf(self):

        logging.config.fileConfig('logging.conf')
        logger = logging.getLogger(LoggerDemoConfig.__name__)

        logger.debug("Debug message")
        logger.info("info message")
        logger.warning("warning message")
        logger.error("error message")
        logger.critical("critical message")


demo = LoggerDemoConfig()
demo.conf()
