"""定義交友配對系統屬性及方法"""
from typing import List

from individual import Individual
from matchmakingStrategy import MatchmakingStrategy


class MatchmakingSystem:
    """類別：交友配對系統"""

    def __init__(
        self, individuals: List[Individual], matchmaking_strategy: MatchmakingStrategy
    ) -> None:
        self._individuals = individuals
        self._matchmaking_strategy = matchmaking_strategy

    def add_individual(self, individuals: List[Individual]):
        """新增待配對用戶"""
        self._individuals += individuals

    def change_match_strategy(self, matchmaking_strategy):
        """改變排序策略"""
        self._matchmaking_strategy = matchmaking_strategy

    def match(self) -> dict:
        """執行配對排序"""
        return {
            _individual: self._matchmaking_strategy.match(
                individuals=self._individuals, individual=_individual
            )
            for _individual in self._individuals
        }
