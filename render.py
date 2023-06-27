from space import *
import arcade

SQUARE = 400

class Graph(object):

    def __init__(self) -> None:
        self.vectors = []
        self.motions = []
        self.routes = []

        # the size of one cell in pixels
        self.cell_size = 20

    def addVector(self, vector: object) -> None:
        self.vectors.append(vector)

    def addMotion(self, motion: object) -> None:
        self.motions.append(motion)

    def addRoute(self, route: object) -> None:
        self.routes.append(route)

    def setCellSize(self, size: int) -> None:
        if size <= 100:
            self.cell_size = size

    def run(self) -> None:
        arcade.open_window(SQUARE, SQUARE, "Graph")
        arcade.set_background_color(arcade.color.WHITE)

        arcade.start_render()

        self.constructGrid()
        for vector in self.vectors:
            self.constructVector(vector)

        for motion in self.motions:
            self.constructMotion(motion)

        for route in self.routes:
            self.constructRoute(route)

        arcade.finish_render()

        arcade.run()

    def constructGrid(self) -> None:
        size = self.cell_size

        # sum of cells
        cells = round(SQUARE / size)

        # vertical construction
        for i in range(1, cells):
            x = size * i
            if round(cells / 2) == i:
                arcade.draw_line(start_x = x, start_y = 0, end_x = x, end_y = SQUARE, color = arcade.color.BLACK, line_width = 2.5)
                arcade.draw_text("Y", x, SQUARE - 20, arcade.color.BLACK, 15)
            else:
                arcade.draw_line(start_x = x, start_y = 0, end_x = x, end_y = SQUARE, color = arcade.color.GRAY)

        # horizontal construction
        for i in range(1, cells):
            y = size * i
            if round(cells / 2) == i:
                arcade.draw_line(start_x = 0, start_y = y, end_x = SQUARE, end_y = y, color = arcade.color.BLACK, line_width = 2.5)
                arcade.draw_text("X", SQUARE - 20, y, arcade.color.BLACK, 15)
            else:
                arcade.draw_line(start_x = 0, start_y = y, end_x = SQUARE, end_y = y, color = arcade.color.GRAY)

    def constructVector(self, vector: object) -> None:
        size = self.cell_size
        # sum of cells
        cells = round(SQUARE / size)

        center = round((size * cells) / 2)

        x = vector.getX()
        y = vector.getY()
        arcade.draw_line(start_x = center, start_y = center, end_x = center + x * size, end_y = center + y * size, color = arcade.color.RED, line_width = 2.5)

    def constructMotion(self, motion: object) -> None:
        size = self.cell_size
        # sum of cells
        cells = round(SQUARE / size)
        center = round((size * cells) / 2)

        start_x = motion.getStartPoint().getX()
        start_y = motion.getStartPoint().getY()

        end_x = motion.getEndPoint().getX()
        end_y = motion.getEndPoint().getY()

        # drav a vector of the motion
        arcade.draw_line(
            start_x = center + start_x * size,
            start_y = center + start_y * size,
            end_x = center + end_x * size,
            end_y = center + end_y * size,
            color = arcade.color.GREEN,
            line_width = 2.5
        )

    def constructRoute(self, route: object) -> None:
        size = self.cell_size

        # sum of cells
        cells = round(SQUARE / size)
        center = round((size * cells) / 2)

        end_point = Location(0, 0, 0)

        for motion in route.getMotions():
            arcade.draw_line(
            start_x = center + end_point.getX() * size,
            start_y = center + end_point.getY() * size,
            end_x = center + motion.getEndPoint().getX() * size,
            end_y = center + motion.getEndPoint().getY() * size,
            color = arcade.color.BLUE,
            line_width = 2.5
            )

            end_point = motion.getEndPoint()