import pygame
import random

pygame.init()
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Jogo de Tarot")

# Carregue as imagens das cartas (coloque-as na pasta do projeto)
card_images = ["card1.png", "card2.png", "card3.png"]  # Exemplo

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Quando o jogador clica, revele uma carta aleatória
                random_card = random.choice(card_images)
                # Exiba a imagem da carta na tela

        # Atualize a tela
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()