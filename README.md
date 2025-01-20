# Realistic Fireworks and Birthday Cake

This is a fun interactive Python game created with Pygame. When you click anywhere on the screen, fireworks explode at the clicked position, accompanied by a birthday greeting. Once all the fireworks have finished, a birthday cake with candles and flames appears on the screen.

## Features

- Interactive Fireworks: Click to create fireworks with realistic particle effects.
- Birthday Cake: After all fireworks have been triggered, a colorful birthday cake with animated candles and flames appears.
- Birthday Message: Displays a birthday message that changes with each firework explosion.

## Requirements

- Python 3.x
- Pygame library

### Install Pygame

To install Pygame, run the following command:

```bash
pip install pygame
```

## How to Run

1. Download or clone the repository.
2. Ensure you have Python 3.x and Pygame installed.
3. Run the Python script to launch the fireworks and birthday cake animation:

```bash
python fireworks_and_cake.py
```

Click on the screen to trigger fireworks. The birthday cake will appear after all messages are displayed.

## Code Explanation

- Firework Class: Handles the creation of particles for each firework. The particles are launched in random directions with different speeds and colors.
- Particle Class: Represents a single particle in a firework. Each particle has a velocity, color, and lifetime, and moves according to its velocity until its lifetime expires.
- Cake Drawing: The cake is drawn with a gradient effect to give a 3D appearance. The candles and animated flames add a dynamic effect.
- Main Loop: The `run_fireworks` function handles the game loop, showing fireworks on mouse clicks and displaying birthday messages.

## Compatibility

This script should work on both **Windows** and **Linux** as long as Python and Pygame are installed. 
