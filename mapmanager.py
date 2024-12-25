import pickle
class Mapmanager:
    def __init__(self):
        self.model = 'models/block'
        self.texture = 'textures/brick_stone.jpeg'
        self.colors = [
            (0.33, 0.55, 0.27, 1),
            (0.55, 0.27, 0.07, 1),
            (0.27, 0.54, 0.81, 1),
            (0.96, 0.82, 0.14, 1)
        ]

        self.start_new()

    def clear(self):
        self.land.removeNode()
        self.start_new()

    def set_color(self, z):
        if z < len(self.colors):
            return self.colors[z]
        else:
            #return self.colors[-1]
            return self.colors[z % len(self.colors)]


    def add_block(self, position: tuple, texture=None, color=None) -> None:
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(texture or self.texture))
        self.block.setColor(self.set_color(position[2]))
        self.block.setPos(position)
        self.block.setTag('at', str(position))
        self.block.reparentTo(self.land)

    def del_block(self, pos):
        blocks = self.find_blocks(pos)
        for block in blocks:
            block.removeNode()

    def build_block(self, pos):
        x, y, z = pos
        new =self.find_highest_empty(pos)
        if new[2] <= z + 1:
            self.add_block(new)

    def del_block_from(self, pos):
        x, y, z = self.find_highest_empty(pos)
        pos = x, y, z - 1
        blocks = self.find_blocks(pos)
        for block in blocks:
            block.removeNode()

    def find_blocks(self, pos):
        return self.land.findAllMatches('=at=' + str(pos))

    def is_empty(self, pos):
        blocks = self.find_blocks(pos)
        if blocks:
            return False
        else:
            return True

    def find_highest_empty(self, pos):
        x, y, z = pos
        z = 1
        while not self.is_empty((x, y, z)):
            z += 1
        return x, y, z


    def start_new(self):
       self.land = render.attachNewNode('Land')

    def load_map_from_file(self):
        self.clear()
        with open('maps/my_map.dat', 'rb') as file:
           len_blocks = pickle.load(file)
           for i in range(len_blocks):
               pos = pickle.load(file)
               self.add_block(pos)

    def load_map(self, filename):
        self.clear()
        with open(filename, 'r') as file:
            y = 0
            for line in file:
                x = 0
                line_lst = line.split(' ')
                for z in line_lst:
                    for z0 in range(int(z) + 1):
                        block = self.add_block((x, y, z0))
                    x += 1
                y += 1
            return x, y


    def save_map(self):
        blocks = self.land.getChildren()
        with open('maps/my_map.dat', 'wb') as file:
            pickle.dump(len(blocks), file)
            for block in blocks:
                x, y, z = block.getPos()
                pos = int(x), int(y), int(z)
                pickle.dump(pos, file)

