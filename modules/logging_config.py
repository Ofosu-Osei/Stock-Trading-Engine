import logging
import os


def setup_logging(log_to_file=False, log_file="app.log", log_level=logging.INFO):
    """
    Configures logging with a console handler and, optionally, a file handler.
    Args:
        log_to_file (bool): If True, logs will also be written to a file.
        log_file (str): Path to the log file.
        log_level (int): Logging level for logging.INFO, logging.DEBUG ect.
    Returns:
        Logger: The configured logger instance.
    """
    # Get the root logger and clear any existing handlers
    logger = logging.getLogger()
    logger.setLevel(log_level)
    if logger.hasHandlers():
        logger.handlers.clear()

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Create a file handler
    if log_to_file:
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
