import logging

COMMON_FORMAT = '%(levelname)s: (%(filename)s:%(lineno)d): %(message)s'

logger = logging.getLogger('common')
logger.setLevel(logging.DEBUG)


class CustomHandler(logging.Handler):
    def __init__(self, log):
        super().__init__()
        self.log = log

    def emit(self, record):
        log_entry = self.format(record)
        self.log(log_entry)


def init_logger():
    fh = logging.FileHandler('logs.txt')
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s: (%(filename)s:%(lineno)d %(threadName)s): %(message)s',
        datefmt="%m/%d/%Y %H:%M:%S"
    )
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    sh = logging.StreamHandler()
    sh.setLevel(logging.INFO)
    formatter = logging.Formatter(COMMON_FORMAT)
    sh.setFormatter(formatter)
    logger.addHandler(sh)


def add_handler(cb, level=logging.ERROR, logs_format=COMMON_FORMAT):
    ch = CustomHandler(cb)
    ch.setLevel(level)
    formatter = logging.Formatter(logs_format)
    ch.setFormatter(formatter)
    logger.addHandler(ch)


if __name__ == 'logger':
    init_logger()
