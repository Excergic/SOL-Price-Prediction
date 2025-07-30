import sys
from solprice.exception import MyException
from solprice.logging import logger

try:
    logger.logging.info("This is a test log message")
    x = 1
    div = x / 1
    print(div)
except Exception as e:
    raise MyException(e, sys) from e