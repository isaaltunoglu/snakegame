import tkinter
import random


ROWS = 25
COLS = 25
TILE_SIZE = 25

WİNDOW_WIDTH = COLS * TILE_SIZE
WİNDOW_HEIGHT = ROWS * TILE_SIZE

class Tile:
    def __init__(self,x,y):
        self.x = x
        self.y = y
#FOR WİNDOW

window = tkinter.Tk()
window.title("Snake Game")
window.resizable(False, False)
canvas = tkinter.Canvas(window,bg = "black", width=WİNDOW_WIDTH, height=WİNDOW_HEIGHT,borderwidth=0, highlightthickness=5,highlightbackground="blue")
canvas.pack()
window.update()
#center the window
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))
#format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
#---------------------------------------------------------------

#initialize game
snake = Tile(5*TILE_SIZE,5*TILE_SIZE)#SİNGLE TİLE,SNAKE'S HEAD
food = Tile(10*TILE_SIZE,10*TILE_SIZE)
snake_body = [] #multiple_tiles
velocityX = 0
velocityY = 0
game_over = False
score = 0



def change_direction(e): #e = event
    # print(e)
    # print(e.keysym)
    global velocityX,velocityY

    if game_over:
        return
    if e.keysym.lower() ==  "up" and velocityY != 1:
        velocityX = 0
        velocityY = -1
    elif e.keysym.lower() == "down" and velocityY != -1:
        velocityX = 0
        velocityY = 1
    elif e.keysym.lower() == "right" and velocityX != -1:
        velocityX = 1
        velocityY = 0
    elif e.keysym.lower() == "left"and velocityX != 1:
        velocityX = -1
        velocityY = 0

def move():
    global snake,food,snake_body,game_over,score
    if game_over:
        return

    if snake.x < 0 or snake.x >= WİNDOW_WIDTH or snake.y < 0 or snake.y >= WİNDOW_HEIGHT:
        game_over = True
        return
    for tile in snake_body:
        if snake.x == tile.x and snake.y == tile.y:
            game_over = True
            return
    #collision
    if snake.x == food.x and snake.y == food.y:
        snake_body.append(Tile(food.x,food.y))
        food.x = random.randint(0,COLS-1) * TILE_SIZE
        food.y = random.randint(0,ROWS-1) * TILE_SIZE
        score += 1
    #update snake body
    for i in range(len(snake_body)-1,-1,-1):
        tile = snake_body[i]
        if i == 0:
            tile.x = snake.x
            tile.y = snake.y
        else:
            prev_tile = snake_body[i-1]
            tile.x = prev_tile.x
            tile.y = prev_tile.y


    snake.x += velocityX * TILE_SIZE
    snake.y += velocityY * TILE_SIZE

def draw():
    global snake,food,snake_body,game_over,score
    move()
    canvas.delete("all")

    #draw snake
    canvas.create_rectangle(snake.x,snake.y,snake.x+TILE_SIZE,snake.y+TILE_SIZE,fill="green")
    #draw food
    canvas.create_rectangle(food.x,food.y,food.x+TILE_SIZE,food.y+TILE_SIZE,fill="red")

    for tile in snake_body:
        canvas.create_rectangle(tile.x,tile.y,tile.x + TILE_SIZE,tile.y + TILE_SIZE, fill="green")

    if game_over:
        canvas.create_text(WİNDOW_WIDTH/2,WİNDOW_HEIGHT/2,text=f"GAME OVER: {score}",fill="white",font=("Arial",24))
    else:
        canvas.create_text(30, 20,font = ("Arial",10),fill="white",text=f"Score: {score}")
        window.after(100,draw)#100 ms = 1/10 second


draw()
window.bind("<KeyRelease>",change_direction)

window.mainloop()

