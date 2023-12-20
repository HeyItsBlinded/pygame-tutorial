import pygame, sys
import random

# very important
pygame.init()
clock = pygame.time.Clock()

# window set-up
scr_width = 1280
scr_height = 960
screen = pygame.display.set_mode((scr_width, scr_height))   # display surface
pygame.display.set_caption('PONG')

# creating color palette
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

# score-keeping initializations
player1_score = 0
player2_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)

# game assets - rects go around sprites, like a hitbox?
ball = pygame.Rect(scr_width/2 - 15, scr_height/2 - 15, 30, 30)
player1 = pygame.Rect(scr_width - 20, scr_height/2 - 70, 10, 140)
player2 = pygame.Rect(10, scr_height/2 - 70, 10, 140)

ballspeedX = 7 * random.choice((1,-1))
ballspeedY = 7 * random.choice((1,-1))
player1Speed = 0
player2Speed = 0

# ------- DEFS -------
def ball_animation():
    global ballspeedX, ballspeedY, player1_score, player2_score
    ball.x += ballspeedX
    ball.y += ballspeedY
    if ball.top <= 0 or ball.bottom >= scr_height:
        ballspeedY *= -1
    if ball.left <= 0:  # if player1 scores
        player1_score += 1
        ballresetpos()
    if ball.right >= scr_width: # if player2 scores
        player2_score += 1
        ballresetpos()
    if ball.colliderect(player1) and ballspeedX > 0:
        if abs(ball.right - player1.left < 10):
            ballspeedX *= -1
        elif abs(ball.bottom - player1.top) < 10 and ballspeedY > 0:
            ballspeedY *= -1
        elif abs(ball.top - player1.bottom) < 10 and ballspeedY < 0:
            ballspeedY *= -1
    if ball.colliderect(player2) and ballspeedX < 0:
        if abs(ball.left - player2.right < 10):
            ballspeedX *= -1
        elif abs(ball.bottom - player2.top) < 10 and ballspeedY > 0:
            ballspeedY *= -1
        elif abs(ball.top - player2.bottom) < 10 and ballspeedY < 0:
            ballspeedY *= -1

def ballresetpos():
    global ballspeedX, ballspeedY
    ball.center = (scr_width/2, scr_height/2)
    ballspeedY = 0
    ballspeedX = 0

def player1_animation():
    player1.y += player1Speed
    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= scr_height:
        player1.bottom = scr_height

def player2_animation():
    player2.y += player2Speed
    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= scr_height:
        player2.bottom = scr_height

# ------- GAME LOOP -------
while True:
    # handles input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ballresetpos()
                ballspeedY = random.choice((1, -1)) * 7
                ballspeedX = random.choice((1, -1)) * 7

        # player1 ctrls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player1Speed += 7
            if event.key == pygame.K_UP:
                player1Speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player1Speed -= 7
            if event.key == pygame.K_UP:
                player1Speed += 7

        # player2 ctrls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                player2Speed += 7
            if event.key == pygame.K_w:
                player2Speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                player2Speed -= 7
            if event.key == pygame.K_w:
                player2Speed += 7
    
    ball_animation()
    player1_animation()
    player2_animation()

    # visuals !!
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player1)
    pygame.draw.rect(screen, light_grey, player2)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (scr_width/2, 0), (scr_width/2, scr_height))

    # score visuals
    player1_text = game_font.render(f"{player1_score}", False, light_grey)
    screen.blit(player1_text, (660, 470))
    player2_text = game_font.render(f"{player2_score}", False, light_grey)
    screen.blit(player2_text, (600, 470))

    # updates game window
    pygame.display.flip()
    clock.tick(60)