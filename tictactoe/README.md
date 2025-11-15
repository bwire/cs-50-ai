# Tic Tac Toe with AI

A Python implementation of Tic Tac Toe featuring an unbeatable AI opponent using the minimax algorithm.

## Features

- 🎮 Interactive GUI built with Pygame
- 🤖 Unbeatable AI opponent using minimax algorithm
- 👥 Human vs AI gameplay
- 🎯 Player choice (X or O)
- 🔄 Play again functionality

## Requirements

- Python 3.7+
- Pygame 2.6.1+

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd tictactoe
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## How to Run

```bash
python3 runner.py
```

## How to Play

1. **Choose your player**: Click "Play as X" or "Play as O" when the game starts
2. **Make your move**: Click on an empty square to place your mark
3. **AI turn**: The computer will automatically make its move using the minimax algorithm
4. **Game over**: The game ends when someone wins or the board is full
5. **Play again**: Click "Play Again" to start a new game

## Game Rules

- X always goes first
- Players take turns placing their marks on a 3x3 grid
- Win by getting 3 marks in a row (horizontally, vertically, or diagonally)
- If all squares are filled with no winner, it's a tie

## AI Algorithm

The AI uses the **minimax algorithm** with the following strategy:
- **Maximizing player (X)**: Tries to maximize the score (wins = +1)
- **Minimizing player (O)**: Tries to minimize the score (wins = -1)
- **Tie**: Results in a score of 0

The AI evaluates all possible future game states and chooses the move that leads to the best outcome, making it unbeatable.

## Project Structure

```
tictactoe/
├── tictactoe.py      # Core game logic and minimax algorithm
├── runner.py         # Pygame GUI and game loop
├── requirements.txt  # Python dependencies
├── .gitignore       # Git ignore rules
└── README.md        # This file
```

## Code Overview

### `tictactoe.py`
Contains the core game logic:
- `initial_state()`: Creates empty 3x3 board
- `player(board)`: Determines whose turn it is
- `actions(board)`: Returns set of possible moves
- `result(board, action)`: Applies a move to the board
- `winner(board)`: Checks for winning conditions
- `terminal(board)`: Checks if game is over
- `utility(board)`: Returns game score (-1, 0, 1)
- `minimax(board)`: AI decision making
- `max_value(board)` / `min_value(board)`: Minimax implementation

### `runner.py`
Handles the Pygame interface:
- Game window and rendering
- Mouse click detection
- Player vs AI turn management
- Game state display

## Development

This project was created as a learning exercise to understand:
- Game tree algorithms
- Minimax strategy
- Pygame basics
- Python game development

## License

This project is open source and available under the MIT License.
