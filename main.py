# Pygame game template

import pygame
import sys
import config # Import the config module

def init_game ():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events ():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True
def main():
    screen = init_game()
    clock = pygame.time.Clock() # Initialize the clock here
    running = True
    while running:
        running = handle_events()
        screen.fill(config.WHITE) # Use color from config
        
        thick = 10

        st_cord1 = (100,100)
        st_cord2 = (200,200)
        st_cord3 = (300,300)
        st_cord4 = (400,400)
        st_cord5 = (500,500)
        st_cord6 = (600,600)

        end_cord1 = (700,100)
        end_cord2 = (300,800)
        end_cord3 = (500,400)
        end_cord4 = (600,700)
        end_cord5 = (100,800)
        end_cord6 = (800,500)

        pygame.draw.line(screen, config.FIREBRICK, st_cord1, end_cord1, thick)
        pygame.draw.line(screen, config.TANGERINE, st_cord2, end_cord2, thick)
        pygame.draw.line(screen, config.DARKGOLDENROD, st_cord3, end_cord3, thick)
        pygame.draw.line(screen, config.BLACK, st_cord4, end_cord4, thick)
        pygame.draw.line(screen, config.LAVENDERPURPLE, st_cord5, end_cord5, thick)
        pygame.draw.line(screen, config.ROSYBROWN, st_cord6, end_cord6, thick)

        pygame.display.flip()
        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(config.FPS) # Use the clock to control the frame rate

    pygame.quit()

    sys.exit()

if __name__ == "__main__":
    main()