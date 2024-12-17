"""
Liam Doran
404
TP5
"""

import arcade
import random


YELLOW = (204, 153, 0)

window_width = 700
window_height = 450

Left_tank = window_width - 600
Right_tank = window_width - 100
Bottom_tank = window_height - 350
Top_tank = window_height - 50

rock_point = [
    (Right_tank - 190, Bottom_tank + 20),
    (Right_tank - 180, Bottom_tank + random.randint(30, 50)),
    (Right_tank - 170, Bottom_tank + random.randint(30, 50)),
    (Right_tank - 160, Bottom_tank + random.randint(30, 50)),
    (Right_tank - 150, Bottom_tank + random.randint(30, 50)),
    (Right_tank - 140, Bottom_tank + random.randint(30, 50)),
    (Right_tank - 130, Bottom_tank + random.randint(30, 50)),
    (Right_tank - 120, Bottom_tank + random.randint(30, 50)),
    (Right_tank - 110, Bottom_tank + random.randint(30, 50)),
    (Right_tank - 100, Bottom_tank + random.randint(30, 50)),
    (Right_tank - 90, Bottom_tank + random.randint(30, 50)),
    (Right_tank - 80, Bottom_tank + random.randint(30, 50)),
    (Right_tank - 70, Bottom_tank + random.randint(30, 50)),
    (Right_tank - 30, Bottom_tank + 20),
]

X_Fish = window_width - 175
Y_Fish = window_height - 125


def draw():

    arcade.draw_lrbt_rectangle_filled(Left_tank, Right_tank, Bottom_tank, Top_tank, arcade.color.BLUEBERRY)
    arcade.draw_lrbt_rectangle_outline(Left_tank, Right_tank, Bottom_tank, Top_tank, arcade.color.BLACK, 5)



    arcade.draw_ellipse_filled(X_Fish, Y_Fish, 75, 45, YELLOW)
    arcade.draw_circle_filled(X_Fish + 20, Y_Fish + 10, 3.5, arcade.color.BLACK)
    arcade.draw_triangle_filled(X_Fish, Y_Fish, X_Fish - 50, Y_Fish + 30, X_Fish - 50, Y_Fish - 30, YELLOW)

    arcade.draw_polygon_filled(rock_point, arcade.color.BLACK)






def main():
    arcade.open_window(700, 450, "fish")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.start_render()
    draw()
    arcade.finish_render()

    arcade.run()


main()
