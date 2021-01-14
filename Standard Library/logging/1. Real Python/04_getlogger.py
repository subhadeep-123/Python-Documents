import logging

logging.basicConfig(format='%(levelname)s - %(name)s - %(message)s')

logger = logging.getLogger('OpenUp')

logger.warning('This is a warning')
