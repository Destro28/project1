from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class EatingAssessmentApp(App):
    def build(self):
        self.responses = {
            "thoughts about weight or appearance": 0,
            "eating speed and feeling full": 0,
            "control over eating urges": 0,
            "eating when bored": 0,
            "eating when not physically hungry": 0,
            "guilt or self-hate after overeating": 0,
            "dieting and binge eating": 0,
            "feeling uncomfortably stuffed": 0,
            "caloric intake fluctuations": 0,
            "ability to stop eating": 0,
            "stopping when full": 0,
            "eating around others": 0,
            "meal frequency and snacking": 0,
            "preoccupation with eating urges": 0,
            "thoughts about food": 0,
            "knowing when physically hungry": 0,
        }
        self.current_question = None
        self.index = 0
        self.questions = list(self.responses.keys())

        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Select the statement that best describes how you feel:")
        self.layout.add_widget(self.label)

        self.add_question(self.questions[self.index])

        return self.layout

    def add_question(self, question):
        if self.current_question is not None:
            self.layout.remove_widget(self.current_question)

        self.current_question = BoxLayout(orientation='vertical')
        self.current_question.add_widget(Label(text=f"{question}"))
        response_options = ["Never", "Almost never", "Sometimes", "Fairly often", "Very often"]
        button_colors = [(1, 1, 0.8, 1), (0.78, 0.92, 0.80, 1), (0.38, 0.77, 0.87, 1), (0.18, 0.53, 0.73, 1), (0.07, 0.28, 0.42, 1)]

        for i, option in enumerate(response_options):
            btn = Button(text=option, background_color=button_colors[i])
            btn.bind(on_press=lambda instance, q=question, ans=i: self.process_response(q, ans))
            self.current_question.add_widget(btn)

        self.layout.add_widget(self.current_question)

    def process_response(self, question, answer):
        self.responses[question] = answer

        self.index += 1
        if self.index < len(self.questions):
            self.add_question(self.questions[self.index])
        else:
            self.display_result()

    def display_result(self):
        # Perform the calculation and display the result here
        total_score = sum(self.responses.values())
        concern_level = ""
        if total_score >= 48:
            concern_level = "Very High Concern - Seek Professional Help"
        elif total_score >= 36:
            concern_level = "High Concern - Consider Consulting a Healthcare Professional"
        elif total_score >= 24:
            concern_level = "Moderate Concern - Self-Monitor and Consider Seeking Support"
        else:
            concern_level = "Low Concern - Continue Healthy Eating Habits"

        self.layout.clear_widgets()
        result_label = Label(text="\nAssessment Result:")
        self.layout.add_widget(result_label)
        total_score_label = Label(text=f"Total Score: {total_score}")
        self.layout.add_widget(total_score_label)
        concern_level_label = Label(text=f"Level of Concern: {concern_level}")
        self.layout.add_widget(concern_level_label)

if __name__ == '__main__':
    EatingAssessmentApp().run()
