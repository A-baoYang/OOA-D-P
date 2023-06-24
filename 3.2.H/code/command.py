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

    def __repr__(self) -> str:
        return self.__class__.__name__
    
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def undo(self):
        pass
