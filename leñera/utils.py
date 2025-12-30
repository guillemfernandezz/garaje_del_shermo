import logging

def setup_geologger(log_path):
    logger = logging.getLogger('leñera')
    logger.setLevel(logging.DEBUG)
    
    f_handler = logging.FileHandler(log_path, encoding='utf-8')
    f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    f_handler.setFormatter(f_format)
    
    logger.addHandler(f_handler)
    logging.StreamHandler(f_handler)
    
    return logger