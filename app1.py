from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import turtle
import colorsys
import math

class SymmetricPatternsApp(App):
    def build(self):
        layout = GridLayout(cols=2, padding=10, spacing=10)

        # Create buttons for each pattern
        for pattern_num in range(1, 8):
            pattern_button = Button(text=f'Pattern {pattern_num}', size_hint=(None, None))
            pattern_button.bind(on_release=lambda button, num=pattern_num: self.generate_pattern(num))
            layout.add_widget(pattern_button)

        self.info_label = Label(text='', size_hint=(1, None))
        layout.add_widget(self.info_label)

        return layout

    def generate_pattern(self, pattern_num):
        def case_1():
            self.info_label.text = "Running Pattern 1"
            turtle.clear()
            turtle.speed(0)
            turtle.bgcolor('black')
            hue = 0.0
            turtle.hideturtle()
            turtle.pensize(5)
            for i in range(300):
                col = colorsys.hsv_to_rgb(hue, 1, 1)
                turtle.pencolor(col)
                hue += 0.005
                turtle.forward(i)
                turtle.right(20 * 2 + 1)
                turtle.circle(50)
            self.info_label.text = "Pattern 1 Done"

        def case_2():
            self.info_label.text = "Running Pattern 2"
            turtle.clear()
            t = turtle.Turtle()
            t.speed(150)
            turtle.bgcolor('black')
            for i in range(250):
                t.color('green')
                t.forward(i)
                t.left(5)
            self.info_label.text = "Pattern 2 Done"

        def case_3():
            self.info_label.text = "Running Pattern 3"
            turtle.clear()
            colors = ['red', 'purple', 'white', 'yellow', 'green', 'pink']
            turtle.bgcolor('black')
            for x in range(360):
                turtle.pencolor(colors[x % 6])
                turtle.width(x / 100 + 1)
                turtle.forward(x)
                turtle.left(59)
                turtle.speed(500)
            self.info_label.text = "Pattern 3 Done"

        def case_4():
            self.info_label.text = "Running Pattern 4"
            turtle.clear()
            f = turtle.Turtle()
            f.speed(14)
            f.color('blue')
            turtle.bgcolor('black')
            for i in range(100):
                f.circle(80)
                f.right(50)
            self.info_label.text = "Pattern 4 Done"

        def case_5():
            self.info_label.text = "Running Pattern 5"
            turtle.clear()
            t = turtle.Turtle()
            s = turtle.Screen()
            s.bgcolor("black")
            t.pencolor("cyan")
            a = 0
            b = 0
            t.speed(0)
            t.penup()
            t.goto(0, 200)
            t.pendown()
            while True:
                t.forward(a)
                t.right(b)
                a += 3
                b += 1
                if b == 210:
                    break
                t.hideturtle()
            self.info_label.text = "Pattern 5 Done"

        def case_6():
            self.info_label.text = "Running Pattern 6"
            turtle.clear()
            def hearta(k):
                return 15 * math.sin(k) ** 3

            def heartb(k):
                return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

            turtle.speed(0)
            turtle.bgcolor("black")
            for i in range(10000):
                turtle.goto(hearta(i) * 20, heartb(i) * 20)
                for j in range(5):
                    turtle.color("#f73487")
                    turtle.goto(0, 0)
            self.info_label.text = "Pattern 6 Done"

        def case_7():
            self.info_label.text = "Running Pattern 7"
            turtle.clear()
            hr = turtle.Turtle()
            hr.left(90)
            hr.speed(150)

            def tree(i):
                if (i >= 20):
                    hr.forward(i)
                    hr.left(30)
                    tree(3 * i / 4)
                    hr.right(30)
                    tree(3 * i / 4)
                    hr.right(30)
                    tree(3 * i / 4)
                    hr.left(30)
                    hr.backward(i)

            tree(100)
            self.info_label.text = "Pattern 7 Done"

        switch = {
            1: case_1,
            2: case_2,
            3: case_3,
            4: case_4,
            5: case_5,
            6: case_6,
            7: case_7
        }

        selected_case = switch.get(pattern_num)
        if selected_case:
            selected_case()
        else:
            self.info_label.text = "Invalid case selected."

if __name__ == '__main__':
    SymmetricPatternsApp().run()
