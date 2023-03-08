# %%

import logging

# logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

logger.info('info message')



# %%
print(logger)
print(logger.handlers)