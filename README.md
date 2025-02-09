#Snake Game 2025 - Learning Python with 100 days of code 

## Program Overview
This is a version of the snake game created in Python using the 'turtle' module. You play as a snake that is trying to eat 
food pellets while avoiding the walls and your own tail. The tail of the snake grows longer as it eats more pellets increasing 
the difficulty level of the game. Eating a pellet increases the player score. 


##Features 
- **Movement**: The snake moves continuously in four directions up, down, left, and right. Controlled with the arrow keys. 
- **Food**: The snake eats the food pellets causing the tail to grow longer and the score to increase.
- **Collision Detection**: The game detects the snakes collision with the walls and its own tail ending the game.
- **Scoreboard**: The score increases by eating food pellets and resets to 0 at game end.

##Requirements 
- Python 3.x
- 'turtle' module

##How to Play 
1. **Start the game**: Run the program from main to start the game window.
2. **Control of Snake**: Snake will start in the center of the screen and is controlled with the arrow keys on keyboard.
 - **Up**: Move the snake up.
 - **Down**: Move the snake down.
 - **Left**: Move the snake left.
 - **Right**: Move the snake right.
3. **Eating Food**: Touching the pellots grows the snake and increases your score.
4. **Collisions**: Touching the walls or the snakes tail will end the game and record your high score.

## Code Description
- **Screen Setup**: The game initializes a 600x600 black screen using the `turtle` module. The title of the game is "Snake 2025 - Learning Python".
- **Snake Object**: The snake is created as an object that consists of segments (initially 3 segments long).
- **Food Object**: The food appears at random positions on the screen and is eaten when the snake collides with it.
- **Scoreboard**: Tracks the score, which increases when the snake eats food and resets when the game restarts after a collision.
- **Game Loop**: The game runs in a loop, updating the screen and checking for collisions with food, walls, and the snake's tail.

## How to Run
1. Download or clone the repository to your local machine.
2. Ensure you have Python 3.x installed.
3. Run the script in your Python environment:
   ```bash
   python snake_game.py


##License
This project is open-source and available for educational purposes. Feel free to modify and improve =. 

Enjoy! 
   
