import pygame

pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Text Input Box")

# Create a font object
font = pygame.font.Font(None, 32)

# Create a rectangular area for the input box
input_box = pygame.Rect(100, 100, 200, 32)

# Initialize the input string
input_string = ''

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                # Remove the last character from the input string
                input_string = input_string[:-1]
            elif event.key == pygame.K_RETURN:
                # Do something with the input string
                print(input_string)
                input_string = ''
            elif event.unicode.isalpha():
                # Add the pressed key to the input string if it's an alphabet character
                input_string += event.unicode

    # Clear the screen
    screen.fill(WHITE)

    # Draw the input box and the text inside it
    pygame.draw.rect(screen, BLACK, input_box, 2)
    text_surface = font.render(input_string, True, BLACK)
    screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
