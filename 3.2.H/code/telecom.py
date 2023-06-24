import logging


class Telecom:
    def __init__(self) -> None:
        pass

    def connect(self) -> str:
        _status_msg = "The telecom has been turned on."
        logging.info(_status_msg)
        return _status_msg

    def disconnect(self) -> str:
        _status_msg = "The telecom has been turned off."
        logging.info(_status_msg)
        return _status_msg
