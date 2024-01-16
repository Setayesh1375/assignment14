import random
from typing import Optional
import arcade
from bullet import Bullet
from enemy import Enemy
from spaceship import Spaceship 



class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500 , height=600 , title="interstellar game 2023")
        arcade.set_background_color(arcade.color.UA_BLUE)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me = Spaceship(self.width)
        self.enemy_list = []

        

    #نمایش دادن
    def on_draw(self):
            arcade.start_render()
            arcade.draw_lrwh_rectangle_textured(0 , 0 , self.width , self.height ,self.background)
            self.me.draw()
            for doshman in self.enemy_list:
               doshman.draw()


            for bullet in self.me.bullet_list : 
                bullet.draw()

            arcade.finish_render()


    def on_key_press(self, symbol: int, modifiers: int):
         if symbol==arcade.key.A or symbol == arcade.key.LEFT: 
             self.me.change_x = -1  
         elif symbol==arcade.key.D or symbol == arcade.key.RIGHT: 
             self.me.change_x = 1  
         elif symbol == arcade.key.DOWN :
             self.me.change_x = 0
         elif symbol == arcade.key.SPACE :
             self.me.fire()
                
             
    def on_key_release(self, symbol: int, modifiers: int):
        self.me.change_x = 0


    #تابعی که تند تند به صورت اتوماتیک اجرا میشه
    # منطق    

    def on_update(self, delta_time: float):

        for doshman in self.enemy_list:
            if arcade.check_for_collision(self.me , doshman):
                print("Game Over")
                exit(0)

        self.me.move()

        for doshman in self.enemy_list:
           doshman.move()

        for bullet in self.me.bullet_list:
               bullet.move()

        for doshman in self.enemy_list:
            for bullet in self.me.bullet_list:
                if arcade.check_for_collision(doshman , bullet ):
                    self.enemy_list.remove(doshman)  
                    self.me.bullet_list.remove(bullet)    


        for doshman in self.enemy_list:
            if doshman.center_y < 0:
                self.enemy_list.remove(doshman)


        if random.randint(1,100) == 6:
            self.new_doshman = Enemy(self.width , self.height)
            self.enemy_list.append(self.new_doshman)

 

window = Game()             
arcade.run()
