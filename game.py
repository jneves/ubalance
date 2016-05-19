from microbit import Image, button_a, button_b, display, sleep

class Ball():
    def __init__(self, speed=100):
        self.speed = 100
        self.reset()
    
    def reset(self):
        self.lives = 9
        self.x = 2
        self.y = 2
        display.show(self.image())
        
    def move_up(self):
        if self.x == 0:
            self.lives -= 1
        else:
            self.x -= 1
        display.show(self.image())

    def move_down(self):
        if self.x == 4:
            self.lives -= 1
        else:
            self.x += 1
        display.show(self.image())

    def move_left(self):
        if self.y == 0:
            self.lives -= 1
        else:
            self.y -= 1
        display.show(self.image())

    def move_right(self):
        if self.y == 4:
            self.lives -= 1
        else:
            self.y += 1
        display.show(self.image())
            
    def image(self):
        if not self.lives:
            return Image.SAD

        s = ''
        for x in range(5):
            for y in range(5):
                if x == self.x and y == self.y:
                    s += str(self.lives)
                else:
                    s += '0'
            s += ':'
        return Image(s)


ball = Ball()
while True:
    sleep(100)
    if ball.lives:
        if button_a.was_pressed():
            ball.move_left()
        if button_b.was_pressed():
            ball.move_right()
    else:
        if button_a.was_pressed() or button_b.was_pressed():
            ball.reset()
