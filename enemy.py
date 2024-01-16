import random
import arcade

class Enemy(arcade.Sprite):
    def __init__(self , w , h):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.center_x = random.randint(0 ,w)
        self.center_y = h + 24
        self.angle = 180
        self.width = 30
        self.height = 30
        self.speed = 2
    def move(self):
         self.center_y -= self.speed
