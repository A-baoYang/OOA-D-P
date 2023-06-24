import logging


class Tank:
    def __init__(self) -> None:
        pass

    def move_forward(self) -> str:
        _status_msg = "The tank has moved forward."
        logging.info(_status_msg)
        return _status_msg

    def move_backward(self) -> str:
        _status_msg = "The tank has moved backward."
        logging.info(_status_msg)
        return _status_msg
