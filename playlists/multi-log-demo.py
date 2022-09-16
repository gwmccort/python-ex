'''
demo of log to console & file with different levels
'''
import logging

logger = logging.getLogger("mylog")
formatter = logging.Formatter(
    '%(asctime)s | %(name)s |  %(levelname)s: %(message)s')
logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(formatter)

logFilePath = "my.log"
file_handler = logging.handlers.TimedRotatingFileHandler(
    filename=logFilePath, when='midnight', backupCount=30)
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)
