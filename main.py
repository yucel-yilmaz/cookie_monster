import pygame


def draw_maze(maze, start_pos, width, height, space):
    blank_rect = pygame.Rect(start_pos[0], start_pos[1], width, height)
    border_rect = pygame.Rect(16, 16, 48, 48)
    color_black = (0, 0, 0)
    color_border = (192, 192, 192)
    color_white = (229, 255, 204)
    color_gray = (100, 125, 150)
    w = len(maze[0])
    h = len(maze)
    current_rect = blank_rect
    current_border = border_rect
    for j in range(w):
        for i in range(h):
            if maze[i][j] == 0:
                pygame.draw.rect(screen, color_white, current_rect)
            elif maze[i][j] == 1:
                pygame.draw.rect(screen, color_gray, current_rect)
            else:
                pygame.draw.circle(screen, (153, 76, 0), (current_rect.centerx, current_rect.centery), 14, 0)

            # current_border = current_border.move((0, 28))
            current_rect = current_rect.move((0, height + space))
        # current_border = current_border.move((28, -28 * w))
        current_rect = current_rect.move(width + space, (-height - space) * w)


class Robot(object):
    def __init__(self, scr, start_pos, width, height, jump_space):
        self.screen = scr
        self.start_pos = start_pos
        self.width = width
        self.height = height
        self.jump_space = jump_space
        self.robot_color = (51, 153, 255)

        self.robot_base = pygame.Rect(start_pos[0], start_pos[1], self.width, self.height)

    def move_top(self):
        self.robot_base = self.robot_base.move(0, -self.height - self.jump_space)
        self.draw()

    def move_bottom(self):
        self.robot_base = self.robot_base.move(0, +self.height + self.jump_space)
        self.draw()

    def move_right(self):
        self.robot_base = self.robot_base.move(self.height + self.jump_space, 0)
        self.draw()

    def move_left(self):
        self.robot_base = self.robot_base.move(-self.height - self.jump_space, 0)
        self.draw()

    def draw(self):
        pygame.draw.rect(self.screen, self.robot_color, self.robot_base)
        pygame.display.flip()
        pygame.time.delay(500)


def play_robot(path, robot: Robot):
    robot.draw()
    for it in path:
        if it == 0:
            robot.move_top()
        elif it == 1:
            robot.move_bottom()
        elif it == 2:
            robot.move_right()
        elif it == 3:
            robot.move_left()


mz = [[0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
      [0, 2, 0, 1, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
      [0, 2, 0, 0, 0, 2, 2, 2, 0, 0],
      [0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
      [0, 0, 1, 0, 2, 1, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
      [0, 2, 1, 0, 1, 1, 1, 1, 1, 1],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

route = [1, 1, 1, 3, 1, 3, 3, 1, 3, 0, 3, 1, 1, 3, 0, 3, 0, 3, 0, 0, 0, 3, 1, 1, 1, 1, 1, 1, 2, 1]

pygame.init()
scr_width = 500
scr_height = 500

# @start_pos : maze and robot start position (pixel value)
# @width, @height : maze and robot rectangle distance
# @space: maze matrix rectangle margin space
# @row, @column: robot start point maze matrix
start_pos, width, height, space, row, column = (20, 20), 40, 40, 4, 1, 10
rbt_pos = x, y = start_pos[0] + (width + space) * (column - 1), start_pos[1] + (height + space) * (row - 1)

maze_size = r, c = len(mz), len(mz[0])

scr_width = int((width + space) * c + start_pos[0]*2)
scr_height = int((height + space) * r + start_pos[1]*2)

screen = pygame.display.set_mode((scr_width, scr_height))
title = pygame.display.set_caption("Cookie Monster")
run = True

rbt = Robot(screen, rbt_pos, width, height, space)

while run:
    pygame.time.delay(1000)
    screen.fill((224, 224, 224))

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            quit()
    draw_maze(mz, start_pos, width, height, space)

    pygame.time.delay(1000)
    play_robot(route, rbt)
    pygame.display.flip()
    run = False
