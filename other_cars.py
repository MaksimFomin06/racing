from random import randrange, seed, choice, randint
import pygame
seed(10)

class Opponent:
    def __init__(self, screen_width: int, screen_height: int)-> None:
        self.__start_x_lst = [169,285,410,535]
        self.__test = 0
        self.car_lst: list = []
        self.car_rect_lst: list = []
        for i in range(1, 12):
            self.car_image = pygame.transform.smoothscale(
            pygame.image.load(f"images/car{i}.png").convert_alpha(),
            (100, 155)
            )
            self.car_rect = self.car_image.get_rect()
            self.car_rect.x = choice(self.__start_x_lst)
            self.car_rect.y = randrange(-3000, -100, 155)
        
            self.car_lst.append(self.car_image)
            self.car_rect_lst.append(self.car_rect)
        
    """def __check_spawn(self) -> None:
        for car1, car2 in zip(self.car_rect_lst, self.car_rect_lst):
            if car1.colliderect(car2):
                car2.x += 20
    """
    def draw(self, screen) -> None:
        
        for car, rect in zip(self.car_lst, self.car_rect_lst):
            screen.blit(car, rect)
        """
        screen.blit(self.__car1, self.__car1_rect)
        screen.blit(self.__car2, self.__car2_rect)
        screen.blit(self.__car3, self.__car3_rect)
        screen.blit(self.__car4, self.__car4_rect)
        screen.blit(self.__car5, self.__car5_rect)
        
        """
        
    
    def move(self) -> None:
        for car in self.car_rect_lst:
            car.y += 3
        
    def check_logic(self) -> None:
        for car_rect in self.car_rect_lst:
            if car_rect.y > 1000:
                car_rect.y = randrange(-2000, -100, 200)
                car_rect.x = choice(self.__start_x_lst)
        
            
            
    #позиция курсора
    """def __move(self):
        self.__x, self.__y = pygame.mouse.get_pos()
        print(self.__x, self.__y)"""