"""Модуль отвечающий за машину игрока."""

import pygame
import abc


class BasePlayerCar(abc.ABC):
    """Абстрактный класс машины."""

    @abc.abstractmethod
    def __init__(self, screen_width, screen_height) -> None:
        """Инициализация параметров машины."""
        self.__image_path: str
        self.car_rect: pygame.Rect
        self.__speed: int
        self.movement: dict[int, bool]
        self.__diagonal_movement_coefficient: float

    @abc.abstractmethod
    def move(self) -> None:
        """Движение машины."""

    @abc.abstractmethod
    def check_logic(self) -> None:
        """Обработка логики движения машины."""

    @abc.abstractmethod
    def draw(self, screen) -> None:
        """
        Отрисовка машины.

        :param screen: Экран игры
        :type screen: pygame.Surface
        """


class PlayerCar(BasePlayerCar):
    """Реализация машины в игре."""

    def __init__(self, screen_width, screen_height) -> None:
        """Инициализация параметров машины."""
        self.__image_path = pygame.transform.smoothscale(pygame.image.load("racing/images/car12.png").convert_alpha(), (95, 135))
        self.car_rect = self.__image_path.get_rect()
        self.car_rect.x = 160
        self.car_rect.y = screen_height - 190
        self.__speed = 8
        self.movement = {pygame.K_a: False, pygame.K_d: False, pygame.K_s: False, pygame.K_w: False}
        self.__diagonal_movement_coefficient = 1 / (2 ** 0.5)

    def move(self) -> None:
        """Движение машины."""
        if self.movement[pygame.K_a] or self.movement[pygame.K_d]:
            self.car_rect.x += (self.__speed * self.__diagonal_movement_coefficient * (self.movement[pygame.K_d] - self.movement[pygame.K_a]))
        else:
            self.car_rect.x += self.__speed * (self.movement[pygame.K_d] - self.movement[pygame.K_a])

    def check_logic(self):
        """Обработка логики движения машины."""
        if self.car_rect.x < 125:
            self.car_rect.x = 125
        elif self.car_rect.x > 575:
            self.car_rect.x = 575

    def draw(self, screen) -> None:
        """Отрисовка машины."""
        screen.blit(self.__image_path, self.car_rect)
