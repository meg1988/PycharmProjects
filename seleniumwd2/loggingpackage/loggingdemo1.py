import logging

"""
logging.warning("This is warning message")
logging.info("Info message")
logging.error("Error message")

"""

logging.basicConfig(filename="test.log", level=logging.DEBUG)
logging.warning("This is warning message")
logging.info("Info message")
logging.error("Error message")