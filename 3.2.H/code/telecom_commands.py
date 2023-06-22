from typing import Any
from command import Command


class TelecomConnect(Command):
    def __init__(self, tool: Any) -> None:
        super().__init__(tool)

    def execute(self) -> None:
        self._tool.connect()


class TelecomDisconnect(Command):
    def __init__(self, tool: Any) -> None:
        super().__init__(tool)

    def execute(self) -> None:
        self._tool.disconnect()
