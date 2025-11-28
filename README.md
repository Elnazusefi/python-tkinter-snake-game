# 🐍 Python Snake Game 🐍
A classic implementation of the popular Snake game, developed using the Tkinter library for the Graphical User Interface (GUI) and Object-Oriented Programming (OOP) principles in Python. This project was created to reinforce skills in event handling, animation, and organized code structure.

# ✨ Key Features
Classic Gameplay: Complete Snake game mechanics, including continuous movement, growth upon eating food, and Game Over logic upon collision with walls or the snake's own body.

Tkinter GUI: Utilizes a Canvas for drawing the grid-based environment and rendering smooth animation updates.

Event Handling: Employs the ``` window.bind() ``` method to control the snake's direction using keyboard arrow keys.

Scoring System: Real-time score display at the top of the window.

Restart Functionality: Includes a dedicated ```RESTART``` button for quick game resets.

# 🛠️ How to Run
This project requires no external library installation and runs natively with Python 3 (as tkinter is included by default).
1. Clone the Repository
```
git clone [Your Repository URL Here]
cd python-tkinter-snake-game
```
2. Execute the Game
Run the main file using your terminal or Command Prompt:
```
python snake_game.py
```
# 💡 Structure and Architecture
The code is organized using Object-Oriented Programming (OOP) concepts:

```class Snake```: Responsible for holding the snake's body coordinates and the graphical IDs of each segment.

```class Food```: Responsible for randomly generating food coordinates and displaying the food item.

```next_turn()```: The core game loop function that handles movement, checks for food collisions, and manages the animation refresh using ```window.after()```.

# 📚 Learning Resource
This project was completed as a practical exercise following a Tkinter GUI development course from the ```Sabzlearn``` team.

# 🤝 Contribution
Suggestions for improving the code and adding new features (like a persistent high score or difficulty levels) are highly welcome!

1. Fork the repository.

2. Create a new branch for your feature (```git checkout -b feature/amazing-feature```).

3. Commit your changes (```git commit -m 'Add amazing feature'```).

4. Push the changes (```git push origin feature/amazing-feature```).

5. Open a Pull Request.
