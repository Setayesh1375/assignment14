import arcade

class Health ( arcade.Sprite ) :

    def __init__ ( self , x ) :
        super().__init__ ( "assignment14\heart2.png" )
        self.width = 22
        self.height = 22
        self.center_x = x
        self.center_y = 20
