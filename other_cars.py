from random import randrange, seed, choice, randint
from time import sleep
import pygame


class Opponent:
    def __init__(self, screen_width: int, screen_height: int)-> None:
        self.__start_x_lst = [169,285,410,535]
        self.car_lst: list = []
        self.car_rect_lst: list = []
        for i in range(1, 12):
            self.car_image = pygame.transform.smoothscale(
            pygame.image.load(f"images/car{i}.png").convert_alpha(),
            (100, 155)
            )
            self.car_rect = self.car_image.get_rect()
            self.car_rect.x = choice(self.__start_x_lst)
            self.car_rect.y = -200
            if len(self.car_rect_lst)>1:
                for car_lower in self.car_rect_lst:
                    if self.car_rect.colliderect(car_lower):
                        while self.car_rect.colliderect(car_lower):
                            self.car_rect.x = choice(self.__start_x_lst)
                    if self.car_rect.y <= car_lower.y:
                        if (self.car_rect.y * (-1)) - (car_lower.y * (-1)) < 380:
                            while (self.car_rect.y * (-1)) - (car_lower.y * (-1)) < 380:
                                self.car_rect.y -= 1
                    if self.car_rect.y >= car_lower.y:
                        if (car_lower.y * (-1)) - (self.car_rect.y * (-1)) < 380:
                            while (car_lower.y * (-1)) - (self.car_rect.y * (-1)) < 380:
                                car_lower.y -= 1
            self.car_lst.append(self.car_image)
            self.car_rect_lst.append(self.car_rect)
    def check_logic(self) -> None:
        for car_rect in self.car_rect_lst:
            if car_rect.y > 1000:
                car_rect.y -= 3200
                car_rect.x = choice(self.__start_x_lst)
    def draw(self, screen) -> None:
        for car, rect in zip(self.car_lst, self.car_rect_lst):
            screen.blit(car, rect)
    def move(self) -> None:
        for car in self.car_rect_lst:
                car.y += 5