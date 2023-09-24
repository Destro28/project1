from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.graphics import Color, Rectangle

class SymptomMonitorApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.symptoms_screen = SymptomsScreen(name='symptoms')
        self.sm.add_widget(self.symptoms_screen)
        return self.sm

class SymptomsScreen(Screen):
    def __init__(self, **kwargs):
        super(SymptomsScreen, self).__init__(**kwargs)

        self.symptoms = {
            "feeling good or hyper": False,
            "irritability and shouting": False,
            "increased self-confidence": False,
            "reduced need for sleep": False,
            "increased talkativeness": False,
            "racing thoughts": False,
            "easily distracted": False,
            "increased energy": False,
            "increased activity": False,
            "increased social behavior": False,
            "increased interest in sex": False,
            "engaging in unusual or risky behaviors": False,
            "spending money recklessly": False,
        }

        self.questions = [
            "Have you experienced feeling good or hyper in the past? (Yes/No):",
            "Have you experienced irritability and shouting in the past? (Yes/No):",
            "Have you experienced increased self-confidence in the past? (Yes/No):",
            "Have you experienced reduced need for sleep in the past? (Yes/No):",
            "Have you experienced increased talkativeness in the past? (Yes/No):",
            "Have you experienced racing thoughts in the past? (Yes/No):",
            "Have you experienced being easily distracted in the past? (Yes/No):",
            "Have you experienced increased energy in the past? (Yes/No):",
            "Have you experienced increased activity in the past? (Yes/No):",
            "Have you experienced increased social behavior in the past? (Yes/No):",
            "Have you experienced increased interest in sex in the past? (Yes/No):",
            "Have you engaged in unusual or risky behaviors in the past? (Yes/No):",
            "Have you spent money recklessly in the past? (Yes/No):"
        ]

        self.question_index = 0

        self.layout = GridLayout(cols=1)
        self.add_widget(self.layout)

        self.layout.canvas.before.add(Color(0.75, 0.87, 1, 1))  # Light blue background color
        self.layout.canvas.before.add(Rectangle(size=(800,800), pos=self.layout.pos))

        self.label = Label(text=self.questions[self.question_index], color=(0, 0, 0, 1))  # Black text
        self.layout.add_widget(self.label)

        self.yes_button = Button(text="Yes", background_color=(0, 0, 1, 1), color=(1, 1, 1, 1))  # Bright blue button, white text
        self.no_button = Button(text="No", background_color=(0, 0, 1, 1), color=(1, 1, 1, 1))  # Bright blue button, white text
        self.yes_button.bind(on_press=self.process_response)
        self.no_button.bind(on_press=self.process_response)

        self.button_layout = GridLayout(cols=2)
        self.button_layout.add_widget(self.yes_button)
        self.button_layout.add_widget(self.no_button)
        self.layout.add_widget(self.button_layout)

    def process_response(self, instance):
        response = instance.text.lower()
        question = self.questions[self.question_index]
        symptom_key = question.split(" ")[-5]  # Extract the symptom key
        self.symptoms[symptom_key] = response == "yes"
        self.question_index += 1

        if self.question_index < len(self.questions):
            # Move to the next question
            self.label.text = self.questions[self.question_index]
        else:
            # All questions have been answered, show the conclusion
            self.show_conclusion()

    def show_conclusion(self):
        conclusion = "No cause for concern"  # Default conclusion
        if any(self.symptoms.values()):
            # Customize the conclusion based on symptoms
            # Modify these criteria and conclusions as needed
            if self.symptoms["feeling good or hyper"] and self.symptoms["increased activity"]:
                conclusion = "Seek medical attention immediately"
            elif self.symptoms["increased talkativeness"] or self.symptoms["racing thoughts"]:
                conclusion = "Consult a healthcare professional"
            else:
                conclusion = "Monitor your symptoms"

        # Display the conclusion
        self.layout.clear_widgets()
        conclusion_label = Label(text="Assessment Result:")
        self.layout.add_widget(conclusion_label)
        outcome_label = Label(text=conclusion)
        self.layout.add_widget(outcome_label)

if __name__ == '__main__':
    SymptomMonitorApp().run()
