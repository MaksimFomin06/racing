import pygame

class GM_window:
    def __init__(self, screen_width: int = 800,
                 screen_height: int = 1000,
                 FPS: int = 60) -> None:
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
        #ГЛАВНОЕ МЕНЮ
        self.__font_comicsans = pygame.font.SysFont("comicsansms", 55)
        self.__text_color = (0, 0, 0)
        
        self.__main_m = self.__font_comicsans.render("ГЛАВНОЕ МЕНЮ", True, self.__text_color)
        self.__main_menu = self.__main_m.get_rect()
        self.__main_menu.x = 190
        self.__main_menu.y = 185    
        #ЗАНОВО
        self.__font_comicsans = pygame.font.SysFont("comicsansms", 55)
        self.__text_color = (0, 0, 0)
        
        self.__again = self.__font_comicsans.render("ЗАНОВО", True, self.__text_color)
        self.__again_button = self.__again.get_rect()
        self.__again_button.x = 280
        self.__again_button.y = 300
    def __del__(self) -> None:
        pygame.quit()
        
    def run(self) -> None:
        while not self.__game_end:
            self.__check_events()
            self.__draw()
            self.__clock.tick(self.__FPS)
            
    def __check_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_end = True
            elif event.type == pygame.KEYDOWN:
                """if event.key == pygame.K_SPACE:
                    menu = Old_Game()
                    menu.run()"""
                if event.key == pygame.K_ESCAPE:
                    self.__game_end = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.__main_menu.collidepoint(*pygame.mouse.get_pos()):
                        from menu import Menu
                        menu = Menu()
                        menu.run()
                    if self.__again_button.collidepoint(*pygame.mouse.get_pos()):
                        from old_racing import Old_Game
                        old_game = Old_Game()
                        old_game.run()
    def __draw(self) -> None:
        self.__screen.blit(self.__bg_screen, (0,0))
        self.__screen.blit(self.__main_m, (self.__main_menu.x, self.__main_menu.y))
        self.__screen.blit(self.__again, (self.__again_button.x, self.__again_button.y))
        pygame.display.flip()
        