import logging
import os
import glob

FILENAME = '.'.join(os.path.basename(__file__).split('.')[:-1])
EXTENSION = glob.glob('*.log')

# Create Logger
logger = logging.getLogger(__name__)
print(
    f'The efficient level of the root logger is Before setLevel()- {logger.getEffectiveLevel()}')
logger.setLevel(logging.DEBUG)
print(
    f'The efficient level of the root logger is After setLevel()- {logger.getEffectiveLevel()}')

# Create Formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Removing the file if it already has contents
if os.path.exists(EXTENSION[0]):
    if os.path.getsize(EXTENSION[0]) > 0:
        os.remove(EXTENSION[0])

# Create Handler 1
sh = logging.StreamHandler()
sh.setLevel(logging.WARN)
sh.setFormatter(formatter)

# Create handler 2

fh = logging.FileHandler(f"{FILENAME}.log")
fh.setLevel(logging.ERROR)
fh.setFormatter(formatter)

logger.info('This is info to test')
logger.debug('This is debug to test')
logger.warning('This is warning to test')
logger.addHandler(sh)
logger.warning('Sh warning')
logger.error('Sh errro')
logger.removeHandler(sh)
logger.addHandler(fh)
logger.critical('Sh critical')
logger.error('fh Error')
logging.shutdown()

a = (1, 2, 3, 4, 5)
a = list(a)
print(type(a))
