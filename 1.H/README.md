# [1.H] Showdown: Card Comparision Game

> Author: @A-baoYang (jyabaodsda)

### Object Oriented Analysis (OOA)

![](336-1.H-OOA-UML.png)


### Run 
```
$ cd code
$ python main.py
```

- Game Logging

```bash
Enter player name: p1
Enter player name: p2
****** New Game Creating ******
Players joining...There are 4 players in this game.
We're going to have 13 rounds. Good luck.

Shuffling Deck...

Now, draw cards until every players have 13 cards in hand.

Show all cards:

Player#0 - AI Player #8315 has hand cards: [Card(Rank=5, Suit=CLUB), Card(Rank=J, Suit=HEART), Card(Rank=A, Suit=DIAMOND), Card(Rank=8, Suit=HEART), Card(Rank=10, Suit=CLUB), Card(Rank=K, Suit=DIAMOND), Card(Rank=3, Suit=CLUB), Card(Rank=5, Suit=HEART), Card(Rank=8, Suit=SPADE), Card(Rank=J, Suit=DIAMOND), Card(Rank=A, Suit=HEART), Card(Rank=3, Suit=DIAMOND), Card(Rank=Q, Suit=DIAMOND)]
Player#1 - AI Player #12380 has hand cards: [Card(Rank=6, Suit=DIAMOND), Card(Rank=2, Suit=DIAMOND), Card(Rank=10, Suit=SPADE), Card(Rank=Q, Suit=SPADE), Card(Rank=2, Suit=CLUB), Card(Rank=6, Suit=SPADE), Card(Rank=K, Suit=CLUB), Card(Rank=2, Suit=HEART), Card(Rank=K, Suit=HEART), Card(Rank=4, Suit=CLUB), Card(Rank=4, Suit=HEART), Card(Rank=6, Suit=HEART), Card(Rank=10, Suit=HEART)]
Player#2 - p1 has hand cards: [Card(Rank=7, Suit=HEART), Card(Rank=2, Suit=SPADE), Card(Rank=7, Suit=SPADE), Card(Rank=5, Suit=DIAMOND), Card(Rank=J, Suit=SPADE), Card(Rank=10, Suit=DIAMOND), Card(Rank=4, Suit=DIAMOND), Card(Rank=J, Suit=CLUB), Card(Rank=A, Suit=SPADE), Card(Rank=8, Suit=DIAMOND), Card(Rank=9, Suit=DIAMOND), Card(Rank=K, Suit=SPADE), Card(Rank=3, Suit=SPADE)]
Player#3 - p2 has hand cards: [Card(Rank=5, Suit=SPADE), Card(Rank=A, Suit=CLUB), Card(Rank=6, Suit=CLUB), Card(Rank=7, Suit=CLUB), Card(Rank=9, Suit=SPADE), Card(Rank=4, Suit=SPADE), Card(Rank=Q, Suit=CLUB), Card(Rank=Q, Suit=HEART), Card(Rank=8, Suit=CLUB), Card(Rank=7, Suit=DIAMOND), Card(Rank=9, Suit=HEART), Card(Rank=9, Suit=CLUB), Card(Rank=3, Suit=HEART)]
***    Game Start!    ***


----- Round 1 -----


Hand Exchang happened at round 1, from Player: AI Player #8315 to Player: p1.
Player p1:
Do you want to exchange hand card this round? (Y/N)Y
{0: Player: AI Player #8315, 1: Player: AI Player #12380, 2: Player: p2}
Player p1:
Who do you wanna exchange with? Please enter player number: 1
Hand Exchang happened at round 1, from Player: p1 to Player: AI Player #12380.
Player p2:
Do you want to exchange hand card this round? (Y/N)Y
{0: Player: AI Player #8315, 1: Player: AI Player #12380, 2: Player: p1}
Player p2:
Who do you wanna exchange with? Please enter player number: 2
Hand Exchang happened at round 1, from Player: p2 to Player: p1.
 Show cards: 

Card(Rank=9, Suit=DIAMOND) showed.
Player#0 - AI Player #8315: Card(Rank=9, Suit=DIAMOND)

Card(Rank=K, Suit=DIAMOND) showed.
Player#1 - AI Player #12380: Card(Rank=K, Suit=DIAMOND)

{0: Card(Rank=5, Suit=SPADE), 1: Card(Rank=A, Suit=CLUB), 2: Card(Rank=6, Suit=CLUB), 3: Card(Rank=7, Suit=CLUB), 4: Card(Rank=9, Suit=SPADE), 5: Card(Rank=4, Suit=SPADE), 6: Card(Rank=Q, Suit=CLUB), 7: Card(Rank=Q, Suit=HEART), 8: Card(Rank=8, Suit=CLUB), 9: Card(Rank=7, Suit=DIAMOND), 10: Card(Rank=9, Suit=HEART), 11: Card(Rank=9, Suit=CLUB), 12: Card(Rank=3, Suit=HEART)}
Player p1:
Choose card to show. Card number: 9
Card(Rank=7, Suit=DIAMOND) showed.
Player#2 - p1: Card(Rank=7, Suit=DIAMOND)

{0: Card(Rank=6, Suit=DIAMOND), 1: Card(Rank=2, Suit=DIAMOND), 2: Card(Rank=10, Suit=SPADE), 3: Card(Rank=Q, Suit=SPADE), 4: Card(Rank=2, Suit=CLUB), 5: Card(Rank=6, Suit=SPADE), 6: Card(Rank=K, Suit=CLUB), 7: Card(Rank=2, Suit=HEART), 8: Card(Rank=K, Suit=HEART), 9: Card(Rank=4, Suit=CLUB), 10: Card(Rank=4, Suit=HEART), 11: Card(Rank=6, Suit=HEART), 12: Card(Rank=10, Suit=HEART)}
Player p2:
Choose card to show. Card number: 9
Card(Rank=4, Suit=CLUB) showed.
Player#3 - p2: Card(Rank=4, Suit=CLUB)

The winner goes to Player: AI Player #12380!

----- Round 2 -----


 Show cards: 

Card(Rank=4, Suit=DIAMOND) showed.
Player#0 - AI Player #8315: Card(Rank=4, Suit=DIAMOND)

Card(Rank=A, Suit=HEART) showed.
Player#1 - AI Player #12380: Card(Rank=A, Suit=HEART)

{0: Card(Rank=5, Suit=SPADE), 1: Card(Rank=A, Suit=CLUB), 2: Card(Rank=6, Suit=CLUB), 3: Card(Rank=7, Suit=CLUB), 4: Card(Rank=9, Suit=SPADE), 5: Card(Rank=4, Suit=SPADE), 6: Card(Rank=Q, Suit=CLUB), 7: Card(Rank=Q, Suit=HEART), 8: Card(Rank=8, Suit=CLUB), 9: Card(Rank=9, Suit=HEART), 10: Card(Rank=9, Suit=CLUB), 11: Card(Rank=3, Suit=HEART)}
Player p1:
Choose card to show. Card number: 1
Card(Rank=A, Suit=CLUB) showed.
Player#2 - p1: Card(Rank=A, Suit=CLUB)

{0: Card(Rank=6, Suit=DIAMOND), 1: Card(Rank=2, Suit=DIAMOND), 2: Card(Rank=10, Suit=SPADE), 3: Card(Rank=Q, Suit=SPADE), 4: Card(Rank=2, Suit=CLUB), 5: Card(Rank=6, Suit=SPADE), 6: Card(Rank=K, Suit=CLUB), 7: Card(Rank=2, Suit=HEART), 8: Card(Rank=K, Suit=HEART), 9: Card(Rank=4, Suit=HEART), 10: Card(Rank=6, Suit=HEART), 11: Card(Rank=10, Suit=HEART)}
Player p2:
Choose card to show. Card number: 1
Card(Rank=2, Suit=DIAMOND) showed.
Player#3 - p2: Card(Rank=2, Suit=DIAMOND)

The winner goes to Player: AI Player #12380!

----- Round 3 -----


 Show cards: 

Card(Rank=5, Suit=DIAMOND) showed.
Player#0 - AI Player #8315: Card(Rank=5, Suit=DIAMOND)

Card(Rank=5, Suit=HEART) showed.
Player#1 - AI Player #12380: Card(Rank=5, Suit=HEART)

{0: Card(Rank=5, Suit=SPADE), 1: Card(Rank=6, Suit=CLUB), 2: Card(Rank=7, Suit=CLUB), 3: Card(Rank=9, Suit=SPADE), 4: Card(Rank=4, Suit=SPADE), 5: Card(Rank=Q, Suit=CLUB), 6: Card(Rank=Q, Suit=HEART), 7: Card(Rank=8, Suit=CLUB), 8: Card(Rank=9, Suit=HEART), 9: Card(Rank=9, Suit=CLUB), 10: Card(Rank=3, Suit=HEART)}
Player p1:
Choose card to show. Card number: 3
Card(Rank=9, Suit=SPADE) showed.
Player#2 - p1: Card(Rank=9, Suit=SPADE)

{0: Card(Rank=6, Suit=DIAMOND), 1: Card(Rank=10, Suit=SPADE), 2: Card(Rank=Q, Suit=SPADE), 3: Card(Rank=2, Suit=CLUB), 4: Card(Rank=6, Suit=SPADE), 5: Card(Rank=K, Suit=CLUB), 6: Card(Rank=2, Suit=HEART), 7: Card(Rank=K, Suit=HEART), 8: Card(Rank=4, Suit=HEART), 9: Card(Rank=6, Suit=HEART), 10: Card(Rank=10, Suit=HEART)}
Player p2:
Choose card to show. Card number: 4
Card(Rank=6, Suit=SPADE) showed.
Player#3 - p2: Card(Rank=6, Suit=SPADE)

The winner goes to Player: p1!

----- Round 4 -----


 Show cards: 

Card(Rank=J, Suit=SPADE) showed.
Player#0 - AI Player #8315: Card(Rank=J, Suit=SPADE)

Card(Rank=3, Suit=CLUB) showed.
Player#1 - AI Player #12380: Card(Rank=3, Suit=CLUB)

{0: Card(Rank=5, Suit=SPADE), 1: Card(Rank=6, Suit=CLUB), 2: Card(Rank=7, Suit=CLUB), 3: Card(Rank=4, Suit=SPADE), 4: Card(Rank=Q, Suit=CLUB), 5: Card(Rank=Q, Suit=HEART), 6: Card(Rank=8, Suit=CLUB), 7: Card(Rank=9, Suit=HEART), 8: Card(Rank=9, Suit=CLUB), 9: Card(Rank=3, Suit=HEART)}
Player p1:
Choose card to show. Card number: 1
Card(Rank=6, Suit=CLUB) showed.
Player#2 - p1: Card(Rank=6, Suit=CLUB)

{0: Card(Rank=6, Suit=DIAMOND), 1: Card(Rank=10, Suit=SPADE), 2: Card(Rank=Q, Suit=SPADE), 3: Card(Rank=2, Suit=CLUB), 4: Card(Rank=K, Suit=CLUB), 5: Card(Rank=2, Suit=HEART), 6: Card(Rank=K, Suit=HEART), 7: Card(Rank=4, Suit=HEART), 8: Card(Rank=6, Suit=HEART), 9: Card(Rank=10, Suit=HEART)}
Player p2:
Choose card to show. Card number: 3
Card(Rank=2, Suit=CLUB) showed.
Player#3 - p2: Card(Rank=2, Suit=CLUB)

The winner goes to Player: AI Player #8315!

----- Round 5 -----


 Show cards: 

Card(Rank=7, Suit=HEART) showed.
Player#0 - AI Player #8315: Card(Rank=7, Suit=HEART)

Card(Rank=8, Suit=HEART) showed.
Player#1 - AI Player #12380: Card(Rank=8, Suit=HEART)

{0: Card(Rank=5, Suit=SPADE), 1: Card(Rank=7, Suit=CLUB), 2: Card(Rank=4, Suit=SPADE), 3: Card(Rank=Q, Suit=CLUB), 4: Card(Rank=Q, Suit=HEART), 5: Card(Rank=8, Suit=CLUB), 6: Card(Rank=9, Suit=HEART), 7: Card(Rank=9, Suit=CLUB), 8: Card(Rank=3, Suit=HEART)}
Player p1:
Choose card to show. Card number: 6
Card(Rank=9, Suit=HEART) showed.
Player#2 - p1: Card(Rank=9, Suit=HEART)

{0: Card(Rank=6, Suit=DIAMOND), 1: Card(Rank=10, Suit=SPADE), 2: Card(Rank=Q, Suit=SPADE), 3: Card(Rank=K, Suit=CLUB), 4: Card(Rank=2, Suit=HEART), 5: Card(Rank=K, Suit=HEART), 6: Card(Rank=4, Suit=HEART), 7: Card(Rank=6, Suit=HEART), 8: Card(Rank=10, Suit=HEART)}
Player p2:
Choose card to show. Card number: 3
Card(Rank=K, Suit=CLUB) showed.
Player#3 - p2: Card(Rank=K, Suit=CLUB)

The winner goes to Player: p1!

----- Round 6 -----


Hand Exchang happened at round 6, from Player: AI Player #12380 to Player: p2.
 Show cards: 

Card(Rank=2, Suit=SPADE) showed.
Player#0 - AI Player #8315: Card(Rank=2, Suit=SPADE)

Card(Rank=4, Suit=HEART) showed.
Player#1 - AI Player #12380: Card(Rank=4, Suit=HEART)

{0: Card(Rank=5, Suit=SPADE), 1: Card(Rank=7, Suit=CLUB), 2: Card(Rank=4, Suit=SPADE), 3: Card(Rank=Q, Suit=CLUB), 4: Card(Rank=Q, Suit=HEART), 5: Card(Rank=8, Suit=CLUB), 6: Card(Rank=9, Suit=CLUB), 7: Card(Rank=3, Suit=HEART)}
Player p1:
Choose card to show. Card number: 2
Card(Rank=4, Suit=SPADE) showed.
Player#2 - p1: Card(Rank=4, Suit=SPADE)

{0: Card(Rank=5, Suit=CLUB), 1: Card(Rank=J, Suit=HEART), 2: Card(Rank=A, Suit=DIAMOND), 3: Card(Rank=10, Suit=CLUB), 4: Card(Rank=8, Suit=SPADE), 5: Card(Rank=J, Suit=DIAMOND), 6: Card(Rank=3, Suit=DIAMOND), 7: Card(Rank=Q, Suit=DIAMOND)}
Player p2:
Choose card to show. Card number: 3
Card(Rank=10, Suit=CLUB) showed.
Player#3 - p2: Card(Rank=10, Suit=CLUB)

The winner goes to Player: p1!

----- Round 7 -----


 Show cards: 

Card(Rank=10, Suit=DIAMOND) showed.
Player#0 - AI Player #8315: Card(Rank=10, Suit=DIAMOND)

Card(Rank=10, Suit=SPADE) showed.
Player#1 - AI Player #12380: Card(Rank=10, Suit=SPADE)

{0: Card(Rank=5, Suit=SPADE), 1: Card(Rank=7, Suit=CLUB), 2: Card(Rank=Q, Suit=CLUB), 3: Card(Rank=Q, Suit=HEART), 4: Card(Rank=8, Suit=CLUB), 5: Card(Rank=9, Suit=CLUB), 6: Card(Rank=3, Suit=HEART)}
Player p1:
Choose card to show. Card number: 1
Card(Rank=7, Suit=CLUB) showed.
Player#2 - p1: Card(Rank=7, Suit=CLUB)

{0: Card(Rank=5, Suit=CLUB), 1: Card(Rank=J, Suit=HEART), 2: Card(Rank=A, Suit=DIAMOND), 3: Card(Rank=8, Suit=SPADE), 4: Card(Rank=J, Suit=DIAMOND), 5: Card(Rank=3, Suit=DIAMOND), 6: Card(Rank=Q, Suit=DIAMOND)}
Player p2:
Choose card to show. Card number: 0
Card(Rank=5, Suit=CLUB) showed.
Player#3 - p2: Card(Rank=5, Suit=CLUB)

The winner goes to Player: AI Player #12380!

----- Round 8 -----


 Show cards: 

Card(Rank=7, Suit=SPADE) showed.
Player#0 - AI Player #8315: Card(Rank=7, Suit=SPADE)

Card(Rank=K, Suit=HEART) showed.
Player#1 - AI Player #12380: Card(Rank=K, Suit=HEART)

{0: Card(Rank=5, Suit=SPADE), 1: Card(Rank=Q, Suit=CLUB), 2: Card(Rank=Q, Suit=HEART), 3: Card(Rank=8, Suit=CLUB), 4: Card(Rank=9, Suit=CLUB), 5: Card(Rank=3, Suit=HEART)}
Player p1:
Choose card to show. Card number: 0
Card(Rank=5, Suit=SPADE) showed.
Player#2 - p1: Card(Rank=5, Suit=SPADE)

{0: Card(Rank=J, Suit=HEART), 1: Card(Rank=A, Suit=DIAMOND), 2: Card(Rank=8, Suit=SPADE), 3: Card(Rank=J, Suit=DIAMOND), 4: Card(Rank=3, Suit=DIAMOND), 5: Card(Rank=Q, Suit=DIAMOND)}
Player p2:
Choose card to show. Card number: 1
Card(Rank=A, Suit=DIAMOND) showed.
Player#3 - p2: Card(Rank=A, Suit=DIAMOND)

The winner goes to Player: AI Player #8315!

----- Round 9 -----


 Show cards: 

Card(Rank=A, Suit=SPADE) showed.
Player#0 - AI Player #8315: Card(Rank=A, Suit=SPADE)

Card(Rank=6, Suit=DIAMOND) showed.
Player#1 - AI Player #12380: Card(Rank=6, Suit=DIAMOND)

{0: Card(Rank=Q, Suit=CLUB), 1: Card(Rank=Q, Suit=HEART), 2: Card(Rank=8, Suit=CLUB), 3: Card(Rank=9, Suit=CLUB), 4: Card(Rank=3, Suit=HEART)}
Player p1:
Choose card to show. Card number: 4
Card(Rank=3, Suit=HEART) showed.
Player#2 - p1: Card(Rank=3, Suit=HEART)

{0: Card(Rank=J, Suit=HEART), 1: Card(Rank=8, Suit=SPADE), 2: Card(Rank=J, Suit=DIAMOND), 3: Card(Rank=3, Suit=DIAMOND), 4: Card(Rank=Q, Suit=DIAMOND)}
Player p2:
Choose card to show. Card number: 2
Card(Rank=J, Suit=DIAMOND) showed.
Player#3 - p2: Card(Rank=J, Suit=DIAMOND)

The winner goes to Player: AI Player #8315!

----- Round 10 -----


 Show cards: 

Card(Rank=3, Suit=SPADE) showed.
Player#0 - AI Player #8315: Card(Rank=3, Suit=SPADE)

Card(Rank=6, Suit=HEART) showed.
Player#1 - AI Player #12380: Card(Rank=6, Suit=HEART)

{0: Card(Rank=Q, Suit=CLUB), 1: Card(Rank=Q, Suit=HEART), 2: Card(Rank=8, Suit=CLUB), 3: Card(Rank=9, Suit=CLUB)}
Player p1:
Choose card to show. Card number: 2
Card(Rank=8, Suit=CLUB) showed.
Player#2 - p1: Card(Rank=8, Suit=CLUB)

{0: Card(Rank=J, Suit=HEART), 1: Card(Rank=8, Suit=SPADE), 2: Card(Rank=3, Suit=DIAMOND), 3: Card(Rank=Q, Suit=DIAMOND)}
Player p2:
Choose card to show. Card number: 1
Card(Rank=8, Suit=SPADE) showed.
Player#3 - p2: Card(Rank=8, Suit=SPADE)

The winner goes to Player: p2!

----- Round 11 -----


 Show cards: 

Card(Rank=8, Suit=DIAMOND) showed.
Player#0 - AI Player #8315: Card(Rank=8, Suit=DIAMOND)

Card(Rank=2, Suit=HEART) showed.
Player#1 - AI Player #12380: Card(Rank=2, Suit=HEART)

{0: Card(Rank=Q, Suit=CLUB), 1: Card(Rank=Q, Suit=HEART), 2: Card(Rank=9, Suit=CLUB)}
Player p1:
Choose card to show. Card number: 1
Card(Rank=Q, Suit=HEART) showed.
Player#2 - p1: Card(Rank=Q, Suit=HEART)

{0: Card(Rank=J, Suit=HEART), 1: Card(Rank=3, Suit=DIAMOND), 2: Card(Rank=Q, Suit=DIAMOND)}
Player p2:
Choose card to show. Card number: 0
Card(Rank=J, Suit=HEART) showed.
Player#3 - p2: Card(Rank=J, Suit=HEART)

The winner goes to Player: p1!

----- Round 12 -----


 Show cards: 

Card(Rank=J, Suit=CLUB) showed.
Player#0 - AI Player #8315: Card(Rank=J, Suit=CLUB)

Card(Rank=10, Suit=HEART) showed.
Player#1 - AI Player #12380: Card(Rank=10, Suit=HEART)

{0: Card(Rank=Q, Suit=CLUB), 1: Card(Rank=9, Suit=CLUB)}
Player p1:
Choose card to show. Card number: 0
Card(Rank=Q, Suit=CLUB) showed.
Player#2 - p1: Card(Rank=Q, Suit=CLUB)

{0: Card(Rank=3, Suit=DIAMOND), 1: Card(Rank=Q, Suit=DIAMOND)}
Player p2:
Choose card to show. Card number: 0
Card(Rank=3, Suit=DIAMOND) showed.
Player#3 - p2: Card(Rank=3, Suit=DIAMOND)

The winner goes to Player: AI Player #12380!

----- Round 13 -----


 Show cards: 

Card(Rank=K, Suit=SPADE) showed.
Player#0 - AI Player #8315: Card(Rank=K, Suit=SPADE)

Card(Rank=Q, Suit=SPADE) showed.
Player#1 - AI Player #12380: Card(Rank=Q, Suit=SPADE)

{0: Card(Rank=9, Suit=CLUB)}
Player p1:
Choose card to show. Card number: 0
Card(Rank=9, Suit=CLUB) showed.
Player#2 - p1: Card(Rank=9, Suit=CLUB)

{0: Card(Rank=Q, Suit=DIAMOND)}
Player p2:
Choose card to show. Card number: 0
Card(Rank=Q, Suit=DIAMOND) showed.
Player#3 - p2: Card(Rank=Q, Suit=DIAMOND)

The winner goes to Player: AI Player #8315!

***** Game Results *****
 Final Winner: [Player: AI Player #8315]
 Winner gain points: 4
 Winner of each round: {1: 'AI Player #12380', 2: 'AI Player #12380', 3: 'p1', 4: 'AI Player #8315', 5: 'p1', 6: 'p1', 7: 'AI Player #12380', 8: 'AI Player #8315', 9: 'AI Player #8315', 10: 'p2', 11: 'p1', 12: 'AI Player #12380', 13: 'AI Player #8315'}
 Points of each players:

Player: AI Player #8315 | points: 4

Player: AI Player #12380 | points: 4

Player: p1 | points: 4

Player: p2 | points: 1

***   Thank you for playing!   ***
```