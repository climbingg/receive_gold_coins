"""接金幣遊戲專案"""

import random
import time
import os
import pygame


# 初始化
pygame.init()
pygame.mixer.init()
all_sprites = pygame.sprite.Group()

# 設定幀數
FPS = 60

# 設置視窗大小
WIDTH, HEIGHT = 1180 * 3, 548 * 3

# 設定常用RGB
BLACK = (0, 0, 0)

# 分數初始化
score = [0]

# 設定字體
font = pygame.font.SysFont("Arial", 108)
final_font = pygame.font.SysFont("Arial", 600)


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


mini_man = Player()


class Coin(pygame.sprite.Sprite):
    """金幣"""

    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("img/coin_1.png"), (100, 100))
        self.speed = random.randint(10, 20)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(200, 1180 * 3 - 200)
        self.rect.centery = 200

    def update(self) -> None:
        """更新畫面"""
        self.rect.y += self.speed
        if self.rect.bottom > HEIGHT:
            self.kill()
        if pygame.sprite.spritecollide(mini_man, [self], False):
            score[0] += 100
            self.kill()


def main() -> None:
    """主程式"""
    pygame.mixer.music.load(os.path.join("sound", "background.ogg"))
    pygame.mixer.music.play(-1)
    get_coins_sound = pygame.mixer.Sound("sound/get_gold_coins.wav")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("receve glod coins game")
    clock = pygame.time.Clock()
    # 引入圖片
    board = pygame.image.load("img/board.png")
    board = pygame.transform.scale(board, (1180 * 3, 548 * 3))
    all_sprites.add(mini_man)
    running = True
    pygame.display.update()
    t = time.time()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if time.time() - t > 20:
            screen.fill(BLACK)
            screen.blit(board, (0, 0))
            running = False
            all_sprites.empty()
            rendered_text = final_font.render(f"final score: {score[0]}", True, BLACK)
            text_rect = rendered_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
            screen.blit(rendered_text, text_rect)
            pygame.display.update()
            time.sleep(5)
            continue
        clock.tick(FPS)
        screen.fill(BLACK)
        if random.randint(1, 15) == 1:
            all_sprites.add(Coin())
        all_sprites.update()
        screen.blit(board, (0, 0))
        all_sprites.draw(screen)
        rendered_text = font.render(f"current score: {score[0]}", True, BLACK)
        text_rect = rendered_text.get_rect(center=(3000, 200))
        screen.blit(rendered_text, text_rect)
        pygame.display.update()
    pygame.quit()


main()
