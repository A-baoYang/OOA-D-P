from individual import Individual
from matchmakingSystem import MatchmakingSystem
from matchmakingStrategy import DistanceBasedStrategy, HabitBasedStrategy
import ast
import random


def create_users():
    users = []
    flag = 1
    while flag:
        user = {
            "gender": input("Gender: (MALE or FEMALE)"),
            "age": int(input("Age: (>=18)")),
            "intro": input("Intro: (<= 200 words)"),
            "habits": input("Habits: (<= 10 keywords, split with ',')").split(","),
            "coord": input("Position: ex: [0.4, 1.4]"),
        }
        user["uid"] = random.randint(1, 10**5)
        print(f'User #{user["uid"]} registered successfully')
        user["coord"] = ast.literal_eval(user["coord"])
        users.append(Individual(**user))
        flag = int(input("Enter another user, press 1; stopping enter, press 0"))
    return users


def decide_strategy():
    strategy = input("Which matching strategy do you like to use? {distance, habit}")
    if strategy == "distance":
        return DistanceBasedStrategy()
    elif strategy == "habit":
        return HabitBasedStrategy()


def main():
    system = MatchmakingSystem(
        individuals=create_users(), matchmaking_strategy=decide_strategy()
    )
    print(f"Match Result: {system.match(reverse=False)}")


if __name__ == "__main__":
    main()
