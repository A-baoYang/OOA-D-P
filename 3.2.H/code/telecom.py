import logging


class Telecom:
    def __init__(self) -> None:
        pass

    def connect(self) -> None:
        logging.info("The telecom has been turned on.")

    def disconnect(self) -> None:
        logging.info("The telecom has been turned off.")
