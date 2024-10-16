import pygame
import math
import random

def generate_random_speed(min_speed, max_speed):
    speed_x = random.randrange(2,5)
    print(speed_x)
    return speed_x

pygame.init()

WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bouncing Ball')

backGroundColor = (255,255,255)
borderColor = (0, 0, 0)
ballColor = (110, 6, 242)

CIRCLE_RADIUS = 120
CIRCLE_CENTER = (WIDTH // 2, HEIGHT // 2)
BALL_RADIUS = 10
ballX, ballY = CIRCLE_CENTER

def is_ball_inside_circle(ballX, ballY):
    distance_from_center = math.sqrt((ballX - CIRCLE_CENTER[0]) ** 2 + (ballY - CIRCLE_CENTER[1]) ** 2)
    # print(distance_from_center,BALL_RADIUS,CIRCLE_RADIUS)
    return distance_from_center + BALL_RADIUS <= CIRCLE_RADIUS

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(backGroundColor)

    pygame.draw.circle(screen, borderColor, CIRCLE_CENTER, CIRCLE_RADIUS, 4)
    ballSpeedX, ballSpeedY = generate_random_speed(1,2), generate_random_speed(1,2)

    ballX += ballSpeedX
    ballY += ballSpeedY

    if not is_ball_inside_circle(ballX, ballY):
        ballSpeedX = -ballSpeedX
        ballSpeedY = -ballSpeedY
        ballX += ballSpeedX
        ballY += ballSpeedY

    pygame.draw.circle(screen, ballColor, (ballX, ballY), BALL_RADIUS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
