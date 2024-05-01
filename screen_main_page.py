import pygame
import sys
import pygame.freetype

# 初始化
pygame.init()

# 死亡畫面
game_over_image = 'img/game_over.png'

# 重新開始按鈕
again_image = 'img/again.png'

# 字體
font_size = 72
font = pygame.freetype.Font(r"font\mexcellent.otf", font_size)

class ScreenSetting:
    def __init__(self, screenInfo):

        # 設定視窗(全螢幕)
        self.screen = pygame.display.set_mode((screenInfo.current_w, screenInfo.current_h), pygame.FULLSCREEN)
        self.screen.fill((255, 255, 255))

        self.fps = 60
        self.clock = pygame.time.Clock()

    def game_over(self):
        self.screen.fill((255, 255, 255))

        self.game_over_image = pygame.image.load(game_over_image)
        self.game_over_image = pygame.transform.scale(self.game_over_image, (self.game_over_image.get_width() // 2, self.game_over_image.get_height() // 2))
        self.screen.blit(self.game_over_image, (self.screen.get_width() // 2 - self.game_over_image.get_width() // 2, self.screen.get_height() // 2 - self.game_over_image.get_height() // 2 - self.screen.get_height() // 5))
        
        # 顯示結束文字
        text = "Game Over"
        text_width = int(font.get_rect(text).size[0])
        font.render_to(self.screen, (self.screen.get_width() // 2 - text_width // 2, self.screen.get_height() // 2), text, (0, 0, 0))
        
        self.again_icon = pygame.image.load(again_image)
        self.again_icon = pygame.transform.scale(self.again_icon, (self.again_icon.get_width() // 4, self.again_icon.get_height() // 4))
        self.screen.blit(self.again_icon, (self.screen.get_width() // 2 - self.again_icon.get_width() // 2, self.screen.get_height() // 2 + self.game_over_image.get_height() // 2 + self.again_icon.get_height() // 2 + 20))
        self.again_icon_rect = self.again_icon.get_rect(topleft=(self.screen.get_width() // 2 - self.again_icon.get_width() // 2, self.screen.get_height() // 2 + self.game_over_image.get_height() // 2 + self.again_icon.get_height() // 2 + 20))

        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.again_icon_rect.collidepoint(event.pos):
                        return True

    def quit(self):
        pygame.quit()
        sys.exit()