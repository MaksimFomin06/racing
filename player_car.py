import pygame
from other_cars import Opponent
class Player_Car:
    def __init__(self, screen_width: int, screen_height: int)-> None:
        #картинка
        self.__image_path: str = pygame.transform.smoothscale(pygame.image.load("images/car12.png").convert_alpha(),(105,155))
        self.car_rect: pygame.Rect = self.__image_path.get_rect()
        self.car_rect.x = 160
        self.car_rect.y = screen_height - 190
        #движение
        self.__speed = 4.5
        self.movement: dict[int, bool] = {pygame.K_a: False,pygame.K_d: False,}
        self.__diagonal_movement_coefficient: float = 1 / (2**0.5) 
        self.__opponent = Opponent(800,1000)
    def move(self)->None:
        if self.movement[pygame.K_a] or self.movement[pygame.K_d]:
            self.car_rect.x += (self.__speed * self.__diagonal_movement_coefficient * (self.movement[pygame.K_d] - self.movement[pygame.K_a]))
        else:
            self.car_rect.x += self.__speed * (self.movement[pygame.K_d] - self.movement[pygame.K_a])
    def check_logic(self):
        if self.car_rect.x < 125:
            pass
            #self.car_rect.x = 125
        elif self.car_rect.x > 575:
            self.car_rect.x = 575
    def draw(self, screen)-> None:
        screen.blit(self.__image_path, self.car_rect)

         