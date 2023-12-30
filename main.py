import pygame
import random
from pygame import mixer


class Snake:

    def __init__(self):  # Creates the snake
        self.x, self.y = screen_width / 2, screen_height / 2  # Sets the spawn of the snake
        self.x_direction = 1  # Creates the x direction
        self.y_direction = 0  # Creates the y direction
        self.head = pygame.Rect(self.x, self.y, grid_size, grid_size)  # Creates the head of the snake
        self.body = [pygame.Rect(self.x - grid_size, self.y, grid_size, grid_size)]  # Creates the body of the snake
        # self.dead = False

    def update(self):  # Function to update the snake

        self.body.append(self.head)

        for i in range(len(self.body)-1):
            self.body[i].x, self.body[i].y = self.body[i+1].x, self.body[i+1].y

        self.head.x += self.x_direction * grid_size
        self.head.y += self.y_direction * grid_size
        self.body.remove(self.head)


class Apple:

    def __init__(self):  # Creates the apple

        self.x = int((random.randint(0, screen_width) / grid_size)) * grid_size  # Sets the spawn location of the apple
        # (x-value)

        self.y = int((random.randint(0, screen_height) / grid_size)) * grid_size  # Sets the spawn location of the apple
        # (y-value)

        self.rect = pygame.Rect(self.x, self.y, grid_size, grid_size)  # Creates the apple

    def update(self):  # Updates the apple position

        pygame.draw.rect(screen, apple_color, self.rect)


def title_screen():  # Function to display the title screen message/title

    title_screen_title_surface = title_screen_font.render(f' Snake!', False, font_color)
    title_screen_title_rect = title_screen_title_surface.get_rect(center=(screen_width / 2, 100))
    screen.blit(title_screen_title_surface, title_screen_title_rect)

    title_screen_play = title_screen_font_play_message.render(f' Press "Space" to Play!', False, font_color)
    title_screen_play_rect = title_screen_play.get_rect(center=(screen_width / 2, 500))
    screen.blit(title_screen_play, title_screen_play_rect)


def display_score():  # Function to display the score

    player_score_surface = game_font.render(f' Score: {score}', False, score_color)
    player_score_rect = player_score_surface.get_rect(center=(screen_width / 2, 30))
    screen.blit(player_score_surface, player_score_rect)


def game_over_screen():  # Function to display the game over screen

    game_over_screen_score = title_screen_font_play_message.render(f' You collected {score} apple(s)!', False,
                                                                   font_color)

    game_over_screen_score_rect = game_over_screen_score.get_rect(center=(screen_width / 2, 100))
    screen.blit(game_over_screen_score, game_over_screen_score_rect)

    game_over_screen_play = title_screen_font_play_message.render(f' Press "Space" to Restart', False, font_color)
    game_over_screen_play_rect = game_over_screen_play.get_rect(center=(screen_width / 2, 500))
    screen.blit(game_over_screen_play, game_over_screen_play_rect)


''' def grid():  # Function to display a grid

    for x in range(0, screen_width, grid_size):

        for y in range(0, screen_height, grid_size):

            grid_rect = pygame.Rect(x, y, grid_size, grid_size)

            pygame.draw.rect(screen, grid_color, grid_rect, 1) '''


pygame.init()  # Starts pygame

pygame.display.set_caption('Snake')  # Sets the caption for the game window

# Constant Variables

grid_size = 50

screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))  # Creates the game screen

clock = pygame.time.Clock()  # Part of managing FPS

score = 0

# Colors

snake_color = (0, 255, 0)  # Green

snake_head_color = (255, 0, 0)  # Red

apple_color = (255, 0, 0)  # Red

font_color = (0, 255, 0)  # Green

score_color = (255, 255, 255)  # White

grid_color = (128, 128, 128)

# Game Font

title_screen_font = pygame.font.Font('Minecraft copy 2.ttf', 70)

title_screen_font_play_message = pygame.font.Font('Minecraft copy 2.ttf', 55)

game_font = pygame.font.Font('Minecraft copy 2.ttf', 50)

# Flag Variables

title_screen_flag = False

game_active = False

move_up = False

move_down = False

move_left = False

move_right = False

# List used for randomly picking the snake direction

movement_list = ['up', 'down', 'left', 'right']

snake = Snake()
apple = Apple()

# Game Sounds

