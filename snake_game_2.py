#   SNAKE GAME #
import pygame
x=pygame.init()
import random
import os 
pygame.mixer.init()

bgimg=pygame.image.load("snake.jpeg")
bgimg=pygame.transform.scale(bgimg,(900,600))

#colors defining
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)

#creating game window
game_window=pygame.display.set_mode((900,600))
pygame.display.set_caption("Snakes Game!")
pygame.display.update()

clock=pygame.time.Clock()

font=pygame.font.SysFont(None,55)

def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    game_window.blit(screen_text,[x,y])


def plot_snake(game_window,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(game_window,color,[x,y,snake_size,snake_size])

def welcome():
    exit_game=False
    while not exit_game:
        game_window.fill((0,68,152))
        text_screen("Welcome To Snakes Game",black,260,250)
        text_screen("Press Spacebar to start the game",black,232,290)
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pygame.mixer.music.load('bg_music.mp3')
                    pygame.mixer.music.play()
                    gameloop()   
        pygame.display.update()
        clock.tick(60)       
#creating game loop
def gameloop():
    exit_game=False
    game_over=False
    snake_x=45
    velocity_x=0
    snake_y=55
    velocity_y=0
    snake_size=10
    food_size=10
    score=0
    init_velocity=5
    fps=30 #frames per second
    food_x=random.randint(20,450)
    food_y=random.randint(20,300)
    snk_list=[]
    snk_length=1
    if(not os.path.exists("high_score.txt")):
        with open ("high_score.txt","w") as f:
            f.write("0")
    with open("high_score.txt","r") as f:
        hiscore=f.read()
    while(exit_game==False):
        if game_over:
            with open("high_score.txt","w") as f:
                f.write(str(hiscore))
            game_window.fill(white)
            text_screen("Game over! Press Enter to continue",red,200,150)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=init_velocity
                        velocity_y=0
                    if event.key==pygame.K_LEFT:
                        velocity_x=-init_velocity
                        velocity_y=0
                    if event.key==pygame.K_UP:
                        velocity_x=0
                        velocity_y=-init_velocity
                    if event.key==pygame.K_DOWN:
                        velocity_x=0
                        velocity_y=init_velocity
                    if event.key==pygame.K_q:
                        score+=10
        
            snake_x+=velocity_x
            snake_y+=velocity_y

            if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
                score+=1
                snk_length+=5
                food_x=random.randint(20,450)
                food_y=random.randint(20,300)
                init_velocity+=2
                pygame.draw.rect(game_window,red,[food_x,food_y,10,10])
                if score>int(hiscore):
                    hiscore=score
            game_window.fill(white)
            game_window.blit(bgimg,(0,0))
            text_screen("Score: "+str(score*10)+"High score: "+str(hiscore),red,5,5)
            pygame.draw.rect(game_window,black,[snake_x,snake_y,snake_size,snake_size])
            pygame.draw.rect(game_window,red,[food_x,food_y,food_size,food_size])

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over=True
                pygame.mixer.music.load('game_over.wav')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>900 or snake_y<0 or snake_y>600:
                game_over=True
                pygame.mixer.music.load('game_over.wav')
                pygame.mixer.music.play()

            plot_snake(game_window,black,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)

# Quitting the game
    pygame.quit()
    quit()

welcome()
gameloop()