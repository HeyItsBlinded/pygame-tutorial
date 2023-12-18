import pygame, sys

# very important
pygame.init()
clock = pygame.time.Clock()

# window set-up
scr_width = 1280
scr_height = 960
screen = pygame.display.set_mode((scr_width, scr_height))   # display surface
pygame.display.set_caption('PONG')

# game assets - rects go around sprites, like a hitbox?
ball = pygame.Rect(scr_width/2 - 15, scr_height/2 - 15, 30, 30)
player1 = pygame.Rect(scr_width - 20, scr_height/2 - 70, 10, 140)
player2 = pygame.Rect(10, scr_height/2 - 70, 10, 140)

# creating color palette
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

ballspeedX = 7
ballspeedY = 7
# ball physics and screen border collision
def ball_animation():
    global ballspeedX, ballspeedY
    ball.x += ballspeedX
    ball.y += ballspeedY
    if ball.top <= 0 or ball.bottom >= scr_height:
        ballspeedY *= -1
    if ball.left <= 0 or ball.right >= scr_width:
        ballspeedX *= -1
    if ball.colliderect(player1) or ball.colliderect(player2):
        ballspeedX *= -1

player1Speed = 0
def player1_animation():
    player1.y += player1Speed
    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= scr_height:
        player1.bottom = scr_height

player2Speed = 0
def player2_animation():
    player2.y += player2Speed
    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= scr_height:
        player2.bottom = scr_height

while True:
    # handles input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

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

    # sprites to show up on-screen
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player1)
    pygame.draw.rect(screen, light_grey, player2)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (scr_width/2, 0), (scr_width/2, scr_height))

    # updates game window
    pygame.display.flip()
    clock.tick(60)