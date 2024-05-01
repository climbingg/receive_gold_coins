import pygame
import random

# 初始化
pygame.init()

# 金幣圖片列表
coin_images = [r"img\coin_black_1.png"]

# 計算金幣生成數量
coin_count = 0

# 金幣掉落速度
coin_speed = 5

class Coin:
    def __init__(self, screenInfo):
        # 金幣
        self.coin = pygame.image.load(coin_images[0]).convert_alpha()
        self.coin = pygame.transform.scale(self.coin, (self.coin.get_width() // 16, self.coin.get_height() // 16))

        # 隨機生成金幣位置
        self.coin_rect = self.coin.get_rect()
        self.coin_rect.x = random.randint(screenInfo.current_w // 2 - 700, screenInfo.current_w // 2 + 700)
        self.coin_rect.y = -self.coin_rect.height

        self.screenInfo = screenInfo

    def update(self):
        self.coin_rect.y += coin_speed
        if self.coin_rect.y > self.screenInfo.current_h:
            return True
            
        
