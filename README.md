# Project

# Stone Paper Scissors Thread Game

A simple GUI-based extended version of the classic Stone-Paper-Scissors game built with Python's Tkinter library. This version adds an additional choice, **Thread**, to increase the challenge and fun.

## Features

- Four choices: Stone, Paper, Scissors, Thread
- Best of 5 rounds gameplay
- Real-time score updates
- Game log displaying each round's results
- Final winner announcement at the end of 5 rounds
- Restart and Exit buttons for convenience
- Simple and clean user interface

## How to Play

1. Click on one of the four choice buttons: **Stone**, **Paper**, **Scissors**, or **Thread**.
2. The computer randomly selects a choice.
3. The game decides the round winner based on predefined rules.
4. Scores and round information are updated live.
5. After 5 rounds, the final winner is announced.
6. You can restart the game anytime by clicking the **Restart** button.

## Rules Summary

| Player Choice | Beats           | Loses to        | Tie with       |
|---------------|-----------------|-----------------|----------------|
| Stone         | Scissors        | Paper, Thread   | Stone          |
| Paper         | Stone           | Scissors        | Thread         |
| Scissors      | Paper, Thread   | Stone           | Scissors       |
| Thread        | Stone           | Scissors        | Paper          |

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)

## How to Run

1. Clone or download this repository.
2. Run the `stone_paper_scissors_thread.py` script:

```bash
python stone_paper_scissors_thread.py
