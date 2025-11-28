from tkinter import *
from random import randint
import os
import sys

# ----------------
GAME_WIDTH = 500
GAME_HEIGHT = 500
SPACE_SIZE = 25
BODY_SIZE = 3
SLOWNESS = 100
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "black"
score = 0
direction = "down"

# ----------------
class Snake:
    def __init__(self):
        self.body_size = BODY_SIZE
        self.coordinates = []
        self.squares = []

        for _ in range(BODY_SIZE):
            self.coordinates.append([0,0])
        
        for x,y in self.coordinates:
            squares = canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(squares)
        
class Food:
    def __init__(self):
        x = randint(0,(GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE 
        y = randint(0,(GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=FOOD_COLOR, tag="food")


# ----------------
def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    
    snake.coordinates.insert(0, [x,y])
    square = canvas.create_rectangle(x,y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0,square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text=f"Score: {score}")
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_game_over(snake):
        canvas.delete("all")
        canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,text="Game over", fill="red",
                            font=("Terminal",50), tag="game-over")
    else:
        window.after(SLOWNESS, next_turn, snake, food)

def change_direction(new_dir):
    global direction

    if new_dir == "up" and direction != "down":
        direction = new_dir
    elif new_dir == "down" and direction != "up":
        direction = new_dir
    elif new_dir == "left" and direction != "right":
        direction = new_dir
    elif new_dir == "right" and direction != "left":
        direction = new_dir

def check_game_over(snake):
    x,y = snake.coordinates[0]

    if x < 0 or x > GAME_WIDTH:
        return True
    if y < 0 or y > GAME_HEIGHT:
        return True
    for sq in snake.coordinates[1:]:
        if x == sq[0] and y == sq[1]:
            return True
    return False

def restart_program():
    path = sys.executable
    os.execl(path, path, *sys.argv)

# ----------------
window = Tk()
window.title("Snake Game")
window.resizable(False, False)

label = Label(window, text=f"Score: {score}", font=("Courier", 30))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, width=GAME_WIDTH, height=GAME_HEIGHT)
canvas.pack()

restart = Button(window, fg="red", text="RESTART", command=restart_program) 
restart.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind("<Up>", lambda e: change_direction("up"))
window.bind("<Down>", lambda e: change_direction("down"))
window.bind("<Left>", lambda e: change_direction("left"))
window.bind("<Right>", lambda e: change_direction("right"))

snake = Snake()
food = Food()

next_turn(snake, food)
window.mainloop()

