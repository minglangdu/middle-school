"""
Christopher Lum 6-B1
6th Grade Computer Fair Project: Snake Game
"""
#import some VERY USELESS stuff

from tkinter import *
import random
import time

#defining variables, constant

GAME_WIDTH = 1000
GAME_HEIGHT = 700
BODY = 3
SPEED = 50
SPACE_SIZE = 50
SCORE = 0
FOOD_COLOR = "red"
SNAKE_COLOR = "#00FF00"
BACKGROUND_COLOR = "black"
colors = ["red","blue","#00FF00","yellow","pink","purple","light yellow","grey","maroon","indigo","violet",
          "green","brown","cyan","light blue","orange","lime","gold"]



#defining settings: add body, minus body, add speed, minus speed

def addB():
    global BODY
    global labelBody
    
    if BODY < 100:
        BODY += 1
    elif BODY >= 100:
        print("Body is too big!")
        
    labelBody.config(text=f"BODY SIZE:{BODY}")

def minusB():
    global BODY
    global labelBody
    
    if BODY > 3:
        BODY -= 1
    elif BODY <= 3:
        print("Body is too small!")
        
    labelBody.config(text=f"BODY SIZE:{BODY}")


def addS():
    global SPEED
    global labelSpeed
    
    if SPEED < 500:
        SPEED += 5
    elif SPEED >= 500:
        print("Speed is to slow!")
        
    labelSpeed.config(text=f"SPEED:{SPEED}")

def minusS():
    global SPEED
    global labelSpeed
    
    if SPEED > 25:
        SPEED -= 5
    elif SPEED <= 25:
        print("Speed is to fast!")
        
    labelSpeed.config(text=f"SPEED:{SPEED}")


#class for snake

class Snake:
    global colors
    
    def __init__(self):
        self.body_size = BODY
        self.coordinates = []
        self.squares = []
         
        for i in range(0, BODY): #adds the snake head
            self.coordinates.append([0,0]) 
            
        for x, y in self.coordinates: #creates the snake shape/square
            square = canvas.create_rectangle(x,y, x+SPACE_SIZE, y + SPACE_SIZE,
                                             fill=random.choice(colors), tags = "snake")
            self.squares.append(square)

#class for food
    
class Food:
    
    def __init__(self):
        #randomizing x and y coordinates for the apple to spawn
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) -1) * SPACE_SIZE
       
        self.coordinates = [x,y]
        
        #creating the shape of the food
       
        canvas.create_oval(x,y,x + SPACE_SIZE, y + SPACE_SIZE, fill = FOOD_COLOR, tags = "food")

#checking next turn

def next_turn(snake,food):
    x, y = snake.coordinates[0]
    
    global SCORE
    
    #updates the x and y coordinates depending on the direction
    
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
        
    #inserting the coordinates and updating the snake
    
    snake.coordinates.insert(0,(x,y))

    square = canvas.create_rectangle(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill=random.choice(colors), tags="square")
    
    snake.squares.insert(0,square)
    

    if x == food.coordinates[0] and y == food.coordinates[1]: #condition to check if the snake is on the food
        
        global score
        
        #adds and updates the score
        
        score += 1
        
        label.config(text="Score:{}".format(score))
        
        #deletes the food and spawns a new one
        
        canvas.delete("food")
        
        food = Food()
    
    else:
        
        #the last body part of the snake is deleted
        
        del snake.coordinates[-1]
        
        canvas.delete(snake.squares[-1])
        
        del snake.squares[-1]
        
    if check_collision(snake):
        
        game_over()
    
        
    elif SCORE == 30 or score == 30:
        
        #user wins if they have a score of 30
        
        canvas.delete(ALL)
        canvas.create_text((canvas.winfo_width()/2),(canvas.winfo_height()/2),
                           font=("consolas",70),text="YOU WIN", fill = "yellow",tags="winner")
    
    else:
        window.after(SPEED, next_turn, snake, food)
        
#changing directions
        
def change_direction(new_direction):
    
    global direction
    
    if new_direction == 'left':
        if direction != 'right': # snake is not allowed to turn 180 degrees
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

#checking collisions
        
