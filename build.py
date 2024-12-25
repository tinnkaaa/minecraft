for y in range(2, 7):
    self.add_block((1, y, 1))

for y in range(8, 13):
    self.add_block((1, y, 1))

for x in range(2, 7):
    self.add_block((x, 13, 1))

for x in range(8, 13):
    self.add_block((x, 13, 1))

for y in range(8, 13):
    self.add_block((13, y, 1))

for y in range(2, 7):
    self.add_block((13, y, 1))

for x in range(8, 13):
    self.add_block((x, 7, 1))

for y in range(2, 7):
    self.add_block((7, y, 1))

for x in range(2, 7):
    self.add_block((x, 1, 1))

for x in range(8, 13):
    self.add_block((x, 1, 1))

self.add_block((1, 7, 1), texture='textures/spruce_log.jpg')
self.add_block((1, 13, 1), texture='textures/spruce_log.jpg')
self.add_block((7, 13, 1), texture='textures/spruce_log.jpg')
self.add_block((13, 13, 1), texture='textures/spruce_log.jpg')
self.add_block((13, 7, 1), texture='textures/spruce_log.jpg')
self.add_block((13, 1, 1), texture='textures/spruce_log.jpg')
self.add_block((1, 1, 1), texture='textures/spruce_log.jpg')
self.add_block((7, 1, 1), texture='textures/spruce_log.jpg')
self.add_block((7, 7, 1), texture='textures/spruce_log.jpg')

for y in range(1, 14):
    for z in (2, 3):
        self.add_block((1, y, z))

for x in range(2, 14):
    for z in (2, 3):
        self.add_block((x, 13, z))

for y in range(2, 14):
    for z in (2, 3):
        self.add_block((13, y, z))

for x in range(2, 14):
    for z in (2, 3):
        self.add_block((x, 1, z))

for x in range(8, 13):
    for z in (2, 3):
        self.add_block((x, 7, z))

for y in range(2, 8):
    for z in (2, 3):
        self.add_block((7, y, z))

for x in range(2, 7):
    for y in range(2, 13):
        for z in range(1, 4):
            self.add_block((x, y, z), texture='textures/spruce_boards.jpg')

for x in range(7, 13):
    for y in range(8, 13):
        for z in range(1, 4):
            self.add_block((x, y, z), texture='textures/spruce_boards.jpg')

for x in range(8, 13):
    for y in range(2, 7):
        for z in range(1, 4):
            self.add_block((x, y, z), texture='textures/spruce_boards.jpg')

for z in range(4, 9):
    self.add_block((1, 1, z), texture='textures/hewn_wood.jpg')

for z in range(4, 9):
    self.add_block((7, 1, z), texture='textures/hewn_wood.jpg')

for z in range(4, 9):
    self.add_block((13, 1, z), texture='textures/hewn_wood.jpg')

for z in range(4, 9):
    self.add_block((1, 7, z), texture='textures/hewn_wood.jpg')

for z in range(4, 9):
    self.add_block((7, 7, z), texture='textures/hewn_wood.jpg')

for z in range(4, 9):
    self.add_block((13, 7, z), texture='textures/hewn_wood.jpg')

for z in range(4, 9):
    self.add_block((1, 13, z), texture='textures/hewn_wood.jpg')

for z in range(4, 9):
    self.add_block((7, 13, z), texture='textures/hewn_wood.jpg')

for z in range(4, 9):
    self.add_block((13, 13, z), texture='textures/hewn_wood.jpg')

for y in range(1, 14):
    self.add_block((1, y, 9), texture='textures/hewn_wood.jpg')

for y in range(1, 14):
    self.add_block((13, y, 9), texture='textures/hewn_wood.jpg')

for x in range(2, 13):
    self.add_block((x, 1, 9), texture='textures/hewn_wood.jpg')

for x in range(2, 13):
    self.add_block((x, 13, 9), texture='textures/hewn_wood.jpg')

for x in range(7, 13):
    self.add_block((x, 7, 9), texture='textures/hewn_wood.jpg')

for y in range(2, 7):
    self.add_block((7, y, 9), texture='textures/hewn_wood.jpg')

for x in range(2, 7):
    for y in range(2, 13):
        self.add_block((x, y, 9), texture='textures/spruce_boards.jpg')

for x in range(7, 13):
    for y in range(8, 13):
        self.add_block((x, y, 9), texture='textures/spruce_boards.jpg')

for x in range(8, 13):
    for y in range(2, 7):
        self.add_block((x, y, 9), texture='textures/spruce_boards.jpg')

for x in range(2, 7):
    for z in range(4, 9):
        self.add_block((x, 1, z), texture='textures/birch_boards.jpg')

for y in range(2, 7):
    for z in range(4, 9):
        self.add_block((1, y, z), texture='textures/birch_boards.jpg')

for y in range(8, 13):
    for z in range(4, 9):
        self.add_block((1, y, z), texture='textures/birch_boards.jpg')

for x in range(2, 7):
    for z in range(4, 9):
        self.add_block((x, 13, z), texture='textures/birch_boards.jpg')

for x in range(8, 13):
    for z in range(4, 9):
        self.add_block((x, 13, z), texture='textures/birch_boards.jpg')

for x in range(2, 7):
    for z in range(4, 9):
        self.add_block((x, 7, z), texture='textures/birch_boards.jpg')

for y in range(8, 13):
    for z in range(4, 9):
        self.add_block((7, y, z), texture='textures/birch_boards.jpg')

for y in range(2, 7):
    for z in range(4, 9):
        self.add_block((7, y, z), texture='textures/birch_boards.jpg')

for x in range(8, 13):
    for z in range(4, 9):
        self.add_block((x, 7, z), texture='textures/birch_boards.jpg')

for y in range(8, 13):
    for z in range(4, 9):
        self.add_block((13, y, z), texture='textures/birch_boards.jpg')