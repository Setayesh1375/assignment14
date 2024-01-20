import time
import random
import arcade
from bullet import Bullet
from enemy import Enemy
from spaceship import Spaceship 
from health import Health



class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500 , height=600 , title="interstellar game 2023")
        arcade.set_background_color(arcade.color.UA_BLUE)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.gameover_background = arcade.load_texture ( "assignment14\game over.png" )
        self.mode = None
        self.score = 0
        self.enemy_speed = 3
        self.timer = time.time ()
        self.me = Spaceship(self.width)
        self.enemy_list = []
        self.health_list = []
        self.health_x = 15
        self.health_number = 3
        self.fire_voice = arcade.load_sound ( ":resources:sounds/laser4.wav" )
        self.explode = arcade.load_sound ( ":resources:sounds/gameover3.wav" )
        for i in range ( self.health_number ) :
            new_health = Health ( self.health_x )
            self.health_list.append ( new_health )
            self.health_x += 25
        

    #نمایش دادن
    def on_draw(self):
            arcade.start_render()

            if self.mode == "Game_over" :
                arcade.set_background_color ( arcade.color.BLACK )
                arcade.draw_lrwh_rectangle_textured ( 0 , 0 , self.width , self.height , self.gameover_background )
                score_text = f" Final Score : { self.score }"
                arcade.draw_text ( score_text , ( self.width // 2 ) - 90 , 35 , arcade.color.BLACK , 25)
            
            else :
                arcade.set_background_color ( arcade.color.DARK_BLUE)
                arcade.draw_lrwh_rectangle_textured ( 0 , 0 , self.width , self.height , self.background )

            
            self.me.draw()

            for enemy in self.enemy_list:
                enemy.draw()


            for bullet in self.me.bullet_list : 
                bullet.draw()

            for health in self.health_list :
                health.draw ()

            score_text = f" Score : { self.score }" 
            arcade.draw_text ( score_text , self.width - 130 , 12 , arcade.color.BLACK , 16 )    

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
             arcade.play_sound ( self.fire_voice )
                
             
    def on_key_release(self, symbol: int, modifiers: int):
        self.me.change_x = 0


    #تابعی که تند تند به صورت اتوماتیک اجرا میشه
    # منطق    

    def on_update(self, delta_time):

        self.me.move ()

        for bullet in self.me.bullet_list :
            bullet.move ()
        
        for enemy in self.enemy_list :
            enemy.move ()

        for enemy in self.enemy_list :
            if enemy.center_y <= 0 and len ( self.health_list ) > 0 :
                self.enemy_list.remove ( enemy )
                self.health_list.pop ( self.health_number - 1 )
                self.health_number -= 1
        
        for bullet in self.me.bullet_list :
            if bullet.center_y >= self.height :
                self.me.bullet_list.remove ( bullet )

        if time.time () >= self.timer + 3 :
            new_enemy = Enemy ( self , self.enemy_speed )
            self.enemy_list.append ( new_enemy )
            self.enemy_speed += 0.1
            self.timer = time.time ()

        if self.health_number == 0 :
            self.mode = "Game_over"

        for enemy in self.enemy_list :
            if arcade.check_for_collision ( self.me , enemy ) :
                self.mode = "Game_over"

        for enemy in self.enemy_list :
            for bullet in self.me.bullet_list :
                if arcade.check_for_collision ( enemy , bullet ) :
                    self.enemy_list.remove ( enemy )
                    self.me.bullet_list.remove ( bullet )
                    arcade.play_sound ( self.explode )
                    self.score += 1
        
        
        if random.randint(1,100) == 6:
            self.new_enemy = Enemy(self.width , self.height)
            self.enemy_list.append(self.new_enemy)

 

window = Game()             
arcade.run()
