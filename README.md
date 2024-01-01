# Snakes and Ladders Board Game
***Author:*** Vishrutha Gopa

## Introduction

This Python implementation of the Snakes and Ladders board game utilizes the pygame library for graphical representation. The game includes additional features, such as numbered tiles, exact requirements for movement, and snake connections.

## Features Implemented

1. **Numbered Tiles:** The board consists of numbered tiles, with each square displaying its corresponding number.
2. **Exact Requirements:** Players cannot move past the end of the board, ensuring adherence to the game's rules.
3. **Snake Connections:** To address a potential issue where players might get stuck on square 109, snake connections have been implemented. Landing on specific squares redirects the player to a different square.

## How to Play

1. Run the Python script to launch the game.
2. Players take turns rolling two six-sided dice by pressing Enter.
3. The purple player (Player 1) and green player (Player 2) tokens move across the board based on the dice roll.
4. The game incorporates snake connections on certain squares, redirecting players to different positions.
5. The first player to reach or exceed square 110 wins the game.