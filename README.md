

# Rock Paper Scissors Game ✊✋✌️

A simple command-line implementation of the classic Rock Paper Scissors game written in Python. Play against the computer and see who wins!

## ✨ Features

*   Play Rock Paper Scissors against a computer opponent.
*   Computer choices are randomized.
*   Keeps track of the score (User vs. Computer) throughout the session.
*   Prompts the user to play again after each round.
*   Simple and intuitive text-based interface.
*   Basic input validation for user choice.

## ⚙️ Technology

*   **Language:** Python 3.x
*   **Libraries:** Uses only the standard Python `random` library (no external dependencies needed).

## 🛠️ Setup

1.  **Download:** Save the Python script (e.g., `rps_game.py`).
2.  **Python:** Ensure you have Python 3 installed on your system. You can check by opening a terminal or command prompt and typing `python --version` or `python3 --version`. If you don't have it, download it from [python.org](https://www.python.org/).

## ▶️ How to Play

1.  **Navigate:** Open your terminal or command prompt. Navigate to the directory where you saved the Python script (e.g., `rps_game.py`).
2.  **Run the Script:** Execute the script using the Python interpreter:
    ```bash
    python rps_game.py
    ```
    *(Replace `rps_game.py` with the actual name of your file if different)*
3.  **Make Your Choice:** When prompted, type `rock`, `paper`, or `scissors` and press Enter.
    ```
    Choose rock, paper, or scissors: rock
    ```
4.  **See the Results:** The game will show your choice, the computer's random choice, the outcome (Win, Lose, or Tie), and the updated score.
    ```
    You: rock, Computer: scissors
    You win!
    Score: You 1 - Computer 0
    ```
5.  **Play Again?** The game will ask if you want to play another round.
    ```
    Play again? (y/n): y
    ```
    *   Type `y` (case-insensitive) and press Enter to play again.
    *   Type any other key (or just press Enter) to quit the game.
6.  **Exit:** The game will print "Bye!" when you choose not to play again.

## 💡 Potential Future Improvements

*   More robust input handling (e.g., accepting 'r' for 'rock', handling capitalization).
*   Option for a "Best of N" rounds mode.
*   Clearer win/loss/tie messages or ASCII art representation.
*   Track win streaks.

