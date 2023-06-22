from abc import ABC, abstractmethod
from typing import Any


class Command(ABC):
    def __init__(self, tool: Any) -> None:
        self._tool = tool

    @property
    def tool(self) -> Any:
        return self._tool

    @tool.setter
    def tool(self, tool: Any) -> None:
        self._tool = tool

    @abstractmethod
    def execute(self):
        pass
