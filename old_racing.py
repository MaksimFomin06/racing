import pygame
from time import sleep
from player_car import Player_Car
from other_cars import Opponent
from pause import Pause

class Old_Game:
    def __init__(self, screen_width: int = 800,
                 screen_height: int = 1000,
                 FPS: int = 60)-> None:
        pygame.init()
        self.__screen_width: int = screen_width
        self.__screen_height: int = screen_height
        self.__screen: pygame.Surface = pygame.display.set_mode(
            (self.__screen_width, self.__screen_height)
        )
        self.__bg_screen: str = pygame.transform.smoothscale(pygame.image.load("images/track.png").convert(),(self.__screen_width, self.__screen_height))
        self.__bg_y = 0
        self.__FPS: int = FPS
        self.__clock: pygame.time.Clock = pygame.time.Clock()
        self.__pause: str = pygame.transform.smoothscale(
            pygame.image.load("images/pause-button.png").convert_alpha(),
            (80,80)
        )
        self.__pause_rect: pygame.Rect = self.__pause.get_rect()
        self.__pause_rect.x = self.__screen_width - 85
        self.__pause_rect.y = 5
        self.__game_end: bool = False
        self.__opponent = Opponent(self.__screen_width, self.__screen_height)
        self.__car = Player_Car(self.__screen_width, self.__screen_height)
        self.__score: int = 0
        with open("data/max_score_tc.txt", "r") as file:
            self.max_score = int(file.read().strip())
        self.__score_txt = str(int(self.__score))
        self.__font_comicsans = pygame.font.SysFont("comicsansms", 55)
        self.__text_color = (255, 0, 0)
        self.__score_button = self.__font_comicsans.render(f"{self.__score_txt}", True, self.__text_color)
        self.__score_button_rect = self.__score_button.get_rect()
        self.__score_button_rect.x = 30
        self.__score_button_rect.y = 50
    
    def __del__(self) -> None:
        pygame.quit()
    def run(self) -> None:
        while not self.__game_end:
            self.__check_events()
            self.__draw()
            self.__clock.tick(self.__FPS)
            self.__move_objects()
            self.__check_collision()
            self.__bg_y += 8
            if self.__bg_y == 1000:
                self.__bg_y = 0
    def __check_events(self) -> None:
        event: pygame.event.Event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_end = True
            elif event.type == pygame.KEYDOWN and event.key in self.__car.movement:
                self.__car.movement[event.key] = True
            elif event.type == pygame.KEYUP and event.key in self.__car.movement:
                self.__car.movement[event.key] = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.__pause_rect.collidepoint(*pygame.mouse.get_pos()):
                        menu = Pause()
                        menu.run()
    def __move_objects(self) -> None:
        self.__car.move()
        self.__car.check_logic()
        self.__opponent.move()
        self.__opponent.check_logic()
        self.__print_score()
    def __check_collision(self) -> None:
        for car in self.__opponent.car_rect_lst:
            if self.__car.car_rect.colliderect(car):
                self.__max_score_counter()
                from gameover_window import GM_window
                gm = GM_window()
                gm.run()
    def __print_score(self) -> None:
        self.__score_txt = str(int(self.__score))
        self.__score_button = self.__font_comicsans.render(f"{self.__score_txt}", True, self.__text_color)
        self.__score += 0.01
    def __max_score_counter(self) -> None:
        self.__score += 0.01
        if self.max_score < self.__score:
            self.test_txt = open("data/max_score_tc.txt", "w")
            self.test_txt.write(str(int(self.__score)))
            self.test_txt.close()
    def __draw(self) -> None:
        self.__screen.blit(self.__bg_screen, (0, self.__bg_y))
        self.__screen.blit(self.__bg_screen, (0, self.__bg_y - 1000))
        self.__screen.blit(self.__pause, self.__pause_rect)
        self.__car.draw(self.__screen)
        self.__opponent.draw(self.__screen)
        self.__screen.blit(self.__score_button, (self.__score_button_rect.x, self.__score_button_rect.y))
        pygame.display.flip()
        
