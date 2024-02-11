import pygame
import random

pygame.init()

# Constants
WIDTH = 800
HEIGHT = 750
WORDS = ["Python", "Computer", "Hangman", "Programming", "Algorithm", "Keyboard", "Mouse", "Software", "Internet", "Database"]
HINTS = [
    "A popular programming language known for its simplicity and readability.",
    "An electronic device that processes data according to a set of instructions.",
    "A word guessing game where players try to guess a word letter by letter.",
    "The process of designing and building computer programs.",
    "A step-by-step procedure or formula for solving a problem.",
    "An input device used for typing characters into a computer or other device.",
    "A pointing device used to interact with graphical user interfaces.",
    "Programs and applications that run on computers and other devices.",
    "A global network that connects millions of computers and devices worldwide.",
    "An organized collection of data, typically stored and accessed electronically from a computer system."
]
HANGMAN_IMAGES = [pygame.transform.scale(pygame.image.load(f"images/hangman{i}.png"), (200, 200)) for i in range(7)]

# Function to display text on the screen
def display_text(screen, text, x, y, size=50, color=(0, 0, 0)):
    font = pygame.font.SysFont('Courier New', size)
    while len(text) > 60:
        rendered_text = font.render(text[:60], True, color)
        screen.blit(rendered_text, (x, y))
        text = text[50:]
        y += 15
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, (x, y))

# Function to display underscores for the word
def display_word(word, guessed_letters):
    displayed = ""
    for letter in word.lower():
        if letter in guessed_letters:
            displayed += letter + " "
        else:
            displayed += "_ "
    return displayed

# Function to check if the mouse cursor is over a button
def is_over_button(mouse_pos, button_rect):
    if button_rect.collidepoint(mouse_pos):
        return True
    return False

# Function to draw the retry button
def draw_buttons(screen):
    # Retry button rectangle
    retry_button_rect = pygame.Rect(150, 680, 200, 50)
    # Quit button rectangle
    quit_button_rect = pygame.Rect(450, 680, 200, 50)

    # Draw retry button
    pygame.draw.rect(screen, (180, 180, 180), retry_button_rect, border_radius=10)
    pygame.draw.rect(screen, (200, 200, 200), retry_button_rect.inflate(-4, -4), border_radius=10)
    retry_font = pygame.font.SysFont('Arial', 30)
    retry_text = retry_font.render("Retry", True, (0, 0, 0))
    retry_text_rect = retry_text.get_rect(center=retry_button_rect.center)
    screen.blit(retry_text, retry_text_rect)

    # Draw quit button
    pygame.draw.rect(screen, (180, 180, 180), quit_button_rect, border_radius=10)
    pygame.draw.rect(screen, (200, 200, 200), quit_button_rect.inflate(-4, -4), border_radius=10)
    quit_font = pygame.font.SysFont('Arial', 30)
    quit_text = quit_font.render("Quit", True, (0, 0, 0))
    quit_text_rect = quit_text.get_rect(center=quit_button_rect.center)
    screen.blit(quit_text, quit_text_rect)

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Hangman")
    clock = pygame.time.Clock()

    word = random.choice(WORDS)
    guessed_letters = set()
    wrong_attempts = 0
    game_over = False

    running = True
    while running:
        screen.fill((255, 255, 255))

        # Display hint message
        hint_message = "Hint: It's a " + HINTS[WORDS.index(word)]
        display_text(screen, hint_message, 50, 50, size=18, color=(100, 100, 100))

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and not game_over:
                if not game_over and event.key >= pygame.K_a and event.key <= pygame.K_z:
                    letter = chr(event.key)
                    if letter not in guessed_letters:
                        guessed_letters.add(letter)
                        if letter not in word:
                            wrong_attempts += 1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                retry_button_rect = pygame.Rect(150, 680, 200, 50)
                quit_button_rect = pygame.Rect(450, 680, 200, 50)
                if is_over_button(mouse_pos, retry_button_rect):
                    word = random.choice(WORDS)
                    guessed_letters = set()
                    wrong_attempts = 0
                    game_over = False
                if is_over_button(mouse_pos, quit_button_rect):
                    running = False

        # Display hangman image
        screen.blit(HANGMAN_IMAGES[wrong_attempts], (300, 400))

        # Display word
        displayed_word = display_word(word, guessed_letters)
        display_text(screen, displayed_word, 40, 150)

        # Draw buttons
        draw_buttons(screen)

        # Check win/loss
        if set(word.lower()) <= guessed_letters:
            display_text(screen, "You Won!", 300, 600, color=(0, 255, 0))
            game_over = True
        elif wrong_attempts >= 6:
            display_text(screen, "You Lost!", 300, 600, color=(255, 0, 0))
            game_over = True

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
