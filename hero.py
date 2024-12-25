from time import time

class Hero:
    def __init__(self, pos, land):
        self.camera_on = None
        self.mode = True
        self.land = land
        self.hero = loader.loadModel('smiley')
        self.hero.setColor(.95, .89, .2, 1)
        self.hero.setScale(.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)

        self.accept_events()

        self.damage_snd = base.loader.loadSfx("sounds/collision.ogg")
        self.up_snd = base.loader.loadSfx("sounds/up.mp3")

        self.last_move_sound_time = 0
        self.move_sound_delay = 0.3
        self.move_snd = base.loader.loadSfx('sounds/step.ogg')

    def camera_bind(self):
        '''Прикріплює камеру до гравця'''
        base.disableMouse()
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 1.5)
        base.camera.setH(180)
        self.camera_on = True

    def camera_up(self):
        '''Повертає камеру в режим спостерігача'''
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2] -3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.camera_on = False

    def switch_cam(self):
        '''переключає режим камери'''
        if self.camera_on:
            self.camera_up()
        else:
            self.camera_bind()

        start_snd = base.loader.loadSfx('sounds/change_mode.ogg')
        start_snd.set_volume(0.5)
        start_snd.setLoop(False)
        start_snd.play()


    def change_mode(self):
        """Перемикає режим руху героя між вільним та обмеженим."""
        if self.mode:
            self.mode = False
        else:
            self.mode = True

        start_snd = base.loader.loadSfx('sounds/pick.mp3')
        start_snd.set_volume(0.5)
        start_snd.setLoop(False)
        start_snd.play()

    def move_to(self, angle):
        '''Рухає героя в заданому напрямку залежно від режиму'''
        if self.mode:
            self.just_move(angle)
        else:
            self.try_move(angle)

    def try_move(self, angle):
        '''рух із перевіркою перешкод'''
        pos = self.look_at(angle)
        if self.land.is_empty(pos):
            pos = self.land.find_highest_empty(pos)
            self.hero.setPos(pos)
        else:
            pos = pos[0], pos[1], pos[2] + 1
            if self.land.is_empty(pos):
                self.up_snd.play()
                self.hero.setPos(pos)
            else:
                self.damage_snd.play()

        current_time = time()
        if current_time - self.last_move_sound_time > self.move_sound_delay:
            self.move_snd.set_volume(0.5)
            self.move_snd.setLoop(False)
            self.move_snd.play()
            self.last_move_sound_time = current_time

    def just_move(self, angle):
        '''рух гравця без перевірки перешкод'''
        pos = self.look_at(angle)
        self.hero.setPos(pos)

        current_time = time()
        if current_time - self.last_move_sound_time > self.move_sound_delay:
            self.move_snd.set_volume(0.5)
            self.move_snd.setLoop(False)
            self.move_snd.play()
            self.last_move_sound_time = current_time
    def check_dir(self, angle):
        ''' повертає заокруглені зміни координат X, Y,
        відповідні переміщенню у бік кута angle.
        Координата Y зменшується, якщо персонаж дивиться на кут 0,
        та збільшується, якщо дивиться на кут 180.
        Координата X збільшується, якщо персонаж дивиться на кут 90,
        та зменшується, якщо дивиться на кут 270.
            кут 0 (від 0 до 20) -> Y - 1
            кут 45 (від 25 до 65) -> X + 1, Y - 1
            кут 90 (від 70 до 110) -> X + 1
            від 115 до 155 -> X + 1, Y + 1
            від 160 до 200 -> Y + 1
            від 205 до 245 -> X - 1, Y + 1
            від 250 до 290 -> X - 1
            від 290 до 335 -> X - 1, Y - 1
            від 340 -> Y - 1
        '''
        if 0 <= angle <= 20:
            return 0, -1
        elif angle <= 65:
            return 1, -1
        elif angle <= 110:
            return 1, 0
        elif angle <= 155:
            return 1, 1
        elif angle <= 200:
            return 0, 1
        elif angle <= 245:
            return -1, 1
        elif angle <= 290:
            return -1, 0
        elif angle <= 335:
            return -1, -1
        else:
            return 0, -1

    def look_at(self, angle):
        '''Розраховує позицію, на яку гравець має переміститися'''
        from_x = round(self.hero.getX())
        from_y = round(self.hero.getY())
        from_z = round(self.hero.getZ())

        dx, dy = self.check_dir(angle)

        return from_x + dx, from_y + dy, from_z

    def turn_left(self):
        '''Повертання камери вліво'''
        self.hero.setH((self.hero.getH() + 5) % 360)

    def turn_right(self):
        '''Повертання камери впаво'''
        self.hero.setH((self.hero.getH() - 5) % 360)

    def forward(self):
        '''рух гравця вперед'''
        angle = self.hero.getH() % 360
        self.move_to(angle)

    def back(self):
        '''рух гравця назад'''
        angle = (self.hero.getH() + 180) % 360
        self.move_to(angle)

    def left(self):
        '''рух гравця вліво'''
        angle = (self.hero.getH() - 90) % 360
        self.move_to(angle)
    def right(self):
        '''рух гравця вправо'''
        angle = (self.hero.getH() + 90) % 360
        self.move_to(angle)

    def up(self):
        '''рух гравця вгору'''
        if self.mode:
            self.hero.setZ(self.hero.getZ() + 1)

    def down(self):
        '''рух гравця вниз'''
        if self.mode:
            self.hero.setZ(self.hero.getZ() - 1)

    def build(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.add_block(pos)
        else:
            self.land.build_block(pos)

        start_snd = base.loader.loadSfx('sounds/build.ogg')
        start_snd.set_volume(0.5)
        start_snd.setLoop(False)
        start_snd.play()


    def destroy(self):
        '''Руйнування блоку'''
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.del_block(pos)
        else:
            self.land.del_block_from(pos)

        start_snd = base.loader.loadSfx('sounds/break.ogg')
        start_snd.set_volume(0.5)
        start_snd.setLoop(False)
        start_snd.play()


    def accept_events(self):
        '''обробник подій'''
        base.accept('c', self.switch_cam)
        base.accept('arrow_left', self.turn_left)
        base.accept('arrow_left-repeat', self.turn_left)
        base.accept('arrow_right', self.turn_right)
        base.accept('arrow_right-repeat', self.turn_right)
        base.accept('w', self.forward)
        base.accept('w-repeat', self.forward)
        base.accept('s', self.back)
        base.accept('s-repeat', self.back)
        base.accept('a', self.right)
        base.accept('a-repeat', self.right)
        base.accept('d', self.left)
        base.accept('d-repeat', self.left)
        base.accept('arrow_up', self.up)
        base.accept('arrow_up-repeat', self.up)
        base.accept('arrow_down', self.down)
        base.accept('arrow_down-repeat', self.down)
        base.accept('z', self.change_mode)
        base.accept('b', self.build)
        base.accept('v', self.destroy)
        base.accept('k', self.land.save_map)
        base.accept('l', self.land.load_map_from_file)