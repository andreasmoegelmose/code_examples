import pygame

class Car:
    def __init__(self, starting_position):
        self.position = starting_position
        self.color = (255, 0, 0)
        self.size = (20, 30)

    def draw(self, screen):
        rect_pos = (self.position[0]-self.size[0]/2,
                    self.position[1]-self.size[1]/2)
        tire_size = (5, 10)
        pygame.draw.rect(screen, self.color,
                         (rect_pos, self.size))
        w, h = self.size
        for offset in ((-w/2-tire_size[0], -h/2), (w/2, -h/2), (-w/2-tire_size[0], h/2), (w/2, h/2)):
            x_offset, y_offset = offset
            y_offset -= tire_size[1]/2
            tire_pos = (self.position[0]+x_offset, self.position[1]+y_offset)
            pygame.draw.rect(screen, (0,0,0),
                            (tire_pos, tire_size))
        
    def drive(self, new_position):
        self.position = new_position

class Truck(Car):
    def __init__(self, starting_position):
        super().__init__(starting_position)
        self.cargo = Box(1000)
        self.crane = Crane()
        self.snowplow = None

    def offload(self):
        print("Offloading cargo...")

    def draw(self):
        print("Drawing truck...")

class Box:
    def __init__(self, weight):
        self.weight = weight

class Crane:
    def __init__(self):
        self.position = (0, 0)

    def move(self, new_position):
        self.position = new_position

def main():
    pygame.init()

    screen = pygame.display.set_mode((640, 480))

    car = Car((50, 50))
    print(f"Car is at: {car.position}")
    car.drive((200, 200))
    car.position = (300, 300)

    dumper = Truck((100, 100))
    dumper.drive((400, 400))
    dumper.offload()

    running = True
    while running:
        screen.fill((255, 255, 255))

        car.draw(screen)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()