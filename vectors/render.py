import arcade

SQUARE = 400
CELL_SIZE = 20

def graph(vectors: len) -> None:
    arcade.open_window(SQUARE, SQUARE, "Graph")
    arcade.set_background_color(arcade.color.WHITE)

    arcade.start_render()

    # sum of cells
    cells = round(SQUARE / CELL_SIZE)

    # vertical construction
    for i in range(1, cells):
        x = CELL_SIZE * i
        if round(cells / 2) == i:
            arcade.draw_line(start_x = x, start_y = 0, end_x = x, end_y = SQUARE, color = arcade.color.BLACK, line_width = 2.5)
            arcade.draw_text("Y", x, SQUARE - 20, arcade.color.BLACK, 15)
        else:
            arcade.draw_line(start_x = x, start_y = 0, end_x = x, end_y = SQUARE, color = arcade.color.GRAY)

    # horizontal construction
    for i in range(1, cells):
        y = CELL_SIZE * i
        if round(cells / 2) == i:
            arcade.draw_line(start_x = 0, start_y = y, end_x = SQUARE, end_y = y, color = arcade.color.BLACK, line_width = 2.5)
            arcade.draw_text("X", SQUARE - 20, y, arcade.color.BLACK, 15)
        else:
            arcade.draw_line(start_x = 0, start_y = y, end_x = SQUARE, end_y = y, color = arcade.color.GRAY)

    for vector in vectors:
        center = round((CELL_SIZE * cells) / 2)
        arcade.draw_line(start_x = center, start_y = center, end_x = center + vector.x * CELL_SIZE, end_y = center + vector.y * CELL_SIZE, color = arcade.color.RED, line_width = 2.5)

    arcade.finish_render()
    arcade.run()
