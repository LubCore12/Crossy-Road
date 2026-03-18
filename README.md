# Crossy Road Parody

A simple parody of **Crossy Road** made with **Python 3.12** and **Pygame**.

## About the Project

In this game, the player must complete the level while avoiding dangers on the way.  
The main goal is to reach the end **without falling into the river or getting hit by a car**.

> This is a **learning project**, so it is **not fully finished**.  
> The game currently **has no animations**, and some mechanics may be simplified.

## Technologies

- Python 3.12
- Pygame

## Gameplay

- Move through the level
- Avoid cars
- Do not fall into the river
- Reach the end of the level to win

## Installation and Launch

These instructions work on **Windows, Linux, and macOS**.

### 1. Clone the repository or download the project archive

```bash
git clone <your-repository-url>
cd <your-project-folder>
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows (Command Prompt):**
```bash
venv\Scripts\activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the game

```bash
python code/main.py
```

## Possible Issue

If the `python` command does not work on your system, try using `python3` instead:

```bash
python3 -m venv venv
python3 code/main.py
```

## Project Status

This project was created for learning purposes to practice:

- Pygame
- basic game logic
- collision handling
- small Python project structure
