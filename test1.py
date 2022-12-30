# https://docs.manim.community/en/stable/tutorials.html
# https://github.com/3b1b/manim
# https://github.com/ManimCommunity/manim
# https://plotly.com/python/animations/

from manim import *

config.background_color = DARK_GRAY

from manim import *

class PointMovingOnShapes(Scene):
    def construct(self):

        # Create a square
        square = Square(color=BLUE)
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)

        # Create a circle
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        # Create animations
        self.play(GrowFromCenter(square))
        self.play(Transform(square, circle))

        self.wait()
