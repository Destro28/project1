from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window

class MentalHealthAssessmentApp(App):
    def build(self):
        self.assessment_questions = [
            "I often feel overwhelmed or excessively stressed.",
            "I have been experiencing persistent feelings of sadness or hopelessness.",
            "I have difficulty concentrating or making decisions.",
            "I have noticed a significant change in my appetite or weight.",
            "I have trouble sleeping or experience changes in my sleep patterns.",
            "I often feel anxious or experience panic attacks.",
            "I have lost interest or pleasure in activities I used to enjoy.",
            "I find it challenging to manage my emotions or control my anger.",
            "I have been isolating myself or withdrawing from social interactions.",
            "I have thoughts of self-harm or suicide.",
            "I often feel fatigued or lacking energy.",
            "I have experienced physical symptoms such as headaches or stomachaches due to stress.",
            "I am experiencing a loss of interest in my work or studies.",
            "I have been using alcohol or drugs as a way to cope with my feelings.",
            "I am experiencing a loss of motivation to engage in daily activities.",
            "I feel hopeless about the future.",
            "I have been avoiding responsibilities or tasks that I used to handle.",
            "I frequently experience racing thoughts or restlessness.",
            "I have been neglecting self-care and personal hygiene.",
            "I find it hard to relax and unwind."
        ]

        self.score = 0
        self.current_question_index = 0

        Window.clearcolor = (0.47, 0.84, 0.78, 1)

        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.question_label = Label(
            text=self.assessment_questions[self.current_question_index],
            color=(0.16, 0.22, 0.42, 1),
            size_hint=(1, 0.6)
        )
        self.layout.add_widget(self.question_label)

        self.case_buttons = [
            Button(text="Strongly Agree", background_color=(0, 0.7, 0, 1)),
            Button(text="Agree", background_color=(0, 0.7, 0, 1)),
            Button(text="Neutral", background_color=(0.7, 0.7, 0, 1)),
            Button(text="Disagree", background_color=(0.8, 0, 0, 1)),
            Button(text="Strongly Disagree", background_color=(0.8, 0, 0, 1))
        ]

        for button in self.case_buttons:
            button.bind(on_press=self.answer_question)
            self.layout.add_widget(button)

        return self.layout

    def answer_question(self, instance):
        case = instance.text
        if case == "Strongly Agree":
            self.score += 5
        elif case == "Agree":
            self.score += 4
        elif case == "Neutral":
            self.score += 3
        elif case == "Disagree":
            self.score += 2
        elif case == "Strongly Disagree":
            self.score += 1

        self.next_question()

    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index < len(self.assessment_questions):
            self.question_label.text = self.assessment_questions[self.current_question_index]
        else:
            self.display_results()

    def display_results(self):
        result_label = Label(
            text=self.get_assessment_result(),
            color=(1, 0.84, 0, 1),  # Bright Yellow
            font_size=18
        )
        result_popup = Popup(
            title="Assessment Results",
            content=result_label,
            size_hint=(None, None),
            size=(400, 200)
        )
        result_popup.open()

    def get_assessment_result(self):
        if self.score <= 30:
            return "Your mental health seems good."
        elif self.score <= 60:
            return "You may have mild mental health concerns. Seek support if needed."
        else:
            return "You may be facing significant mental health challenges. Reach out for professional help."

if __name__ == '__main__':
    MentalHealthAssessmentApp().run()
