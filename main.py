"""
Liam Doran
404
TP5
"""

import arcade
import random
import math

YELLOW = (204, 153, 0)
BLUE = (175, 199, 237)
GREEN = (115, 240, 130)


class FishTank(arcade.Window):
    def __init__(self):
        super().__init__(700, 450, "Poisson")

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

        self.x_fish = random.randint(self.left_tank + 70, self.right_tank - 100)
        self.y_fish = random.randint(self.bottom_tank + 40, self.top_tank - 50)
        self.go_x_fish = random.randint(self.left_tank + 70, self.right_tank - 100)
        self.go_y_fish = random.randint(self.bottom_tank + 40, self.top_tank - 50)
        self.difference_x = 0
        self.difference_y = 0
        self.distance = 0
        self.x_check = 0
        self.change = 1

        self.x_fish2 = random.randint(self.left_tank + 70, self.right_tank - 100)
        self.y_fish2 = random.randint(self.bottom_tank + 40, self.top_tank - 50)
        self.go_x_fish2 = random.randint(self.left_tank + 70, self.right_tank - 100)
        self.go_y_fish2 = random.randint(self.bottom_tank + 40, self.top_tank - 50)
        self.difference_x2 = 0
        self.difference_y2 = 0
        self.distance2 = 0
        self.x_check2 = 0
        self.change2 = 1

    def on_draw(self):

        arcade.set_background_color(arcade.color.WHITE)

        arcade.draw_lrbt_rectangle_filled(
            self.left_tank, self.right_tank, self.bottom_tank, self.top_tank, arcade.color.BLUEBERRY
        )
        arcade.draw_lrbt_rectangle_outline(
            self.left_tank, self.right_tank, self.bottom_tank, self.top_tank, arcade.color.BLACK, 5
        )

        # arcade.draw_circle_outline(self.x_fish + 50, self.y_fish + 15, 7, BLUE, 2)
        # arcade.draw_circle_outline(self.x_fish + 30, self.y_fish + 35, 7, BLUE, 2)
        # arcade.draw_circle_outline(self.x_fish + 50, self.y_fish + 50, 7, BLUE, 2)

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

        # Poisson
        arcade.draw_ellipse_filled(
            self.x_fish2, self.y_fish2, 75, 45, arcade.color.GREEN
        )
        arcade.draw_circle_filled(
            self.x_fish2 + 20 * self.change2, self.y_fish2 + 10, 3.5, arcade.color.BLACK
        )
        arcade.draw_triangle_filled(
            self.x_fish2, self.y_fish2,
            self.x_fish2 - 50 * self.change2,
            self.y_fish2 + 30 * self.change2,
            self.x_fish2 - 50 * self.change2, self.y_fish2 - 30 * self.change2,
            YELLOW
        )

        arcade.draw_ellipse_filled(
            self.x_fish, self.y_fish, 75, 45, YELLOW
        )
        arcade.draw_circle_filled(
            self.x_fish + 20 * self.change, self.y_fish + 10, 3.5, arcade.color.BLACK
        )
        arcade.draw_triangle_filled(
            self.x_fish, self.y_fish,
            self.x_fish - 50 * self.change,
            self.y_fish + 30 * self.change,
            self.x_fish - 50 * self.change, self.y_fish - 30 * self.change,
            YELLOW
        )

    def on_update(self, delta_time: float):

        if self.x_fish != self.go_x_fish and self.y_fish != self.go_y_fish:
            self.difference_x = self.go_x_fish - self.x_fish
            self.difference_y = self.go_y_fish - self.y_fish
            self.distance = math.sqrt(self.difference_x ** 2 + self.difference_y ** 2)

            self.x_fish += self.difference_x / self.distance
            self.y_fish += self.difference_y / self.distance

            self.x_check = abs(self.difference_x)
            if self.x_check <= 1:
                self.x_fish = self.go_x_fish

            if self.difference_x < 0:
                self.change = -1
            else:
                self.change = 1


        elif round(self.x_fish, 0) == round(self.go_x_fish, 0):

            self.go_x_fish = random.randint(self.left_tank + 70, self.right_tank - 100)
            self.go_y_fish = random.randint(self.bottom_tank + 40, self.top_tank - 50)

        else:
            pass


        if self.x_fish2 != self.go_x_fish2 and self.y_fish2 != self.go_y_fish2:
            self.difference_x2 = self.go_x_fish2 - self.x_fish2
            self.difference_y2 = self.go_y_fish2 - self.y_fish2
            self.distance2 = math.sqrt(self.difference_x2 ** 2 + self.difference_y2 ** 2)

            self.x_fish2 += self.difference_x2 / self.distance2
            self.y_fish2 += self.difference_y2 / self.distance2

            self.x_check2 = abs(self.difference_x2)
            if self.x_check2 <= 1:
                self.x_fish2 = self.go_x_fish2

            if self.difference_x2 < 0:
                self.change2 = -1
            else:
                self.change2 = 1


        elif round(self.x_fish, 0) == round(self.go_x_fish, 0):

            self.go_x_fish = random.randint(self.left_tank + 70, self.right_tank - 100)
            self.go_y_fish = random.randint(self.bottom_tank + 40, self.top_tank - 50)



def main():
    FishTank()

    arcade.run()


main()
