import pygame
from parametrs import *
from sprites import Player, Coin


# игровое окно
pygame.init()  # запуск pygame
pygame.mixer.init()  # запуск работы звука

screen = pygame.display.set_mode((WIDTH, HEIGHT))  # размер дисплея
pygame.display.set_caption("Моя первая игра")  # заголовок
clock = pygame.time.Clock()  # переменная для работы с частотой кадров


# группы спрайтов
players_sprites = pygame.sprite.Group()  # создаю группу спрайтов
player = Player()  # создаю спрайт героя
players_sprites.add(player)  # добавляю спрайт в группу
items_sprites = pygame.sprite.Group()
coin = Coin()
items_sprites.add(coin)


running = True  # переменная для запуска игрового цикла
while running:  # запуск игрового цикла
    # контроль FPS
    clock.tick(FPS)

    players_sprites.update()  # обновление спрайтов
    # отрисовка
    screen.blit(background, (0, 0))
    players_sprites.draw(screen)  # отрисовка спрайтов на экране
    items_sprites.draw(screen)

    # после отрисовки, переворачиваем экран
    pygame.display.flip()
    # проверка на сбор спрайтов
    if pygame.sprite.spritecollide(player, items_sprites, False):
        items_sprites.update()

    # обработка событий
    for event in pygame.event.get():
        # проверка на закрытие игры
        if event.type == pygame.QUIT:
            running = False
        #проверка на нажатие клавиши
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.direction = 'LEFT'
        if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        player.direction = 'RIGHT'
        if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        player.direction = 'BOTTOM'
        if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        player.direction = 'TOP'



    # Отрисовка
    # Визуалицая(сборка)
pygame.quit()

