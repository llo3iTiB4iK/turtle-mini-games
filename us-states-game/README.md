# 🗺️ U.S. States Game

A U.S. geography quiz built with Python's `turtle` and `pandas`. Guess all 50 states by name and watch them appear on the map.

## 🧠 How It Works

- A blank U.S. map is displayed.
- You're prompted to type the name of a state.
- If correct, the state's name appears on the map at its location.
- Type `"Exit"` to stop the game and get a CSV file with the states you missed.

## 🕹️ Controls

- Use the input box to type state names (case-insensitive).
- Type `"Exit"` to quit and save progress.

## 📁 Files

- `main.py` — Main game logic
- `50_states.csv` — State names and coordinates
- `blank_states_img.gif` — Background image for the map
- `missing_states.csv` — (Generated) List of states not guessed, saved on exit

## ▶️ How to Run

```bash
python main.py
```

## 🐍 Requirements

- Python 3
- `pandas`
- `turtle` (standard library)

## 📝 Example CSV Format

`50_states.csv`:

| state     | x    | y    |
|-----------|------|------|
| Alabama   | 139  | -77  |
| Alaska    | -230 | -210 |
| ...       | ...  | ...  |

---

✅ A fun way to practice U.S. geography and work with CSV files, GUI input, and coordinate-based turtle graphics.