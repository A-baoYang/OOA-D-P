# [2.2.H] 

> Author: @A-baoYang (jyabaodsda)

### Object Oriented Analysis & Design (OOA/D)

![](336-2.2.H-OOAD.png)

### Run 
```bash
cd MatchmakingSystem
python main.py
```

- Logging
```bash
Gender: (MALE or FEMALE)MALE
Age: (>=18)19
Intro: (<= 200 words)Hi
Habits: (<= 10 keywords, split with ',')跳舞,rap
Position: ex: [0.4, 1.4][4.5,1.9]
User #5467 registered successfully
Enter another user, press 1; stopping enter, press 01
Gender: (MALE or FEMALE)MALE
Age: (>=18)19
Intro: (<= 200 words)Hi
Habits: (<= 10 keywords, split with ',')rap,看書
Position: ex: [0.4, 1.4][1.3, 6.7]
User #25562 registered successfully
Enter another user, press 1; stopping enter, press 01
Gender: (MALE or FEMALE)FEMALE
Age: (>=18)19
Intro: (<= 200 words)Hi
Habits: (<= 10 keywords, split with ',')跑步,跳舞,rap
Position: ex: [0.4, 1.4][1.4, 6.7]
User #67339 registered successfully
Enter another user, press 1; stopping enter, press 00
Which matching strategy do you like to use? {distance, habit}habit
Match Result: {5467: 67339, 25562: 5467, 67339: 5467}
```