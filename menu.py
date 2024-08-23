import pygame
from old_racing import Old_Game

class Menu:
    def __init__(self, screen_width: int = 800, screen_height: int = 1000, FPS: int = 60) -> None:
        pygame.init()
        self.__width: int = screen_width
        self.__height: int = screen_height
        self.__screen: pygame.Surface = pygame.display.set_mode((self.__width, 
                                                                 self.__height))
        self.__bg_screen: str = pygame.transform.smoothscale(
            pygame.image.load("images/background1.jpg").convert_alpha(),(self.__width, self.__height))
        self.__FPS: int = FPS
        self.__clock: pygame.time.Clock = pygame.time.Clock()
        
        self.__game_end: bool = False
        
        self.__font_comicsans = pygame.font.SysFont("comicsansms", 100)
        self.__start = self.__font_comicsans.render("СТАРТ", True, self.__text_color)
        self.__start_rect = self.__start.get_rect(topleft=(250, 170))
        self.__old_game = Old_Game()
        self.__font_comicsans_exit = pygame.font.SysFont("comicsansms", 70)
        self.__exit_text = self.__font_comicsans_exit.render("ВЫЙТИ ИЗ ИГРЫ", True, self.__text_color)
        self.__exit_button = self.__exit_text.get_rect(topleft=(100, 370))
        self.__font_comicsans_ms = pygame.font.SysFont("comicsansms", 20)
        with open("data/max_score_tc.txt", "r") as file:
            self.__mscore_txt = file.read().strip()
        self.__max_score_text = self.__font_comicsans_ms.render(f"Лучший счет {self.__mscore_txt}", True, (255, 255, 255))
        self.__max_score_rect = self.__max_score_text.get_rect(topleft=(40, 40))
    def __del__(self) -> None:
        pygame.quit()
    def run(self) -> None:
        while not self.__game_end:
            self.__check_events()
            self.__draw()
            self.__clock.tick(self.__FPS)
            self.__max_score_print()
    def __max_score_print(self) -> None:
        self.__max_score_text = self.__font_comicsans_ms.render(f"Лучший счет {self.__mscore_txt}", True, (255,255,255))
    def __check_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_end = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.__old_game.run()
                elif event.key == pygame.K_ESCAPE:
                    self.__game_end = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.__start_rect.collidepoint(*pygame.mouse.get_pos()):
                        self.__old_game.run()
                    elif self.__exit_button.collidepoint(*pygame.mouse.get_pos()):
                        self.__game_end = True
    def __draw(self) -> None:
        self.__screen.blit(self.__bg_screen, (0,0))
        self.__screen.blit(self.__start, (self.__start_rect.x, self.__start_rect.y))
        self.__screen.blit(self.__exit_text, (self.__exit_button.x, self.__exit_button.y))
        self.__screen.blit(self.__max_score_text, (self.__max_score_rect.x, self.__max_score_rect.y))
        pygame.display.flip()