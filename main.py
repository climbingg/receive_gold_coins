"""接金幣遊戲專案"""

import pygame
import pygame.freetype

from screen_main_page import ScreenSetting
from coin import Coin
from player import Player

# 初始化
pygame.init()

# 新增screen_setting
screen_main = ScreenSetting(pygame.display.Info())

# 初始化角色
player = Player(pygame.display.Info())

# 金幣列表
coins = []

# 字體
font_size = 36
font = pygame.freetype.Font(r"font\mexcellent.otf", font_size)

# 顯示分數、生命
def show_score(score, life):
    font.render_to(screen_main.screen, (4, 10), f"Score: {score}", (0, 0, 0), None, size=font_size)
    font.render_to(screen_main.screen, (4, 10 + font_size + 4), f"Life: {life}", (0, 0, 0), None, size=font_size)

# 初始化遊戲狀態
def init_game():
    player.__init__(pygame.display.Info())
    screen_main.__init__(pygame.display.Info())
    coins.clear()

again = False

while True:

    # 事件處理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            screen_main.quit()

    # 玩家移動
    if event.type == pygame.KEYDOWN:
        player.update()

    # 生成金幣
    if pygame.time.get_ticks() % 100 == 0:
        coin = Coin(pygame.display.Info())
        coins.append(coin)

    # 更新金幣
    for coin in coins:
        if coin.update():
            player.life -= 1
            coins.remove(coin)
            if player.life == 0:
                again = screen_main.game_over()

        # 碰撞偵測
        elif player.player_rect.colliderect(coin.coin_rect):
            coins.remove(coin)
            player.score += 1

    if again:
        init_game()
        again = False

    # 背景
    screen_main.screen.fill((255, 255, 255))

    # 繪製金幣
    for coin in coins:
        screen_main.screen.blit(coin.coin, coin.coin_rect)

    # 繪製玩家
    screen_main.screen.blit(player.player, player.player_rect)

    # 顯示分數、生命
    show_score(player.score, player.life)

    screen_main.clock.tick(screen_main.fps)
    pygame.display.update()
