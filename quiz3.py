from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Rectangle

class MentalHealthApp(App):
    def build(self):
        self.manager = ScreenManager()
        self.responses = {}  # Store the responses for analysis
        self.count = 0  # Initialize the count variable

        for i in range(1, 16):
            screen = QuestionScreen(name=f"Question{i}", question_number=i, app=self)
            self.manager.add_widget(screen)

        result_screen = ResultScreen(name="Result", app=self)
        self.manager.add_widget(result_screen)

        return self.manager

class QuestionScreen(Screen):
    def __init__(self, question_number, app, **kwargs):
        super(QuestionScreen, self).__init__(**kwargs)
        self.app = app
        self.question_number = question_number

        question_label = Label(text=f"{question_number}. {questions[question_number]}", halign='center', size_hint=(1, 1),
                               color=(0.071, 0.282, 0.420, 1))  # Color: #12486B
        self.add_widget(question_label)

        self.count_label = Label(text=f"Count: {self.app.count}", halign='center', size_hint=(1, 0.1),
                                 color=(0.071, 0.282, 0.420, 1))  # Color: #12486B

        # Set the background color for the QuestionScreen
        with self.canvas.before:
            Color(0.471, 0.839, 0.776, 1)  # Color: #78D6C6
            self.rect = Rectangle(size=(800,800), pos=self.pos)

        self.add_widget(self.count_label)

        self.response_buttons = []
        button_layout = BoxLayout(orientation='horizontal', size_hint=(1.0, 0.2), padding=(40, 40),
                                  spacing=10)
        for i in range(1, 11):
            button = Button(text=str(i), size_hint=(1, 1), background_color=(0.419, 0.153, 0.592, 1))  # Color: #419197
            button.bind(on_press=self.collect_response)
            self.response_buttons.append(button)
            button_layout.add_widget(button)
        self.add_widget(button_layout)

        next_button = Button(text="Next", size_hint=(0.3, 0.1), background_color=(0.964, 0.988, 0.804, 1))  # Color: #F5FCCD
        next_button.bind(on_press=self.show_next_question)
        self.add_widget(next_button)

    def collect_response(self, instance):
        response = int(instance.text)
        self.app.count += response  # Add the button value to the cumulative count
        self.count_label.text = f"Count: {self.app.count}"  # Update the count label
        self.app.responses[self.question_number] = self.app.count  # Store the updated cumulative count

    def show_next_question(self, instance):
        if self.question_number == 15:
            result_screen = self.manager.get_screen("Result")
            result = calculate_points(self.app.responses)
            result_screen.update_result(result)
            self.manager.current = "Result"
        else:
            next_question_number = self.question_number + 1
            next_question = self.manager.get_screen(f"Question{next_question_number}")
            self.manager.current = f"Question{next_question_number}"

class ResultScreen(Screen):
    def __init__(self, app, **kwargs):
        super(ResultScreen, self).__init__(**kwargs)
        self.app = app

        self.result_label = Label(text="", halign='center', color=(0.071, 0.282, 0.420, 1))  # Color: #12486B
        self.add_widget(self.result_label)

    def update_result(self, result):
        self.result_label.text = result

questions = {
    1: "Have you experienced any significant changes in your sleep patterns?",
    2: "Are you finding it challenging to concentrate or make decisions?",
    3: "Have you lost interest in activities you used to enjoy?",
    4: "Are you feeling unusually fatigued or lacking in energy?",
    5: "Have you noticed changes in your appetite or weight recently?",
    6: "Have you had any thoughts of self-harm or suicide?",
    7: "Do you experience physical symptoms like headaches or stomachaches that don't have a clear medical cause?",
    8: "Are you avoiding social interactions or withdrawing from friends and family?",
    9: "Have you experienced any traumatic events or significant life changes recently?",
    10: "Are you using substances as a way to cope with your feelings?",
    11: "How would you describe your support system? Do you have people you can confide in?",
    12: "Have you noticed any recurring negative thoughts or beliefs about yourself?",
    13: "Do you engage in self-care activities like exercise, meditation, or relaxation techniques?",
    14: "Are there specific triggers or situations that seem to worsen your mental health symptoms?",
    15: "How would you rate your overall quality of life right now on a scale from 1 to 10?"
}

def calculate_points(answers):
    points = answers[15]  # Use the cumulative count value as the points
    if points >= 100:
        return "Please seek immediate help. Your responses indicate severe concerns."
    elif points >= 30:
        return "Your score suggests a moderate level of concern. Consider discussing your feelings with someone."
    else:
        return "Your score indicates that you are doing well. Keep up the good work in maintaining your mental health."

if __name__ == '__main__':
    MentalHealthApp().run()
