# Knights and Knaves Puzzle Solver

A Python implementation of a propositional logic solver for classic Knights and Knaves puzzles from CS50's Introduction to Artificial Intelligence with Python.

## 🧩 About Knights and Knaves Puzzles

Knights and Knaves puzzles are classic logic puzzles where:
- **Knights** always tell the truth
- **Knaves** always lie
- You must determine who is who based on their statements

This project implements a propositional logic engine that can solve these puzzles automatically using model checking.

## 🚀 Features

- **Propositional Logic Engine**: Complete implementation of logical operators (And, Or, Not, Implication, Biconditional)
- **Model Checking**: Automated puzzle solving using truth table enumeration
- **Four Classic Puzzles**: Pre-implemented solutions for classic Knights and Knaves scenarios
- **Extensible Design**: Easy to add new puzzles and logical statements

## 📁 Project Structure

```
cs50-knights/
├── logic.py          # Core propositional logic engine
├── puzzle.py         # Puzzle definitions and solver
├── venv/             # Virtual environment
└── README.md         # This file
```

## 🛠️ Installation

1. **Clone the repository** (if not already done):
   ```bash
   git clone <repository-url>
   cd cs50-knights
   ```

2. **Set up virtual environment** (if not already done):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies** (if any):
   ```bash
   pip install -r requirements.txt  # If requirements.txt exists
   ```

## 🎯 Usage

### Running the Puzzles

Simply run the main script to see all puzzle solutions:

```bash
python puzzle.py
```

### Example Output

```
Puzzle 0
    A is a Knave

Puzzle 1
    A is a Knave
    B is a Knight

Puzzle 2
    A is a Knave
    B is a Knight

Puzzle 3
    A is a Knight
    B is a Knave
    C is a Knight
```

## 🧠 Puzzle Descriptions

### Puzzle 0: The Contradiction
- **A says**: "I am both a knight and a knave."
- **Solution**: A must be a knave (since no one can be both)

### Puzzle 1: The Mutual Accusation
- **A says**: "We are both knaves."
- **B says**: nothing
- **Solution**: A is a knave, B is a knight

### Puzzle 2: The Identity Crisis
- **A says**: "We are the same kind."
- **B says**: "We are of different kinds."
- **Solution**: A is a knave, B is a knight

### Puzzle 3: The Complex Chain
- **A says**: either "I am a knight." or "I am a knave." (unknown which)
- **B says**: "A said 'I am a knave'."
- **B says**: "C is a knave."
- **C says**: "A is a knight."
- **Solution**: A is a knight, B is a knave, C is a knight

## 🔧 Technical Details

### Logic Engine Components

The `logic.py` file implements a complete propositional logic system:

- **Symbol**: Represents atomic propositions
- **Not**: Logical negation
- **And**: Logical conjunction
- **Or**: Logical disjunction  
- **Implication**: Logical implication (if-then)
- **Biconditional**: Logical equivalence (if and only if)

### Model Checking Algorithm

The solver uses a recursive model checking algorithm that:
1. Enumerates all possible truth value assignments
2. Checks if the knowledge base is consistent
3. Determines which symbols must be true in all valid models

## 🎓 Educational Value

This project demonstrates:
- **Propositional Logic**: Core concepts of formal logic
- **Model Checking**: Automated theorem proving techniques
- **Recursive Algorithms**: Tree traversal and backtracking
- **Object-Oriented Design**: Clean separation of logical operators

## 🔍 How It Works

1. **Symbol Definition**: Each person's identity is represented as a logical symbol
2. **Constraint Encoding**: Statements are translated into logical formulas
3. **Model Checking**: The algorithm finds all valid truth assignments
4. **Solution Extraction**: Symbols that are true in all valid models are identified

## 🧪 Adding New Puzzles

To add a new puzzle:

1. Define symbols for each person:
   ```python
   XKnight = Symbol("X is a Knight")
   XKnave = Symbol("X is a Knave")
   ```

2. Encode the constraints:
   ```python
   knowledge = And(
       Or(XKnight, XKnave),
       Not(And(XKnight, XKnave)),
       # Add implications based on statements
   )
   ```

3. Add to the puzzles list in `main()`

## 📚 Related Concepts

- **Propositional Logic**: The foundation of formal reasoning
- **Model Theory**: Mathematical study of truth in logical structures
- **Automated Theorem Proving**: Using computers to verify logical arguments
- **Constraint Satisfaction**: Finding solutions that satisfy all given constraints

## 🎯 CS50 Context

This project is part of CS50's Introduction to Artificial Intelligence with Python, specifically covering:
- Knowledge representation
- Logical reasoning
- Automated problem solving
- Python programming fundamentals

## 🤝 Contributing

Feel free to:
- Add new puzzle variations
- Improve the logic engine
- Optimize the model checking algorithm
- Add visualization features

## 📄 License

This project is part of the CS50 curriculum and follows the same educational licensing terms.

---

*Built with Python and powered by propositional logic* 🧠✨
