from typing import Any
from command import Command


class TelecomConnect(Command):
    def __init__(self, tool: Any) -> None:
        super().__init__(tool)

    def execute(self) -> str:
        return self._tool.connect()
    
    def undo(self) -> str:
        return self._tool.disconnect()


class TelecomDisconnect(Command):
    def __init__(self, tool: Any) -> None:
        super().__init__(tool)

    def execute(self) -> str:
        return self._tool.disconnect()

    def undo(self) -> str:
        return self._tool.connect()