death_sound = pygame.mixer.Sound('audio/dead-8bit-41400.mp3')
death_sound.set_volume(1.0)

apple_pickup = pygame.mixer.Sound('audio/beep3-98810.mp3')
apple_pickup.set_volume(1.0)

# Main Game Loop

while True:

    # Event Loop

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()

            exit()

        if game_active:

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:

                    move_up = True

                    move_down = False

                    move_left = False

                    move_right = False

                if event.key == pygame.K_DOWN:

                    move_down = True

                    move_up = False

                    move_left = False

                    move_right = False

                if event.key == pygame.K_LEFT:

                    move_left = True

                    move_up = False

                    move_down = False

                    move_right = False

                if event.key == pygame.K_RIGHT:

                    move_right = True

                    move_up = False

                    move_down = False

                    move_left = False

        else:

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:

                    game_active = True

                    title_screen_flag = True

                    score = 0

                    apple = Apple()

                    # Playing the game music

                    mixer.music.load('audio/026491_pixel-song-8-72675.mp3')  # Loads in the music
                    pygame.mixer.music.play(-1)  # Loops the music
                    pygame.mixer.music.set_volume(1.0)  # Sets the music volume

                    # Resetting the snake position and status

                    snake.head = pygame.Rect(snake.x, snake.y, grid_size, grid_size)
                    snake.body = [pygame.Rect(snake.x - grid_size, snake.y, grid_size, grid_size)]
                    # snake.dead = False

                    # Deciding random movement for the snake to start with

                    movement_pick = random.choice(movement_list)

                    if movement_pick == 'up':

                        move_up = True
                        move_down = False
                        move_left = False
                        move_right = False

                    elif movement_pick == 'down':

                        move_down = True
                        move_up = False
                        move_left = False
                        move_right = False

                    elif movement_pick == 'left':

                        move_left = True
                        move_up = False
                        move_down = False
                        move_right = False

                    elif movement_pick == 'right':

                        move_right = True
                        move_up = False
                        move_down = False
                        move_left = False

    if game_active:

        snake.update()  # Updates the snake

        screen.fill((0, 0, 0))

        ''' grid() '''

        apple.update()  # Updates the apple

        # Drawing the player and the apple on the screen

        pygame.draw.rect(screen, snake_head_color, snake.head)  # Draws the snake head

        for square in snake.body:  # Drawing the snake body

            pygame.draw.rect(screen, snake_color, square)

        # Displaying the score

        display_score()

        # Movement of the player

        if move_up:

            snake.y_direction = -1
            snake.x_direction = 0

        if move_down:

            snake.y_direction = 1
            snake.x_direction = 0

        if move_left:

            snake.x_direction = -1
            snake.y_direction = 0

        if move_right:

            snake.x_direction = 1
            snake.y_direction = 0

        # Checking if the player dies #

        # Checking if the player goes off-screen

        if snake.head.top < 0:

            game_active = False

            pygame.mixer.music.stop()  # Ending the music

            death_sound.play()  # Plays the death sound

        if snake.head.bottom > screen_height:

            game_active = False

            pygame.mixer.music.stop()  # Ending the music

            death_sound.play()  # Plays the death sound

        if snake.head.left < 0:

            game_active = False

            pygame.mixer.music.stop()  # Ending the music

            death_sound.play()  # Plays the death sound

        if snake.head.right > screen_width:

            game_active = False

            pygame.mixer.music.stop()  # Ending the music

            death_sound.play()  # Plays the death sound

        # Checking if the snake collides with itself

        for square in snake.body:

            if (snake.head.x == square.x) and (snake.head.y == square.y):

                game_active = False

                pygame.mixer.music.stop()  # Ending the music

                death_sound.play()  # Plays the death sound

        # Collision with the apple

        if snake.head.colliderect(apple.rect):

            apple_pickup.play()  # Plays the apple pickup sound

            score += 1

            snake.body.append(pygame.Rect(snake.head.x, snake.head.y, grid_size, grid_size))

            apple = Apple()

    else:

        # Displaying the title screen

        if (game_active is False) and (title_screen_flag is False):

            title_screen()

        else:

            # Displaying the Game Over Screen

            screen.fill((0, 0, 0))

            game_over_screen()

    # Updating the display

    pygame.display.update()  # Updates the display

    clock.tick(10)  # Acts as FPS
