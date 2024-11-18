import pygame
import random

# make a comment
def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        x_mole_image = 0
        y_mole_image = 0
        screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x_click, y_click = event.pos
                    if x_mole_image <= x_click + 32:
                        if y_mole_image <= y_click + 32:
                            x_mole_image = random.randrange(0, 20) * 32
                            y_mole_image = random.randrange(0, 16) * 32

            screen.fill("light green")
            x = 0
            y = 0
            for i in range(20):
                x += 32
                pygame.draw.line(screen, "black", (x, 0), (x, 512))
            for i in range(16):
                y += 32
                pygame.draw.line(screen, "black", (0, y), (640, y))
            screen.blit(mole_image, (x_mole_image, y_mole_image))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