def check_collision(snake):
    x, y = snake.coordinates[0]
    
    if x < 0 or x >= GAME_WIDTH: # checks if the x coordinates of the snake is less than zero or greater than the game width
        return True
    elif y < 0 or y >= GAME_HEIGHT: # checks if the y coordinates of the snake is less than zero or greater than the game height
        return True
    for body_part in snake.coordinates[1:]: #checks if the snake hits itself
        if x == body_part[0] and y == body_part[1]:
            return True
    return False
        
        
#game over

def game_over():
    canvas.delete(ALL)
    canvas.create_text((canvas.winfo_width()/2),(canvas.winfo_height()/2),
                       font=("consolas",70),text="GAME OVER", fill = "red",tags="gameover")

#restart


def restart():
    global score
    global SCORE      
    global Snake
    global Food
    global direction
    
    #reseting the canvas, score, direction, and updating them
    
    canvas.delete(ALL)
    
    score = 0
    SCORE = 0
    
    label.config(text=f"Score:{SCORE}")
    
    window.update()

    direction = "down"
    
    #recalling snake, food, and next turn
    
    snake = Snake()
    food = Food()

    next_turn(snake,food)



#framework, canvas, labels, and window/window size

window = Tk()
window.title("Snake Game")
window.resizable(True,True)

window.config(bg="dark blue")

score = 0
direction = "down"

label = Label(window,text=f"Score:{SCORE}", font=("consolas",70),bg="cyan")
label.pack()

canvas = Canvas(window,bg="black",width=GAME_WIDTH,height=GAME_HEIGHT)
canvas.pack()

#starts the window

window.mainloop

#allows fullscreen

window.attributes("-fullscreen")

#menu

def menu():
    
    words = "Welcome to the Snake Game"
    win = "30 Points to win the game!"
    settings = "This game is customizable!"
    fs = 'Click the full screen button!'
    
        
    canvas.create_text(500,150,font=("Consolas",50),text=words,fill="#00FF00",tags=words)
    
    canvas.create_text(500,300,font=("Consolas",50),text=win,fill="gold",tags=win)

    canvas.create_text(500,450,font=("Consolas",50),text=settings,fill="blue",tags=settings)
    
    canvas.create_text(500,600,font=("Consolas",45),text=fs,fill="red",tags=settings)

    
menu()

#restart button

button = Button(window,width=7,height=2,text='Restart',font=('consolas',50), command=restart,bg="cyan",activebackground="cyan")
button.pack()

window.update()



#settings

#allows user to increase and decrease the body
labelBody = Label(window,text=f"BODY SIZE:{BODY}",font=('consolas',30),bg="cyan",fg="black",height=2)
labelBody.place(x=115,y=865)

buttonBodyAdd = Button(window,width=5,height=2,text="+",font=('consolas',30), command=addB)
buttonBodyAdd.place(x=0,y=850)

buttonBodySub = Button(window,width=5,height=2,text="-",font=('consolas',30), command=minusB)
buttonBodySub.place(x=380,y=850)


#allows user to increase and decrase the speed
labelSpeed = Label(window,text=f"SPEED:{SPEED}",font=('consolas',35),bg="cyan",fg="black",height=2)
labelSpeed.place(x=890,y=855)

buttonSpeedAdd = Button(window,width=5,height=2,text="+",font=('consolas',30), command=addS)
buttonSpeedAdd.place(x=770,y=850)

buttonSpeedSub = Button(window,width=5,height=2,text="-",font=('consolas',30), command=minusS)
buttonSpeedSub.place(x=1150,y=850)


#key binding

window.bind("<Up>", lambda event: change_direction('up'))
window.bind("<Down>", lambda event: change_direction('down'))
window.bind("<Left>", lambda event: change_direction('left'))
window.bind("<Right>", lambda event: change_direction('right'))
window.bind("<w>", lambda event: change_direction('up'))
window.bind("<s>", lambda event: change_direction('down'))
window.bind("<a>", lambda event: change_direction('left'))
window.bind("<d>", lambda event: change_direction('right'))

#calling snake, food, and start

time.sleep(7)

canvas.delete(ALL)

snake = Snake()
food = Food()

next_turn(snake,food)