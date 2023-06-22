from typing import Any
from command import Command


class TankMoveForward(Command):
    def __init__(self, tool: Any) -> None:
        super().__init__(tool)

    def execute(self) -> None:
        self._tool.move_forward()


class TankMoveBackward(Command):
    def __init__(self, tool: Any) -> None:
        super().__init__(tool)

    def execute(self) -> None:
        self._tool.move_backward()
