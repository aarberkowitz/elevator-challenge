Elevator Challenge Game
Overview

The Elevator Challenge is a simulation game built using Pygame. The game involves a building with multiple floors and elevators. Users interact with the game by clicking on floor buttons to call elevators, which will move between floors to pick up and drop off passengers. The goal is to manage the elevators efficiently to minimize wait times.
Features:

    Interactive floor buttons to call elevators.
    Multiple elevators that move up and down between floors.
    Elevator arrival notification with a sound effect ("ding").
    Scrolling canvas to view all floors and elevators.
    Smooth elevator movement with adjustable speed.

Requirements

Before running the game, ensure you have the following installed:

    Python 3.x (Preferably 3.7 or higher)
    Pygame library

You can install Pygame by running:

pip install pygame

Files
Main Code

    main.py: This is the primary file where the game logic runs. It initializes Pygame, handles user input, and updates the game state.

Classes

    Elevator: Represents an elevator in the building. It handles its movement, task queue, and interaction with floors.
    Floor: Represents a floor in the building. Each floor has a call button that users can click to request an elevator.
    Building: Represents the entire building, which consists of multiple floors and elevators. It manages the floor requests and dispatches elevators to serve those requests.

Assets

    ELEVATOR_IMG_PATH: The image of the elevator.
    FLOOR_IMG_PATH: The image of the floor.
    ELEVATOR_DING_PATH: Path to the elevator arrival sound.

Configuration

The game uses some constants that can be set in a separate configuration file:

    SCREEN_WIDTH and SCREEN_HEIGHT: Screen dimensions.
    MARGIN: The margin between floor images.
    TOTAL_FLOORS: The total number of floors in the building.
    NUMBER_OF_ELEVATORS: The number of elevators available.
    ELEVATOR_SIZE: Size of the elevator image.
    BUTTON_RADIUS: Radius of the floor call button.

How to Play

    Launch the game by running main.py.
    Click on any of the floor call buttons to request an elevator.
    Watch the elevator move to the requested floor.
    The elevator plays a "ding" sound when it arrives at a floor.
    Scroll the canvas up and down to view all floors and elevators using your mouse wheel.
    Enjoy the challenge of managing multiple elevators simultaneously!

Running the Game

To start the game, run the following command in the terminal:

python main.py

Make sure the required assets (images and sound files) are correctly placed in the project folder. These assets are crucial for the correct rendering of the game.
Code Structure

    main.py: This file contains the core game loop, event handling, and updates for the game.
    Elevator class: Manages the elevator's state, movement, and floor requests.
    Floor class: Handles each floor's button and position.
    Building class: Manages the entire building, including floors and elevators.

Customization

If you want to modify the game:

    Add More Floors or Elevators: Change TOTAL_FLOORS or NUMBER_OF_ELEVATORS in the configuration file to increase or decrease the number of floors or elevators.
    Customize Elevator Speed: Modify the constant ELEVATOR_MOVEMENT_SPEED to change how quickly the elevator moves between floors.
    Change Images and Sounds: Replace the elevator and floor images or the sound file for the "ding" sound.

License

This project is open-source. Feel free to modify, fork, and share!
