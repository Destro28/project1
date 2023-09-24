from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Rectangle, Color  # Import Rectangle and Color

class GAD7App(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical', spacing=10, padding=10)
        self.root.canvas.before.clear()
        self.root.canvas.before.add(Color(0.471, 0.839, 0.776, 1))  # Color: #78D6C6
        self.root.canvas.before.add(Rectangle(pos=self.root.pos, size=self.root.size))  # Set the background size
        self.current_question = 0
        self.questions = [
            "Feeling nervous, anxious or on edge",
            "Not being able to stop or control worrying",
            "Worrying too much about different things",
            "Trouble relaxing",
            "Being so restless that it is hard to sit still",
            "Becoming easily annoyed or irritable",
            "Feeling afraid as if something awful might happen"
        ]
        self.responses = [None] * len(self.questions)  # To store the responses
        self.create_question_label()
        self.create_response_buttons()

        return self.root

    def create_question_label(self):
        question_label = Label(text=self.questions[self.current_question], color=[0.071, 0.282, 0.420, 1])  # Color: #12486B
        self.root.add_widget(question_label)

    def create_response_buttons(self):
        button_layout = BoxLayout(orientation='horizontal', spacing=10)
        response_options = ["Not at all", "Several days", "More than half the days", "Nearly every day"]

        for option in response_options:
            response_button = Button(text=option, background_normal='', background_color=[0.419, 0.153, 0.592, 1])  # Color: #419197
            response_button.bind(on_press=lambda instance, text=option: self.save_response(text))
            button_layout.add_widget(response_button)

        self.root.add_widget(button_layout)

    def save_response(self, response):
        self.responses[self.current_question] = response
        self.current_question += 1

        if self.current_question < len(self.questions):
            self.root.clear_widgets()
            self.root.canvas.before.clear()
            self.root.canvas.before.add(Color(0.471, 0.839, 0.776, 1))  # Color: #78D6C6
            self.root.canvas.before.add(Rectangle(pos=self.root.pos, size=self.root.size))  # Set the background size
            self.create_question_label()
            self.create_response_buttons()
        else:
            self.calculate_score()

    def calculate_score(self):
        total_score = sum(self.get_score(response) for response in self.responses)
        interpretation = self.interpret_score(total_score)
        self.root.clear_widgets()
        self.root.canvas.before.clear()
        self.root.canvas.before.add(Color(0.471, 0.839, 0.776, 1))  # Color: #78D6C6
        self.root.canvas.before.add(Rectangle(pos=self.root.pos, size=self.root.size))  # Set the background size
        self.root.add_widget(Label(text=f"Total GAD-7 Score: {total_score}", color=[0.071, 0.282, 0.420, 1]))  # Color: #12486B
        self.root.add_widget(Label(text=f"Interpretation: {interpretation}", color=[0.071, 0.282, 0.420, 1]))  # Color: #12486B

    def get_score(self, response):
        if response == "Not at all":
            return 0
        elif response == "Several days":
            return 1
        elif response == "More than half the days":
            return 2
        elif response == "Nearly every day":
            return 3
        else:
            return -1

    def interpret_score(self, total_score):
        if total_score >= 0 and total_score <= 4:
            return "Minimal Anxiety"
        elif total_score >= 5 and total_score <= 9:
            return "Mild Anxiety"
        elif total_score >= 10 and total_score <= 14:
            return "Moderate Anxiety"
        elif total_score >= 15 and total_score <= 21:
            return "Severe Anxiety"

if __name__ == "__main__":
    GAD7App().run()
