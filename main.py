"""
Liam Doran
404
TP5
"""

import arcade


YELLOW = (204, 153, 0)


def draw():

    arcade.draw_ellipse_filled(350, 225, 115, 75, YELLOW)
    arcade.draw_circle_filled(382.5, 240, 5, arcade.color.BLACK)
    arcade.draw_triangle_filled(350, 225, 275, 180, 275, 270, YELLOW)








def main():
    arcade.open_window(700, 450, "art")
    arcade.set_background_color(arcade.color.BLUEBERRY)
    arcade.start_render()
    draw()
    arcade.finish_render()

    arcade.run()


main()
