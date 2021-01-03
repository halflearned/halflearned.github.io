from manimlib.imports import *


class Graphing(GraphScene):
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": -4,
        "y_max": 4,
        "graph_origin": ORIGIN,
        "function_color": WHITE,
        "axes_color": BLUE
    }

    def construct(self):
        # Make graph
        self.setup_axes(animate=True)
        graph_l = self.get_graph(func_l, WHITE)
        lab_l = self.get_graph_label(graph_l, label="L")

        graph_ln = self.get_graph(func_ln, RED)
        lab_ln = self.get_graph_label(graph_ln, label="L_{n}")

        theta = 0
        thetan = 1.5
        point_l_theta = Dot(self.coords_to_point(theta, func_l(theta)), color=WHITE)
        point_ln_theta = Dot(self.coords_to_point(theta, func_ln(theta)), color=YELLOW)
        point_l_thetan = Dot(self.coords_to_point(thetan, func_l(thetan)), color=BLUE)
        point_ln_thetan = Dot(self.coords_to_point(thetan, func_ln(thetan)), color=RED)

        # Line: R[theta] to R[thetan]
        line1_beg = self.coords_to_point(theta, func_l(theta))
        line1_end = self.coords_to_point(thetan, func_l(thetan))
        line1 = Line(line1_beg, line1_end, color=YELLOW)

        # Display graph
        self.play(ShowCreation(graph_l), Write(lab_l))
        self.add(point_l_theta)
        self.wait(1)
        self.add(point_l_thetan)
        self.wait(1)
        self.play(ShowCreation(line1))

        self.wait(2)
        self.play(ShowCreation(graph_ln), Write(lab_ln))
        self.add(point_ln_thetan)
        self.wait(1)
        self.add(point_ln_theta)
        self.wait(1)


def func_l(x):
    return (x + 0.5) ** 2 + 1


def func_ln(x):
    return (x - 1.2) ** 2 - 1.3 + np.random.normal(scale=0.05)
