# [1.H] Showdown

> Author: @A-baoYang (jyabaodsda)

### Object Oriented Analysis (OOA)

![](336-1.H-OOA-UML.png)


### Run 
```
$ cd showdown
$ python main.py
```

- Game Logging

```bash
****** New Game Creating ******

Players joining...
There are 4 players in this game.

We're going to have 13 rounds. Good luck.

Shuffling Deck...

Now, draw cards until every players have 13 cards in hand.

Show all cards:

Player#0 - HHH has hand cards: [Card(Rank=J, Suit=DIAMOND), Card(Rank=K, Suit=HEART), Card(Rank=A, Suit=CLUB), Card(Rank=Q, Suit=DIAMOND), Card(Rank=6, Suit=HEART), Card(Rank=5, Suit=HEART), Card(Rank=8, Suit=DIAMOND), Card(Rank=6, Suit=DIAMOND), Card(Rank=4, Suit=CLUB), Card(Rank=4, Suit=DIAMOND), Card(Rank=8, Suit=CLUB), Card(Rank=5, Suit=CLUB), Card(Rank=10, Suit=SPADE)]
Player#1 - CCC has hand cards: [Card(Rank=10, Suit=HEART), Card(Rank=10, Suit=DIAMOND), Card(Rank=5, Suit=SPADE), Card(Rank=2, Suit=CLUB), Card(Rank=K, Suit=DIAMOND), Card(Rank=9, Suit=SPADE), Card(Rank=A, Suit=SPADE), Card(Rank=J, Suit=SPADE), Card(Rank=9, Suit=HEART), Card(Rank=9, Suit=CLUB), Card(Rank=J, Suit=HEART), Card(Rank=2, Suit=HEART), Card(Rank=4, Suit=SPADE)]
Player#2 - OJOJI has hand cards: [Card(Rank=3, Suit=CLUB), Card(Rank=7, Suit=SPADE), Card(Rank=7, Suit=CLUB), Card(Rank=Q, Suit=HEART), Card(Rank=J, Suit=CLUB), Card(Rank=3, Suit=HEART), Card(Rank=A, Suit=DIAMOND), Card(Rank=2, Suit=DIAMOND), Card(Rank=3, Suit=DIAMOND), Card(Rank=8, Suit=HEART), Card(Rank=8, Suit=SPADE), Card(Rank=Q, Suit=CLUB), Card(Rank=A, Suit=HEART)]
Player#3 - QJWODJPOWJ has hand cards: [Card(Rank=K, Suit=SPADE), Card(Rank=3, Suit=SPADE), Card(Rank=7, Suit=DIAMOND), Card(Rank=4, Suit=HEART), Card(Rank=6, Suit=CLUB), Card(Rank=9, Suit=DIAMOND), Card(Rank=K, Suit=CLUB), Card(Rank=6, Suit=SPADE), Card(Rank=7, Suit=HEART), Card(Rank=5, Suit=DIAMOND), Card(Rank=Q, Suit=SPADE), Card(Rank=2, Suit=SPADE), Card(Rank=10, Suit=CLUB)]
***    Game Start!    ***


----- Round 1 -----


Hand Exchang happened at round 1, from Player: HHH to Player: CCC.
Hand Exchang happened at round 1, from Player: OJOJI to Player: HHH.
 Show cards: 

Player#0 - HHH: Card(Rank=7, Suit=SPADE)

Player#1 - CCC: Card(Rank=6, Suit=DIAMOND)

Player#2 - OJOJI: Card(Rank=5, Suit=SPADE)

Player#3 - QJWODJPOWJ: Card(Rank=9, Suit=DIAMOND)

The winner goes to Player: HHH!

----- Round 2 -----


 Show cards: 

Player#0 - HHH: Card(Rank=3, Suit=CLUB)

Player#1 - CCC: Card(Rank=5, Suit=HEART)

Player#2 - OJOJI: Card(Rank=2, Suit=HEART)

Player#3 - QJWODJPOWJ: Card(Rank=K, Suit=CLUB)

The winner goes to Player: CCC!

----- Round 3 -----


Hand Exchang happened at round 3, from Player: QJWODJPOWJ to Player: CCC.
 Show cards: 

Player#0 - HHH: Card(Rank=Q, Suit=CLUB)

Player#1 - CCC: Card(Rank=7, Suit=DIAMOND)

Player#2 - OJOJI: Card(Rank=J, Suit=SPADE)

Player#3 - QJWODJPOWJ: Card(Rank=4, Suit=DIAMOND)

The winner goes to Player: OJOJI!

----- Round 4 -----


 Show cards: 

Player#0 - HHH: Card(Rank=8, Suit=SPADE)

Player#1 - CCC: Card(Rank=2, Suit=SPADE)

Player#2 - OJOJI: Card(Rank=J, Suit=HEART)

Player#3 - QJWODJPOWJ: Card(Rank=8, Suit=DIAMOND)

The winner goes to Player: HHH!

----- Round 5 -----


 Show cards: 

Player#0 - HHH: Card(Rank=2, Suit=DIAMOND)

Player#1 - CCC: Card(Rank=Q, Suit=SPADE)

Player#2 - OJOJI: Card(Rank=10, Suit=DIAMOND)

Player#3 - QJWODJPOWJ: Card(Rank=Q, Suit=DIAMOND)

The winner goes to Player: CCC!

----- Round 6 -----


Hand Exchang happened at round 6, from Player: CCC to Player: QJWODJPOWJ.
 Show cards: 

Player#0 - HHH: Card(Rank=3, Suit=HEART)

Player#1 - CCC: Card(Rank=K, Suit=HEART)

Player#2 - OJOJI: Card(Rank=9, Suit=SPADE)

Player#3 - QJWODJPOWJ: Card(Rank=7, Suit=HEART)

The winner goes to Player: OJOJI!

----- Round 7 -----


 Show cards: 

Player#0 - HHH: Card(Rank=A, Suit=HEART)

Player#1 - CCC: Card(Rank=4, Suit=CLUB)

Player#2 - OJOJI: Card(Rank=9, Suit=CLUB)

Player#3 - QJWODJPOWJ: Card(Rank=K, Suit=SPADE)

The winner goes to Player: QJWODJPOWJ!

----- Round 8 -----


 Show cards: 

Player#0 - HHH: Card(Rank=7, Suit=CLUB)

Player#1 - CCC: Card(Rank=5, Suit=CLUB)

Player#2 - OJOJI: Card(Rank=4, Suit=SPADE)

Player#3 - QJWODJPOWJ: Card(Rank=5, Suit=DIAMOND)

The winner goes to Player: OJOJI!

----- Round 9 -----


 Show cards: 

Player#0 - HHH: Card(Rank=8, Suit=HEART)

Player#1 - CCC: Card(Rank=J, Suit=DIAMOND)

Player#2 - OJOJI: Card(Rank=K, Suit=DIAMOND)

Player#3 - QJWODJPOWJ: Card(Rank=6, Suit=SPADE)

The winner goes to Player: QJWODJPOWJ!

----- Round 10 -----


 Show cards: 

Player#0 - HHH: Card(Rank=A, Suit=DIAMOND)

Player#1 - CCC: Card(Rank=10, Suit=SPADE)

Player#2 - OJOJI: Card(Rank=10, Suit=HEART)

Player#3 - QJWODJPOWJ: Card(Rank=3, Suit=SPADE)

The winner goes to Player: CCC!

----- Round 11 -----


 Show cards: 

Player#0 - HHH: Card(Rank=3, Suit=DIAMOND)

Player#1 - CCC: Card(Rank=6, Suit=HEART)

Player#2 - OJOJI: Card(Rank=9, Suit=HEART)

Player#3 - QJWODJPOWJ: Card(Rank=10, Suit=CLUB)

The winner goes to Player: OJOJI!

----- Round 12 -----


 Show cards: 

Player#0 - HHH: Card(Rank=Q, Suit=HEART)

Player#1 - CCC: Card(Rank=8, Suit=CLUB)

Player#2 - OJOJI: Card(Rank=A, Suit=SPADE)

Player#3 - QJWODJPOWJ: Card(Rank=6, Suit=CLUB)

The winner goes to Player: OJOJI!

----- Round 13 -----


 Show cards: 

Player#0 - HHH: Card(Rank=J, Suit=CLUB)

Player#1 - CCC: Card(Rank=A, Suit=CLUB)

Player#2 - OJOJI: Card(Rank=2, Suit=CLUB)

Player#3 - QJWODJPOWJ: Card(Rank=4, Suit=HEART)

The winner goes to Player: QJWODJPOWJ!

***** Game Results *****

 Final Winner: Player: OJOJI
 Winner gain points: 5

 Winner of each round: {1: 'HHH', 2: 'CCC', 3: 'OJOJI', 4: 'HHH', 5: 'CCC', 6: 'OJOJI', 7: 'QJWODJPOWJ', 8: 'OJOJI', 9: 'QJWODJPOWJ', 10: 'CCC', 11: 'OJOJI', 12: 'OJOJI', 13: 'QJWODJPOWJ'}

 Points of each players:

Player: HHH | points: 2

Player: CCC | points: 3

Player: OJOJI | points: 5

Player: QJWODJPOWJ | points: 3

***   Thank you for playing!   ***
```