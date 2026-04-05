import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -%(levelname)s - %(message)s')

logging.debug('Some minor code and debugging details.')
logging.info('An event happened')
logging.warning('Something could go wrong')
logging.error('An error has occurred.')
logging.critical('The program is unable to recover and will now terminate!')