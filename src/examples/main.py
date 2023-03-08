import np_logging

import examples.a as a
import examples.b as b
import examples.c as c

logger = np_logging.getLogger() # root

logger.info('Starting script A')
a.run()
logger.info('Starting script B')
b.run()
logger.info('Starting script C')
c.run()