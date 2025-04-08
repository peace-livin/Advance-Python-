'''
logging: writing flows of execution of an application inside file is called logging
logging level:

------------

DEBUG:    prints all the statements 10 
INFO:     prints all the statements 20
WARNING:  prints all the statements 30
ERROR:    prints all the statements 40
CRITICAL: prints all the statements 50

'''

import logging
logging.basicConfig(filename='log.txt',level=logging.ERROR)
logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')  
logging.critical('critical message')