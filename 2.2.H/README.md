# [2.2.H] Card Game Framework (Template Method)

> Author: @A-baoYang (jyabaodsda)

### Object Oriented Analysis & Design (OOA/D)

![](336-2.2.H-OOD.png)

### Run Showdown
```bash
cd Showdown
python showdown.py
```

### Run UNO
```bash
cd UNO
python uno.py
```

- Logging
```bash
***    Game Start!    ***

UNO Game Rule: The very first player whose hand card cleared wins the game!

Latest Showed Card: Card({'_number': 9, '_color': 'GREEN'})
Player A:
You have these cards in Hand: {0: Card({'_number': 6, '_color': 'GREEN'}), 1: Card({'_number': 9, '_color': 'BLUE'}), 2: Card({'_number': 9, '_color': 'YELLOW'}), 3: Card({'_number': 2, '_color': 'YELLOW'})}
Choose a cards to show. Card numbers: 0
Cards: [Card({'_number': 6, '_color': 'GREEN'})] showed.
Latest Showed Card: Card({'_number': 6, '_color': 'GREEN'})
Player C:
You have these cards in Hand: {0: Card({'_number': 7, '_color': 'GREEN'}), 1: Card({'_number': 2, '_color': 'RED'}), 2: Card({'_number': 2, '_color': 'GREEN'}), 3: Card({'_number': 3, '_color': 'GREEN'})}
Choose a cards to show. Card numbers: 0
Cards: [Card({'_number': 7, '_color': 'GREEN'})] showed.
No valid card to show, draw a new card...
No valid card to show, draw a new card...
No valid card to show, draw a new card...
Latest Showed Card: Card({'_number': 7, '_color': 'GREEN'})
Player C:
You have these cards in Hand: {0: Card({'_number': 2, '_color': 'RED'}), 1: Card({'_number': 2, '_color': 'GREEN'}), 2: Card({'_number': 3, '_color': 'GREEN'})}
Choose a cards to show. Card numbers: 1
Cards: [Card({'_number': 2, '_color': 'GREEN'})] showed.
No valid card to show, draw a new card...
Latest Showed Card: Card({'_number': 2, '_color': 'GREEN'})
Player: AI #21291:

Cards: [Card({'_number': 2, '_color': 'BLUE'})] showed.
Latest Showed Card: Card({'_number': 2, '_color': 'BLUE'})
Player A:
You have these cards in Hand: {0: Card({'_number': 9, '_color': 'BLUE'}), 1: Card({'_number': 9, '_color': 'YELLOW'}), 2: Card({'_number': 2, '_color': 'YELLOW'}), 3: Card({'_number': 8, '_color': 'BLUE'})}
Choose a cards to show. Card numbers: 0
Cards: [Card({'_number': 9, '_color': 'BLUE'})] showed.
No valid card to show, draw a new card...
Latest Showed Card: Card({'_number': 9, '_color': 'BLUE'})
Player: AI #81456:

Cards: [Card({'_number': 9, '_color': 'RED'})] showed.
Latest Showed Card: Card({'_number': 9, '_color': 'RED'})
Player: AI #21291:

Cards: [Card({'_number': 5, '_color': 'YELLOW'})] showed.
The card you show isn't align the rule! Please try again
Latest Showed Card: Card({'_number': 9, '_color': 'RED'})
Player: AI #21291:

Cards: [Card({'_number': 1, '_color': 'RED'})] showed.
No valid card to show, draw a new card...
Latest Showed Card: Card({'_number': 1, '_color': 'RED'})
Player C:
You have these cards in Hand: {0: Card({'_number': 2, '_color': 'RED'}), 1: Card({'_number': 3, '_color': 'GREEN'}), 2: Card({'_number': 4, '_color': 'GREEN'})}
Choose a cards to show. Card numbers: 0
Cards: [Card({'_number': 2, '_color': 'RED'})] showed.
Latest Showed Card: Card({'_number': 2, '_color': 'RED'})
Player: AI #81456:

Cards: [Card({'_number': 1, '_color': 'YELLOW'})] showed.
The card you show isn't align the rule! Please try again
Latest Showed Card: Card({'_number': 2, '_color': 'RED'})
Player: AI #81456:

Cards: [Card({'_number': 1, '_color': 'YELLOW'})] showed.
The card you show isn't align the rule! Please try again
Latest Showed Card: Card({'_number': 2, '_color': 'RED'})
Player: AI #81456:

Cards: [Card({'_number': 3, '_color': 'BLUE'})] showed.
The card you show isn't align the rule! Please try again
Latest Showed Card: Card({'_number': 2, '_color': 'RED'})
Player: AI #81456:

Cards: [Card({'_number': 1, '_color': 'YELLOW'})] showed.
The card you show isn't align the rule! Please try again
Latest Showed Card: Card({'_number': 2, '_color': 'RED'})
Player: AI #81456:

Cards: [Card({'_number': 3, '_color': 'BLUE'})] showed.
The card you show isn't align the rule! Please try again
Latest Showed Card: Card({'_number': 2, '_color': 'RED'})
Player: AI #81456:

Cards: [Card({'_number': 3, '_color': 'BLUE'})] showed.
The card you show isn't align the rule! Please try again
Latest Showed Card: Card({'_number': 2, '_color': 'RED'})
Player: AI #81456:

Cards: [Card({'_number': 7, '_color': 'BLUE'})] showed.
The card you show isn't align the rule! Please try again
Latest Showed Card: Card({'_number': 2, '_color': 'RED'})
Player: AI #81456:

Cards: [Card({'_number': 3, '_color': 'RED'})] showed.
Latest Showed Card: Card({'_number': 3, '_color': 'RED'})
Player: AI #21291:

Cards: [Card({'_number': 5, '_color': 'YELLOW'})] showed.
The card you show isn't align the rule! Please try again
Latest Showed Card: Card({'_number': 3, '_color': 'RED'})
Player: AI #21291:

Cards: [Card({'_number': 0, '_color': 'BLUE'})] showed.
The card you show isn't align the rule! Please try again
Latest Showed Card: Card({'_number': 3, '_color': 'RED'})
Player: AI #21291:

Cards: [Card({'_number': 8, '_color': 'RED'})] showed.
Latest Showed Card: Card({'_number': 8, '_color': 'RED'})
Player A:
You have these cards in Hand: {0: Card({'_number': 9, '_color': 'YELLOW'}), 1: Card({'_number': 2, '_color': 'YELLOW'}), 2: Card({'_number': 8, '_color': 'BLUE'}), 3: Card({'_number': 6, '_color': 'BLUE'})}
Choose a cards to show. Card numbers: 2
Cards: [Card({'_number': 8, '_color': 'BLUE'})] showed.
No valid card to show, draw a new card...
Latest Showed Card: Card({'_number': 8, '_color': 'BLUE'})
Player: AI #81456:

Cards: [Card({'_number': 3, '_color': 'BLUE'})] showed.
Latest Showed Card: Card({'_number': 3, '_color': 'BLUE'})
Player: AI #21291:

Cards: [Card({'_number': 0, '_color': 'BLUE'})] showed.
Latest Showed Card: Card({'_number': 0, '_color': 'BLUE'})
Player A:
You have these cards in Hand: {0: Card({'_number': 9, '_color': 'YELLOW'}), 1: Card({'_number': 2, '_color': 'YELLOW'}), 2: Card({'_number': 6, '_color': 'BLUE'})}
Choose a cards to show. Card numbers: 2
Cards: [Card({'_number': 6, '_color': 'BLUE'})] showed.
No valid card to show, draw a new card...
Latest Showed Card: Card({'_number': 6, '_color': 'BLUE'})
Player: AI #81456:

Cards: [Card({'_number': 4, '_color': 'YELLOW'})] showed.
The card you show isn't align the rule! Please try again
Latest Showed Card: Card({'_number': 6, '_color': 'BLUE'})
Player: AI #81456:

Cards: [Card({'_number': 7, '_color': 'BLUE'})] showed.
No valid card to show, draw a new card...
No valid card to show, draw a new card...
No valid card to show, draw a new card...
No valid card to show, draw a new card...
No valid card to show, draw a new card...
Latest Showed Card: Card({'_number': 7, '_color': 'BLUE'})
Player A:
You have these cards in Hand: {0: Card({'_number': 9, '_color': 'YELLOW'}), 1: Card({'_number': 2, '_color': 'YELLOW'}), 2: Card({'_number': 7, '_color': 'RED'})}
Choose a cards to show. Card numbers: 2
Cards: [Card({'_number': 7, '_color': 'RED'})] showed.
Latest Showed Card: Card({'_number': 7, '_color': 'RED'})
Player C:
You have these cards in Hand: {0: Card({'_number': 3, '_color': 'GREEN'}), 1: Card({'_number': 4, '_color': 'GREEN'}), 2: Card({'_number': 0, '_color': 'RED'}), 3: Card({'_number': 6, '_color': 'RED'}), 4: Card({'_number': 4, '_color': 'BLUE'})}
Choose a cards to show. Card numbers: 2
Cards: [Card({'_number': 0, '_color': 'RED'})] showed.
Latest Showed Card: Card({'_number': 0, '_color': 'RED'})
Player: AI #81456:

Cards: [Card({'_number': 1, '_color': 'YELLOW'})] showed.
The card you show isn't align the rule! Please try again
Latest Showed Card: Card({'_number': 0, '_color': 'RED'})
Player: AI #81456:

Cards: [Card({'_number': 1, '_color': 'YELLOW'})] showed.
The card you show isn't align the rule! Please try again
Latest Showed Card: Card({'_number': 0, '_color': 'RED'})
Player: AI #81456:

Cards: [Card({'_number': 1, '_color': 'YELLOW'})] showed.
The card you show isn't align the rule! Please try again
Latest Showed Card: Card({'_number': 0, '_color': 'RED'})
Player: AI #81456:

Cards: [Card({'_number': 4, '_color': 'YELLOW'})] showed.
The card you show isn't align the rule! Please try again
Latest Showed Card: Card({'_number': 0, '_color': 'RED'})
Player: AI #81456:

Cards: [Card({'_number': 4, '_color': 'YELLOW'})] showed.
The card you show isn't align the rule! Please try again
Latest Showed Card: Card({'_number': 0, '_color': 'RED'})
Player: AI #81456:

Cards: [Card({'_number': 4, '_color': 'YELLOW'})] showed.
The card you show isn't align the rule! Please try again
Latest Showed Card: Card({'_number': 0, '_color': 'RED'})
Player: AI #81456:

Cards: [Card({'_number': 1, '_color': 'YELLOW'})] showed.
The card you show isn't align the rule! Please try again
Latest Showed Card: Card({'_number': 0, '_color': 'RED'})
Player: AI #81456:

Cards: [Card({'_number': 1, '_color': 'YELLOW'})] showed.
The card you show isn't align the rule! Please try again
Latest Showed Card: Card({'_number': 0, '_color': 'RED'})
Player: AI #81456:

Cards: [Card({'_number': 1, '_color': 'YELLOW'})] showed.
The card you show isn't align the rule! Please try again
Latest Showed Card: Card({'_number': 0, '_color': 'RED'})
Player: AI #81456:

Cards: [Card({'_number': 4, '_color': 'YELLOW'})] showed.
The card you show isn't align the rule! Please try again
Latest Showed Card: Card({'_number': 0, '_color': 'RED'})
Player: AI #81456:

Cards: [Card({'_number': 0, '_color': 'GREEN'})] showed.
Latest Showed Card: Card({'_number': 0, '_color': 'GREEN'})
Player: AI #21291:

Cards: [Card({'_number': 6, '_color': 'YELLOW'})] showed.
The card you show isn't align the rule! Please try again
Latest Showed Card: Card({'_number': 0, '_color': 'GREEN'})
Player: AI #21291:

Cards: [Card({'_number': 1, '_color': 'GREEN'})] showed.
No valid card to show, draw a new card...
Latest Showed Card: Card({'_number': 1, '_color': 'GREEN'})
Player C:
You have these cards in Hand: {0: Card({'_number': 3, '_color': 'GREEN'}), 1: Card({'_number': 4, '_color': 'GREEN'}), 2: Card({'_number': 6, '_color': 'RED'}), 3: Card({'_number': 4, '_color': 'BLUE'})}
Choose a cards to show. Card numbers: 0
Cards: [Card({'_number': 3, '_color': 'GREEN'})] showed.
No valid card to show, draw a new card...
No valid card to show, draw a new card...
No valid card to show, draw a new card...
Latest Showed Card: Card({'_number': 3, '_color': 'GREEN'})
Player C:
You have these cards in Hand: {0: Card({'_number': 4, '_color': 'GREEN'}), 1: Card({'_number': 6, '_color': 'RED'}), 2: Card({'_number': 4, '_color': 'BLUE'})}
Choose a cards to show. Card numbers: 0
Cards: [Card({'_number': 4, '_color': 'GREEN'})] showed.
Latest Showed Card: Card({'_number': 4, '_color': 'GREEN'})
Player: AI #81456:

Cards: [Card({'_number': 7, '_color': 'YELLOW'})] showed.
The card you show isn't align the rule! Please try again
Latest Showed Card: Card({'_number': 4, '_color': 'GREEN'})
Player: AI #81456:

Cards: [Card({'_number': 4, '_color': 'YELLOW'})] showed.
Latest Showed Card: Card({'_number': 4, '_color': 'YELLOW'})
Player: AI #21291:

Cards: [Card({'_number': 6, '_color': 'YELLOW'})] showed.
Latest Showed Card: Card({'_number': 6, '_color': 'YELLOW'})
Player A:
You have these cards in Hand: {0: Card({'_number': 9, '_color': 'YELLOW'}), 1: Card({'_number': 2, '_color': 'YELLOW'}), 2: Card({'_number': 5, '_color': 'RED'}), 3: Card({'_number': 5, '_color': 'GREEN'})}
Choose a cards to show. Card numbers: 0
Cards: [Card({'_number': 9, '_color': 'YELLOW'})] showed.
No valid card to show, draw a new card...
Latest Showed Card: Card({'_number': 9, '_color': 'YELLOW'})
Player: AI #81456:

Cards: [Card({'_number': 7, '_color': 'YELLOW'})] showed.
Latest Showed Card: Card({'_number': 7, '_color': 'YELLOW'})
Player: AI #21291:

Cards: [Card({'_number': 5, '_color': 'YELLOW'})] showed.
Latest Showed Card: Card({'_number': 5, '_color': 'YELLOW'})
Player A:
You have these cards in Hand: {0: Card({'_number': 2, '_color': 'YELLOW'}), 1: Card({'_number': 5, '_color': 'RED'}), 2: Card({'_number': 5, '_color': 'GREEN'})}
Choose a cards to show. Card numbers: 0
Cards: [Card({'_number': 2, '_color': 'YELLOW'})] showed.
Latest Showed Card: Card({'_number': 2, '_color': 'YELLOW'})
Player C:
You have these cards in Hand: {0: Card({'_number': 6, '_color': 'RED'}), 1: Card({'_number': 4, '_color': 'BLUE'}), 2: Card({'_number': 8, '_color': 'YELLOW'})}
Choose a cards to show. Card numbers: 2
Cards: [Card({'_number': 8, '_color': 'YELLOW'})] showed.
Latest Showed Card: Card({'_number': 8, '_color': 'YELLOW'})
Player: AI #81456:

Cards: [Card({'_number': 1, '_color': 'YELLOW'})] showed.
Latest Showed Card: Card({'_number': 1, '_color': 'YELLOW'})
Player: AI #21291:

Cards: [Card({'_number': 1, '_color': 'BLUE'})] showed.
***** Game Results *****
 Final Winner: Player: AI #21291 (Cleaned hand cards at round#13)
```
