"""接金幣遊戲專案"""

import time
import pygame


def main() -> None:
    """主程式"""
    pygame.init()
    pygame.mixer.init()
    # 設置視窗大小
    WIDTH, HEIGHT = 1180 * 3, 548 * 3
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("receve glod coins game")
    # 引入圖片
    board = pygame.image.load("img/board.png")
    board = pygame.transform.scale(board, (1180 * 3, 548 * 3))
    coin = pygame.image.load("img/coin.png")
    mini_man = pygame.image.load("img/mini_man.png")
    screen.blit(board, (0, 0))
    running = True
    pygame.display.update()
    while running:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            pass
        if keys[pygame.K_RIGHT]:
            pass
        break
    time.sleep(4)
    pygame.quit()


main()
