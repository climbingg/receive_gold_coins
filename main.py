"""接金幣遊戲專案"""

import time
import os
import pygame


# 初始化
all_sprites = pygame.sprite.Group()

# 設定幀數
FPS = 60

# 設置視窗大小
WIDTH, HEIGHT = 1180 * 3, 548 * 3

# 設定常用RGB
BLACK = (0, 0, 0)


class Player(pygame.sprite.Sprite):
    """玩家角色"""

    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("img/mini_man.png"), (512, 512))
        # img/mini_man.png原本是1024, 1024 被改成512, 512
        self.rect = self.image.get_rect()
        self.rect.centery = HEIGHT - 250
        self.rect.centerx = WIDTH / 2

    def move_left(self):
        """向左移動"""
        self.rect.x -= 20
        if self.rect.left < 0:
            self.rect.left = 0

    def move_right(self):
        """向右移動"""
        self.rect.x += 20
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
    
    def update(self) -> None:
        """更新畫面"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.move_left()
        if keys[pygame.K_RIGHT]:
            self.move_right()
        


class Coin(pygame.sprite.Sprite):
    """金幣"""

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/coin.png")
        self.rect = self.image.get_rect()


def main() -> None:
    """主程式"""
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join("sound", "background.ogg"))
    pygame.mixer.music.play(-1)
    get_coins_sound = pygame.mixer.Sound("sound/get_gold_coins.wav")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("receve glod coins game")
    clock = pygame.time.Clock()
    # 引入圖片
    board = pygame.image.load("img/board.png")
    board = pygame.transform.scale(board, (1180 * 3, 548 * 3))
    mini_man = Player()
    all_sprites.add(mini_man)
    running = True
    pygame.display.update()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(FPS)
        screen.fill(BLACK)
        all_sprites.update()
        screen.blit(board, (0, 0))
        all_sprites.draw(screen)
        pygame.display.update()
    pygame.quit()


main()
