"""docstring"""
import math
from abc import ABC, abstractmethod
from typing import List

from individual import Individual


class MatchmakingStrategy(ABC):
    """docstring"""

    def __init__(self) -> None:
        pass

    @abstractmethod
    def match(
        self,
        individuals: List[Individual],
        individual: Individual,
        reverse: bool = False,
    ) -> Individual:
        """docstring"""
        pass


class DistanceBasedStrategy(MatchmakingStrategy):
    """docstring"""

    def __init__(self) -> None:
        super().__init__()

    def match(
        self,
        individuals: List[Individual],
        individual: Individual,
        reverse: bool = False,
    ) -> Individual:
        result = {
            _individual: math.sqrt(
                sum([(x - y) ** 2 for x, y in zip(_individual.coord, individual.coord)])
            )
            for _individual in individuals
            if _individual.uid != individual.uid
        }

        if reverse:
            result = dict(
                sorted(result.items(), key=lambda item: item[1], reverse=True)
            )
        else:
            result = dict(sorted(result.items(), key=lambda item: item[1]))

        return list(result.keys())[0].uid


class HabitBasedStrategy(MatchmakingStrategy):
    """docstring"""

    def __init__(self) -> None:
        super().__init__()

    def match(
        self,
        individuals: List[Individual],
        individual: Individual,
        reverse: bool = False,
    ) -> Individual:
        result = {
            _individual: len(set(_individual.habits) & set(individual.habits))
            for _individual in individuals
            if _individual.uid != individual.uid
        }

        if reverse:
            result = dict(sorted(result.items(), key=lambda item: item[1]))
        else:
            result = dict(
                sorted(result.items(), key=lambda item: item[1], reverse=True)
            )

        return list(result.keys())[0].uid
