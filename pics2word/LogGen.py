import logging

logger = logging.getLogger(__name__)

def logArg(x):
    return {
        'talk': logging.DEBUG,
        'info': logging.INFO,
        'quiet': logging.NOTSET
    }.get(x, logging.NOTSET) # default = NOTSET

def set_up_logging(arg):
    
    level = logArg(arg)

    logger.setLevel(level)
    ch = logging.StreamHandler()
    ch.setLevel(level)
    formatter = logging.Formatter('%(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)