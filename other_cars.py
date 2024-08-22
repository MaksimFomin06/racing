from random import randrange, seed, choice, randint
import pygame
seed(10)

class Opponent:
    def __init__(self, screen_width: int, screen_height: int)-> None:
        self.__start_x_lst = [169,285,410,535]
        self.car_lst: list = []
        self.car_rect_lst: list = []
        self.__stripe1 = 0
        self.__stripe2 = 0
        self.__stripe3 = 0
        self.__stripe4 = 0
        self.global_car = 0
        self.__speed = 2
        for i in range(1, 12):
            self.car_image = pygame.transform.smoothscale(
            pygame.image.load(f"images/car{i}.png").convert_alpha(),
            (100, 155)
            )
            self.car_rect = self.car_image.get_rect()
            self.car_rect.x = choice(self.__start_x_lst)
            self.car_rect.y = randrange(-3000, -100, 200)
        
            self.car_lst.append(self.car_image)
            self.car_rect_lst.append(self.car_rect)
        for car in self.car_rect_lst:
            if car.x == 169 and self.__stripe1 < 3:
                self.__stripe1 += 1
            elif car.x == 169 and self.__stripe1 == 3:
                car.x = 285
            if car.x == 285 and self.__stripe2 < 3:
                self.__stripe2 += 1
            elif car.x == 285 and self.__stripe2 == 3:
                car.x = 410
            if car.x == 410 and self.__stripe3 < 3:
                self.__stripe3 += 1
            elif car.x == 410 and self.__stripe3 == 3:
                car.x = 535
        
        #скорость
        self.__text_color = (25,0,0)
        self.__font_comicsans_speed = pygame.font.SysFont("comicsansms", 30)
        self.__speed_txt = self.__font_comicsans_speed.render(f"Скорость: {self.global_car}", True, self.__text_color)
        self.__speed_rect = self.__speed_txt.get_rect()
        self.__speed_rect.x = 550
        self.__speed_rect.y = 30
        #движение
       
        self.speed_button = self.__font_comicsans_speed.render(f"Скорость: {self.global_car}", True, self.__text_color)
        self.movement: dict[int, bool] = {pygame.K_a: False, pygame.K_d: False, pygame.K_s: False, pygame.K_w: False}
        self.__diagonal_movement_coefficient: float = 1 / (2**0.5) 

        
    def __print_speed(self) -> None:
        pass
        
        
    def check_logic(self) -> None:
        for car_rect in self.car_rect_lst:
            if car_rect.y > 1000:
                car_rect.y -= 3000
                car_rect.x = choice(self.__start_x_lst)
        
    def draw(self, screen) -> None:
        self.__print_speed()
        screen.blit(self.speed_button, (200,200))
        for car, rect in zip(self.car_lst, self.car_rect_lst):
            screen.blit(car, rect)
        screen.blit(self.__speed_txt, self.__speed_rect)
    
    def move(self) -> None:
        car.y += 3
        if self.movement[pygame.K_s] or self.movement[pygame.K_w]:
            for car in self.car_rect_lst:
                car.y += 3
                self.speed_button = self.__font_comicsans_speed.render(f"Скорость: {car.y}", True, self.__text_color)
                self.global_car = car.y
            
            
    #позиция курсора
    """def __move(self):
        self.__x, self.__y = pygame.mouse.get_pos()
        print(self.__x, self.__y)"""