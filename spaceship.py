import arcade
from bullet import Bullet

class Spaceship(arcade.Sprite):
    def __init__(self , w):
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png")
        self.center_x = w / 2
        self.center_y = 80
        self.change_x = 0
        self.change_y = 0
        self.width = 35
        self.height = 35
        self.speed = 4
        self.game_width = w
        self.bullet_list = []

    def move(self):
        if self.change_x == -1:
            if self.center_x > 0:
              self.center_x -=  self.speed

        elif self.change_x == 1:
            if self.center_x < self.game_width :
               self.center_x +=  self.speed

        elif self.change_y == 1 :
            if self.center_y < self.game_height:
                self.center_y += self.speed
                
        elif self.change_y == -1 :
            if self.center_y > 0:
                self.center_y -= self.speed


    def fire(self):
        new_bullet = Bullet(self)
        self.bullet_list.append(new_bullet)
