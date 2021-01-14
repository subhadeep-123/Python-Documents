import logging


logging.basicConfig(level=logging.DEBUG,
                    filename='first.log',
                    filemode='w',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.debug("This is debug")
