from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero

class Game(ShowBase):
    def __init__(self):
        super().__init__()
        base.camLens.setFov(90)

        #start_snd = base.loader.loadSfx('sounds/inecraft_forest.ogg')
        #start_snd.set_volume(0.4)
        #start_snd.play()

        self.land = Mapmanager()
        x, y = self.land.load_map('maps/mini_labirint.txt')
        self.hero = Hero((31, 1, 1), self.land) #(31, 1, 1)

game = Game()
game.run()