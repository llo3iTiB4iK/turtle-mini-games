# 🐢 Turtle Mini Games Collection

A set of mini games built using Python's built-in `turtle` graphics library. Great for learning basic game logic, OOP principles, and working with graphics in Python.

## 🎮 Included Games

### 1. 🐍 Snake Game

Classic snake game with food, score tracking, and high score saving.

- Arrow keys to control the snake
- Score increases as you eat food
- Game resets when hitting walls or yourself
- High score is saved in `data.txt`

➡️ [View Snake Game README](./snake-game/README.md)

---

### 2. 🐸 Turtle Crossing

Help the turtle cross the road while avoiding oncoming traffic.

- Press ↑ to move the turtle forward
- Cars are randomly generated and increase in speed with each level
- Game ends when the turtle collides with a car

➡️ [View Turtle Crossing README](./turtle-crossing/README.md)

---

### 3. 🗺️ U.S. States Game

A geography quiz to name all 50 U.S. states.

- A blank U.S. map is shown
- Type in state names to label them on the map
- Type `"Exit"` to save a CSV of unguessed states

➡️ [View U.S. States Game README](./us-states-game/README.md)

---

### 4. 🏓 Pong Game

Classic two-player Pong game.

- W/S to move the left paddle
- Up/Down arrows for the right paddle
- Ball bounces off walls and paddles
- Points are scored when a player misses

➡️ [View Pong Game README](./pong-game/README.md)

---

## 🐍 Requirements

- Python 3
- `pandas` (only needed for the U.S. States Game)
- No additional packages required (uses standard `turtle`)

## 📦 Folder Structure

```
turtle-mini-games/
├── snake_game/
│   ├── main.py
│   ├── snake.py
│   ├── food.py
│   ├── scoreboard.py
│   └── data.txt
│
├── turtle_crossing/
│   ├── main.py
│   ├── player.py
│   ├── car_manager.py
│   └── scoreboard.py
│
├── us_states_game/
│   ├── main.py
│   ├── 50_states.csv
│   └── blank_states_img.gif
│
├── pong_game/
│   ├── main.py
│   ├── paddle.py
│   ├── ball.py
│   └── scoreboard.py
│
└── README.md
```

## 🚀 Getting Started

Navigate to any folder and run:

```bash
python main.py
```

Enjoy the games and feel free to customize, improve, or expand them! 🧠🎨🕹️