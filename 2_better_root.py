# %%

import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()

logger.info('info message')



# %%
print(logger)
print(logger.handlers)
