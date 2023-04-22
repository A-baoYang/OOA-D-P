"""程式啟動點"""
import random

from individual import Individual
from coordinate import Coord
from matchmakingStrategy import DistanceBasedStrategy, HabitBasedStrategy
from matchmakingSystem import MatchmakingSystem
from reverse import Reverse


def create_users():
    """從 terminal 創建用戶"""
    users = []
    flag = 1
    while flag:
        user = {
            "gender": input("Gender: (MALE or FEMALE)"),
            "age": int(input("Age: (>=18)")),
            "intro": input("Intro: (<= 200 words)"),
            "habits": input("Habits: (<= 10 keywords, split with ',')").split(","),
        }
        coord = {
            "x": float(input("X-axis (float): ")),
            "y": float(input("Y-axis (float): ")),
        }
        user["uid"] = random.randint(1, 10**5)
        user["coord"] = Coord(**coord)
        user = Individual(**user)
        users.append(user)
        flag = 1 if input("Enter another user? (Y/N)") == "Y" else 0
    return users


def decide_strategy():
    """從 terminal 決定推薦排序策略"""
    strategy = input("Which matching strategy do you like to use? {distance, habit}")
    reverse = input("Do you want to make reverse recommandations? (Y/N)")
    if strategy == "habit":
        strategy_cls = HabitBasedStrategy()
    elif strategy == "distance":
        strategy_cls = DistanceBasedStrategy()
    else:
        print("Strategy class not initiated, using default strategy: DistanceBased")
        strategy_cls = DistanceBasedStrategy()
    if reverse:
        return Reverse(strategy_cls)
    return strategy_cls


def main():
    """執行交友系統推薦排序"""
    system = MatchmakingSystem(
        individuals=create_users(), matchmaking_strategy=decide_strategy()
    )
    print(f"Match Result: {system.match()}")


if __name__ == "__main__":
    main()
