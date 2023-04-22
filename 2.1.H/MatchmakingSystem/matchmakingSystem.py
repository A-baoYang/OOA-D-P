"""docstring"""
from typing import List
from individual import Individual
from matchmakingStrategy import (
    MatchmakingStrategy,
)


class MatchmakingSystem:
    """docstring"""

    def __init__(
        self, individuals: List[Individual], matchmaking_strategy: MatchmakingStrategy
    ) -> None:
        self._individuals = individuals
        self._matchmaking_strategy = matchmaking_strategy

    def add_individual(self, individuals: List[Individual]):
        """docstring"""
        self._individuals += individuals

    def change_match_strategy(self, matchmaking_strategy):
        """docstring"""
        self._matchmaking_strategy = matchmaking_strategy

    def match(self, reverse: bool) -> dict:
        """docstring"""
        return {
            _individual.uid: self._matchmaking_strategy.match(
                individuals=self._individuals, individual=_individual, reverse=reverse
            )
            for _individual in self._individuals
        }
