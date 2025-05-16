from manim import *

class FordFulkersonStepByStep(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # Title
        title = Text("Ford-Fulkerson Algorithm", font_size=52, color=WHITE)
        subtitle = Text("Salih Çimen", font_size=48, color=WHITE).next_to(title, DOWN)

        title.shift(UP * 2.5)
        subtitle.shift(UP * 2.5)
        self.play(title.animate.shift(DOWN * 2.5), run_time=1.8)
        self.wait(0.7)

        subtitle.shift(DOWN * 2.5)
        self.play(Write(subtitle))
        self.wait(0.5)

        self.play(FadeOut(title), FadeOut(subtitle))
        self.wait(0.5)

        # Intro text
        intro_text = Text(
            "Ford-Fulkerson Algorithm\n\n"
            "- The Ford-Fulkerson algorithm finds the maximum flow\n"
            "from a source node to a sink node in a flow network.\n\n"
            "- It repeatedly searches for paths with available capacity\n"
            "and augments flow along them, until no more such paths exist.",
            font_size=28, color=WHITE
        ).move_to(ORIGIN)

        self.play(Write(intro_text), run_time=4)
        self.wait(4)
        self.play(FadeOut(intro_text))


        # Vertex positions
        positions = {
            "s": LEFT * 4,
            "A": UP * 2,
            "B": ORIGIN,
            "C": DOWN * 2,
            "t": RIGHT * 4
        }

        # Create vertices
        vertices = {}
        for name, pos in positions.items():
            circle = Circle(radius=0.3, color=WHITE).move_to(pos)
            label = Text(name, font_size=24).move_to(pos)
            vertices[name] = VGroup(circle, label)
            self.add(vertices[name])

        # Edges and capacities
        edges_info = {
            ("s", "A"): 5,
            ("s", "B"): 7,
            ("s", "C"): 3,
            ("A", "B"): 2,
            ("A", "t"): 6,
            ("B", "t"): 5,
            ("B", "C"): 4,
            ("C", "t"): 8
        }

        edges = {}
        flow_labels = {}
        flows = {}

        for (u, v), cap in edges_info.items():
            arrow = Arrow(start=positions[u], end=positions[v], buff=0.35, stroke_width=4, color=WHITE)
            edges[(u, v)] = arrow
            flows[(u, v)] = 0
            midpoint = (positions[u] + positions[v]) / 2
            direction = positions[v] - positions[u]
            shift = rotate_vector(direction, -PI / 2)
            shift = shift / np.linalg.norm(shift) * 0.3
            flow_label = MathTex(f"0/{cap}", font_size=28).move_to(midpoint + shift)
            flow_labels[(u, v)] = flow_label
            self.add(flow_label)

        self.play(
            *[FadeIn(v) for v in vertices.values()],
            *[GrowArrow(arrow) for arrow in edges.values()],
            *[Write(label) for label in flow_labels.values()]
        )
        self.wait(1.5)

        steps = [
            {"path": [("s", "B"), ("B", "C"), ("C", "t")], "bottleneck": 4,
             "desc": "We send 4 units along s → B → C → t.\nBottleneck is B → C with capacity 4."},

            {"path": [("s", "A"), ("A", "t")], "bottleneck": 5,
             "desc": "We send 5 units along s → A → t.\nBottleneck is s → A with capacity 5."},

            {"path": [("s", "B"), ("B", "t")], "bottleneck": 3,
             "desc": "We send 3 units along s → B → t.\nRemaining capacity on s → B is 3."},

            {"path": [("s", "C"), ("C", "t")], "bottleneck": 3,
             "desc": "We send final 3 units along s → C → t.\nThis saturates both s → C and C → t."}
        ]

        total_flow = 0
        for i, step in enumerate(steps):
            step_num = i + 1
            path = step["path"]
            bottleneck = step["bottleneck"]
            desc = step["desc"]
            total_flow += bottleneck

            highlight = [edges[edge].copy().set_color(GREEN).set_stroke(width=6) for edge in path]

            # Step heading and explanation (shifted slightly up)
            step_text = Text(f"Step {step_num}: Augmenting path\nFlow = {bottleneck}", font_size=30).to_corner(UL)
            step_text.shift(UP * 0.2)  # Slight upward shift
            desc_text = Text(desc, font_size=24, color=WHITE).next_to(step_text, DOWN, buff=0.35).align_to(step_text, LEFT)
            desc_text.shift(UP * 0.2)  # Slight upward shift

            self.play(*[Transform(edges[edge], highlight[j]) for j, edge in enumerate(path)])
            self.play(FadeIn(step_text), FadeIn(desc_text))
            self.wait(3)

            for edge in path:
                prev_flow = flows[edge]
                cap = edges_info[edge]
                new_flow = prev_flow + bottleneck
                flows[edge] = new_flow

                new_tex = MathTex(f"{new_flow}/{cap}", font_size=28)
                new_tex.move_to(flow_labels[edge].get_center())
                self.play(Transform(flow_labels[edge], new_tex))

            self.play(
                *[edges[edge].animate.set_color(WHITE).set_stroke(width=4) for edge in path],
                FadeOut(step_text), FadeOut(desc_text)
            )

        result_text = Text(f"Max Flow = {total_flow}", font_size=32).to_edge(DOWN)
        self.play(Write(result_text))
        self.wait(2)
