import logging

def log_creator():
    logger = logging.getLogger(__name__)
    if not logger.handlers:
        file_handler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
    return logger