import logging


class Logger:

    logger = None

    def __init__(self, name=None, filename=None):
        self.logger = logging.getLogger("[LOGGER]" if name==None else name)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(name)s :: %(message)s')
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        if filename:
            file_handler = logging.FileHandler(filename)
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def log(self, *args):
        args = map(str, args)
        msg = " :: ".join(args)
        self.logger.info(str(msg))
