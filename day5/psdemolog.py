import logging

fmt_str = '%(asctime)s:%(levelname)s:%(name)s:%(filename)s:%(process)s:%(message)s'
logging.basicConfig(level=logging.DEBUG, format=fmt_str, filename='access.log')


logging.debug('debug messages')
logging.info('confirmation notes')
logging.warning('warning message')
logging.error('an error information')
logging.critical('panic error')