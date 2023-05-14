"""定義裝飾器類別屬性及方法"""
from typing import List

from individual import Individual
from matchmakingStrategy import MatchmakingStrategy


class Reverse(MatchmakingStrategy):
    """裝飾器類別：對原先的排序結果轉為反序再輸出"""

    def __init__(self, match_stategy: MatchmakingStrategy) -> None:
        super().__init__()

        self._match_stategy = match_stategy

    def match(
        self, individuals: List[Individual], individual: Individual
    ) -> List[Individual]:
        """執行反向排序"""
        result = self._match_stategy.match(individuals, individual)
        return result[::-1]
