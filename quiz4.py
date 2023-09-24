from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle

class StressAssessmentApp(App):
    def __init__(self):
        super(StressAssessmentApp, self).__init__()
        self.responses = {
            "Never": 0,
            "Almost never": 1,
            "Sometimes": 2,
            "Fairly often": 3,
            "Very often": 4
        }
        self.total_stress_score = 0
        self.question_index = 0
        self.question_labels = [
            "been upset because of something that happened unexpectedly?",
            "felt that you were unable to control the important things in your life?",
            "felt nervous and stressed?",
            "felt confident about your ability to handle your personal problems?",
            "felt that things were going your way?",
            "found that you could not cope with all the things that you had to do?",
            "been able to control irritations in your life?",
            "felt on top of things?",
            "been angered because of things that happened that were outside of your control?",
            "felt difficulties were piling up so high that you could not overcome them?"
        ]

    def build(self):
        self.layout = ScrollView()
        self.grid = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.grid.bind(minimum_height=self.grid.setter('height'))

        with self.grid.canvas.before:
            Color(0.7, 0.9, 0.9, 1)  # Set background color to light blue
            self.rect = Rectangle(size=(800,800), pos=self.grid.pos)

        self.question_label = Label(
            text=f"In the last month, how often have you {self.question_labels[self.question_index]}?",
            size_hint_y=None,
            height=100,
            color=(0, 0, 0, 1)  # Text color
        )

        self.responses_buttons = BoxLayout(
            orientation='horizontal',
            spacing=10,
            size_hint_y=None,
            height=60
        )

        button_colors = [(1, 1, 0.8, 1),(0.78, 0.92, 0.80, 1),(0.38, 0.77, 0.87, 1),(0.18, 0.53, 0.73, 1),(0.07, 0.28, 0.42, 1)]

        for response in sorted(self.responses.keys(), key=lambda x: self.responses[x]):
            button = Button(
                text=response,
                on_press=self.select_response,
                background_normal='',
                background_color=button_colors[self.responses[response]]
            )
            self.responses_buttons.add_widget(button)

        self.grid.add_widget(self.question_label)
        self.grid.add_widget(self.responses_buttons)
        self.layout.add_widget(self.grid)

        return self.layout

    def select_response(self, instance):
        response = instance.text
        self.total_stress_score += self.responses[response]
        self.question_index += 1
        if self.question_index < len(self.question_labels):
            self.question_label.text = f"In the last month, how often have you {self.question_labels[self.question_index]}?"
        elif self.question_index == len(self.question_labels):
            self.calculate_stress_level()

    def calculate_stress_level(self):
        stress_level = ""
        if self.total_stress_score <= 9:
            stress_level = "Low stress"
        elif self.total_stress_score <= 18:
            stress_level = "Moderate stress"
        elif self.total_stress_score <= 27:
            stress_level = "High stress"
        else:
            stress_level = "Very high stress"

        result_label = Label(
            text=f"Stress Assessment Result\nTotal Stress Score: {self.total_stress_score}\nStress Level: {stress_level}",
            size_hint_y=None,
            height=150,
            color=(0, 0, 0, 1)  # Text color
        )
        self.grid.add_widget(result_label)

if __name__ == '__main__':
    StressAssessmentApp().run()
