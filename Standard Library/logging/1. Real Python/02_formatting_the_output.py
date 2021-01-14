import logging
# %(asctime)s adds the time of creation of the LogRecord.
logging.basicConfig(
    format='%(asctime)s - %(process)d - %(levelname)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S')
NAME = "Subhadeep banerjee"
logging.warning(f"{NAME} logged out.")
