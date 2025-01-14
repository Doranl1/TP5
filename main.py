"""
Liam Doran
404
TP5
"""

import arcade
import random

YELLOW = (204, 153, 0)
BLUE = (175, 199, 237)
GREEN = (115, 240, 130)


class FishTank(arcade.Window):
    def __init__(self):
        super().__init__(700, 450, "fish")

        self.window_width = 700
        self.window_height = 450

        self.left_tank = self.window_width - 600
        self.right_tank = self.window_width - 100
        self.bottom_tank = self.window_height - 350
        self.top_tank = self.window_height - 50

        self.leaf_height = self.bottom_tank + 120

        self.rock_point = [
            (self.right_tank - 190, self.bottom_tank + 20),
            (self.right_tank - 180, self.bottom_tank + random.randint(30, 50)),
            (self.right_tank - 170, self.bottom_tank + random.randint(30, 50)),
            (self.right_tank - 160, self.bottom_tank + random.randint(30, 50)),
            (self.right_tank - 150, self.bottom_tank + random.randint(30, 50)),
            (self.right_tank - 140, self.bottom_tank + random.randint(30, 50)),
            (self.right_tank - 130, self.bottom_tank + random.randint(30, 50)),
            (self.right_tank - 120, self.bottom_tank + random.randint(30, 50)),
            (self.right_tank - 110, self.bottom_tank + random.randint(30, 50)),
            (self.right_tank - 100, self.bottom_tank + random.randint(30, 50)),
            (self.right_tank - 90, self.bottom_tank + random.randint(30, 50)),
            (self.right_tank - 80, self.bottom_tank + random.randint(30, 50)),
            (self.right_tank - 70, self.bottom_tank + random.randint(30, 50)),
            (self.right_tank - 30, self.bottom_tank + 20),
        ]

        self.x_fish = self.window_width - 175
        self.y_fish = self.window_height - 125

    def on_draw(self):

        arcade.set_background_color(arcade.color.WHITE)

        arcade.draw_lrbt_rectangle_filled(
            self.left_tank, self.right_tank, self.bottom_tank, self.top_tank, arcade.color.BLUEBERRY
        )
        arcade.draw_lrbt_rectangle_outline(
            self.left_tank, self.right_tank, self.bottom_tank, self.top_tank, arcade.color.BLACK, 5
        )

        arcade.draw_ellipse_filled(
            self.x_fish, self.y_fish, 75, 45, YELLOW
        )
        arcade.draw_circle_filled(
            self.x_fish + 20, self.y_fish + 10, 3.5, arcade.color.BLACK
        )
        arcade.draw_triangle_filled(
            self.x_fish, self.y_fish, self.x_fish - 50, self.y_fish + 30, self.x_fish - 50, self.y_fish - 30, YELLOW
        )

        arcade.draw_text("O", self.x_fish + 40, self.y_fish + 15, BLUE, 20, )
        arcade.draw_text("O", self.x_fish + 30, self.y_fish + 35, BLUE, 20, )
        arcade.draw_text("O", self.x_fish + 50, self.y_fish + 50, BLUE, 20, )

        arcade.draw_line(
            self.left_tank + 70, self.bottom_tank + 30, self.left_tank + 70, self.bottom_tank + 170, GREEN, 10
        )
        arcade.draw_circle_filled(
            self.left_tank + 70, self.bottom_tank + 30, 5, GREEN
        )
        arcade.draw_circle_filled(
            self.left_tank + 70, self.bottom_tank + 170, 5, GREEN
        )
        for i in range(0, 7):
            arcade.draw_arc_outline(
                self.left_tank + 70, self.leaf_height, 100, 100, GREEN, 35, 145, 10
            )
            self.leaf_height -= 20
        self.leaf_height += 140

        arcade.draw_polygon_filled(
            self.rock_point, arcade.color.BLACK
        )

        arcade.draw_text("poisson", self.window_width / 2 - 50, self.window_height - 35, BLUE, 20)


def main():
    draw = FishTank()
    # draw.on_draw()

    arcade.run()


main()
