from variable import *
from display import *

class App:
    def __init__(self):
        self.display = "Menu"
    
    def draw(self):
        screen.fill(cyan)

        if self.display == "Menu":
            self.display = Chinh()
        
        if self.display == "Them":
            self.display = Them()

        if self.display == "Add_bottle":
            self.display = Add_bottle()

        if self.display == "Add_car":
            self.display = Add_car()

        if self.display == "Add_active":
            self.display = Add_active()

        if self.display == "Nhat_Ky":
            self.display = Nhat_Ky()

    def run(self):
        run = True
        while run:
            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.update()
        
        pygame.quit()

if __name__ == "__main__":
    pygame.init()
    App().run()
    save_file(store)