import logging


def setup_logger(name: str) -> logging.Logger:
    logger: logging.Logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Define the log format
    log_format = (
        "[%(asctime)s] [%(name)s] [%(levelname)s] [%(module)s/%(funcName)s] %(message)s"
    )
    formatter = logging.Formatter(log_format)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger
