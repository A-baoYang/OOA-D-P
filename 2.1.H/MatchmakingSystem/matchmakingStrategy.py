"""定義配對策略及子類別"""
from abc import ABC, abstractmethod
from typing import List

from individual import Individual


class MatchmakingStrategy(ABC):
    """類別：配對策略"""

    def __init__(self) -> None:
        pass

    @abstractmethod
    def match(
        self,
        individuals: List[Individual],
        individual: Individual,
    ) -> List[Individual]:
        """定義抽象方法：執行配對排序"""


class DistanceBasedStrategy(MatchmakingStrategy):
    """繼承：距離先決配對策略"""

    def match(
        self,
        individuals: List[Individual],
        individual: Individual,
    ) -> List[Individual]:
        """執行配對排序"""
        result = {
            _individual: _individual.coord - individual.coord
            for _individual in individuals
            if _individual.uid != individual.uid
        }

        result = dict(sorted(result.items(), key=lambda item: item[1]))

        return list(result.keys())


class HabitBasedStrategy(MatchmakingStrategy):
    """繼承：興趣交集先決配對策略"""

    def match(
        self,
        individuals: List[Individual],
        individual: Individual,
    ) -> List[Individual]:
        """執行配對排序"""
        result = {
            _individual: len(set(_individual.habits) & set(individual.habits))
            for _individual in individuals
            if _individual.uid != individual.uid
        }

        result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))

        return list(result.keys())
