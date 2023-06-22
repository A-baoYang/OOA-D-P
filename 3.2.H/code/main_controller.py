from collections import deque


class MainController:
    def __init__(self) -> None:
        self._commands = {}
        self._redo_stack = deque()
        self._undo_stack = deque()
