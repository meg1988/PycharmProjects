import logging

logging.basicConfig(level=logging.DEBUG , format='%(asctime)s: %(levelname)s : %(message)s', datefmt='%m/%d/%Y %H:%M:%S %p')
logging.warning("This is warning message")
logging.info("Info message")
logging.error("Error message")