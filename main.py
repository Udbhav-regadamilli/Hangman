import pygame, random, time

pygame.init()

#images for hangman
hangmans = [ pygame.transform.scale(pygame.image.load(r"images\\hangman0.png"), (200, 200)),
pygame.transform.scale(pygame.image.load(r"images\\hangman1.png"), (200, 200)),
pygame.transform.scale(pygame.image.load(r"images\\hangman2.png"), (200, 200)),
pygame.transform.scale(pygame.image.load(r"images\\hangman3.png"), (200, 200)),
pygame.transform.scale(pygame.image.load(r"images\\hangman4.png"), (200, 200)),
pygame.transform.scale(pygame.image.load(r"images\\hangman5.png"), (200, 200)),
pygame.transform.scale(pygame.image.load(r"images\\hangman6.png"), (200, 200))]

width = 800
height = 750
words = ["lucky", "ujwal", "praveen", "vijaya"]
word = random.choice(words)

#all the functions required for the game
class board:

    #displays the "___" on the screen
    def Words():
        for _ in range(len(word)):
            if 120*(_+1)+40 > width:
                _=_-6
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(120*_+30, 300, 90, 10))
            else:
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(120*_+40, 150, 100, 10))

        pygame.display.flip()


    #displaying the letters user type on the screen
    def display_letter(t, index):
        letter = pygame.font.SysFont('Courier New', 100)
        text = letter.render(t, False, (0, 0, 0))
        for i in range(len(index)):
            if 120*(int(index[i])+1)+55 > width:
                index[i] -= 6
                screen.blit(text, (120*int(index[i])+45, 200))
            else:
                screen.blit(text, (120*int(index[i])+55, 30))

    #displays the hangman images
    def hangman(i):
        print(i)
        screen.blit(hangmans[i], (300, 400))

def main():
    run = True
    t = ''
    ind = []
    worng = 0
    guess = "0"*len(word)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        board.Words()
        text = str(input())
        if len(text) != 0:
            if text[0] in word:
                for i in range(len(word)):
                    if text[0] == word[i]:
                        t = text[0]
                        ind.append(i)
                        guess = guess[:i] + t + guess[i+1:]
                        print(guess)
                        board.display_letter(t.upper(), ind)
                        ind.clear()
            else:
                board.hangman(worng)
                worng += 1
                if worng == 7:
                    print("You Lost!")
                    letter = pygame.font.SysFont('Courier New', 50)
                    text = letter.render("You Lost!", False, (255, 0, 0))
                    screen.blit(text, (300, 600))
        
        if guess == word:
            print("You Won")
            letter = pygame.font.SysFont('Courier New', 50)
            text = letter.render("You Won!", False, (0, 255, 0))
            screen.blit(text, (300, 600))

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hangman")
screen.fill((255,255,255))
pygame.display.flip()
main()