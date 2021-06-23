from manim import *
class OpeningManim(Scene):
    def construct(self):
        title = Tex("This is some \\LaTeX")
        basel = MathTex("\\sum_{n=1}^\\infty " "\\frac{1}{n^2} = \\frac{\\pi^2}{6}")
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeInFrom(basel, UP),
        )
        self.wait()

        transform_title = Tex("That was a transform")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*map(lambda obj: FadeOutAndShift(obj, direction=DOWN), basel)),
        )
        self.wait()

        grid = NumberPlane()
        grid_title = Tex("This is a grid")
        grid_title.scale(1.5)
        grid_title.move_to(transform_title)

        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            FadeOut(title),
            FadeInFrom(grid_title, direction=DOWN),
            ShowCreation(grid, run_time=3, lag_ratio=0.1),
        )
        self.wait()

        grid_transform_title = Tex(
            "That was a non-linear function \\\\" "applied to the grid"
        )
        grid_transform_title.move_to(grid_title, UL)
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.apply_function,
            lambda p: p
                      + np.array(
                [
                    np.sin(p[1]),
                    np.sin(p[0]),
                    0,
                ]
            ),
            run_time=3,
        )
        self.wait()
        self.play(Transform(grid_title, grid_transform_title))
        self.wait()
