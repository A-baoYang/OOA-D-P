from typing import Any
from command import Command


class TankMoveForward(Command):
    def __init__(self, tool: Any) -> None:
        super().__init__(tool)

    def execute(self) -> str:
        return self._tool.move_forward()

    def undo(self) -> str:
        return self._tool.move_backward()


class TankMoveBackward(Command):
    def __init__(self, tool: Any) -> None:
        super().__init__(tool)

    def execute(self) -> str:
        return self._tool.move_backward()

    def undo(self) -> str:
        return self._tool.move_forward()
