import pygame
import pygame, ctypes


class Pause:
    def __init__(self, 
                 screen_width: int = 800,
                 screen_height: int = 1000,
                 fps: int = 60):
        pygame.init()
        self.__width: int = screen_width
        self.__height: int = screen_height
        self.__screen: pygame.Surface = pygame.display.set_mode((self.__width,
                                                                 self.__height))
        self.__bg_screen: str = pygame.transform.smoothscale(
            pygame.image.load("images/background1.jpg").convert_alpha(), 
                                                 (self.__width, self.__height))
        
        self.__fps: int = fps
        self.__clock: pygame.time.Clock = pygame.time.Clock()
        
        self.__game_end: bool = False        
        #работа с текстом 
        #ПРОДОЛЖИТЬ
        self.__font_comicsans = pygame.font.SysFont("comicsansms", 55)
        self.__text_color = (0, 0, 0)
        
        self.__continue = self.__font_comicsans.render("ПРОДОЛЖИТЬ", True, self.__text_color)
        self.__continue_rect = self.__continue.get_rect()
        self.__continue_rect.x = 200
        self.__continue_rect.y = 220
        #ВЫЙТИ В МЕНЮ
        self.__font_comicsans = pygame.font.SysFont("comicsansms", 55)
        self.__text_color = (0, 0, 0)
        
        self.__exit_in_menu = self.__font_comicsans.render("ВЫЙТИ В МЕНЮ", True, self.__text_color)
        self.__exit_in_menu_rect = self.__exit_in_menu.get_rect()
        self.__exit_in_menu_rect.x = 165
        self.__exit_in_menu_rect.y = 370
        
        
    def run(self):
        while not self.__game_end:
            self.__check_events()
            self.__draw()
            self.__clock.tick(self.__fps)
    def __check_events(self)-> None:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_end = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.__exit_in_menu_rect.collidepoint(*pygame.mouse.get_pos()):
                        from menu import Menu
                        menu = Menu()
                        menu.run()
                    elif self.__continue_rect.collidepoint(*pygame.mouse.get_pos()):
                        self.__game_end = True
                        
    def __draw(self)-> None:
        self.__screen.blit(self.__bg_screen, (0, 0))
        self.__screen.blit(self.__exit_in_menu, self.__exit_in_menu_rect)
        self.__screen.blit(self.__continue, self.__continue_rect)
        
        pygame.display.flip()