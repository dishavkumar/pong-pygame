# Pong Game - Python & Pygame

A classic **Pong** game built using **Python** and **Pygame**.  
Two-player game with simple collision and scoring mechanics.

---

## Features

- Two-player gameplay:
  - Left paddle: `W` / `S`
  - Right paddle: `↑` / `↓`
- Ball bounces off paddles and walls
- Score tracking
- Press **SPACE** to start the game

---

## Installation

1. Clone the repo:

git clone https://github.com/dishavkumar/pong-pygame.git
cd pong-pygame

2. Create virtual environment and activate:

py -m venv .venv
.venv\Scripts\activate

3. Install dependencies:

pip install -r requirements.txt


How to Play

Left Paddle: W / S

Right Paddle: ↑ / ↓

Start Game: SPACE

Quit: Close window

Left scores if the ball hits the right edge, right scores if it hits the left edge.

The ball resets after a point.

Files

pong.py → Main game code

requirements.txt → Dependencies

.gitignore → Files to ignore

README.md → Project info