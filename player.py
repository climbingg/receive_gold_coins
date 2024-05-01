import pygame

# 初始化
pygame.init()

player_image = r"img\player.png"

class Player:
    def __init__(self, screenInfo):
        # 玩家
        self.player = pygame.image.load(player_image).convert_alpha()
        self.player = pygame.transform.scale(self.player, (self.player.get_width() // 4, self.player.get_height() // 4))

        # 玩家位置
        self.player_rect = self.player.get_rect()
        self.player_rect.x = screenInfo.current_w // 2 - self.player_rect.width // 2
        self.player_rect.y = screenInfo.current_h - self.player_rect.height

        # 螢幕資訊
        self.screenInfo = screenInfo

        # 分數
        self.score = 0

        # 生命
        self.life = 3

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.player_rect.x > 0:
                self.player_rect.x -= 10
        if keys[pygame.K_RIGHT]:
            if self.player_rect.x < self.screenInfo.current_w - self.player_rect.width:
                self.player_rect.x += 10