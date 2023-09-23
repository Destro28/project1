from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class MentalHealthAssessmentApp(App):
    def build(self):
        self.assessment_questions = [
            "Do you often feel overwhelmed or excessively stressed?",
            "Have you been experiencing persistent feelings of sadness or hopelessness?",
            "Do you have difficulty concentrating or making decisions?",
            "Have you noticed a significant change in your appetite or weight?",
            "Are you having trouble sleeping or experiencing changes in your sleep patterns?",
            "Do you often feel anxious or experience panic attacks?",
            "Have you lost interest or pleasure in activities you used to enjoy?",
            "Do you find it challenging to manage your emotions or control your anger?",
            "Have you been isolating yourself or withdrawing from social interactions?",
            "Do you have thoughts of self-harm or suicide?",
            "Do you often feel fatigued or lacking energy?",
            "Have you experienced physical symptoms such as headaches or stomachaches due to stress?",
            "Are you experiencing a loss of interest in your work or studies?",
            "Have you been using alcohol or drugs as a way to cope with your feelings?",
            "Are you experiencing a loss of motivation to engage in daily activities?",
            "Do you feel hopeless about the future?",
            "Have you been avoiding responsibilities or tasks that you used to handle?",
            "Do you frequently experience racing thoughts or restlessness?",
            "Have you been neglecting self-care and personal hygiene?",
            "Do you find it hard to relax and unwind?",
        ]

        self.score = 0
        self.current_question_index = 0

        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.question_label = Label(text=self.assessment_questions[self.current_question_index])
        self.layout.add_widget(self.question_label)

        self.yes_button = Button(text="Yes")
        self.yes_button.bind(on_press=self.answer_yes)
        self.layout.add_widget(self.yes_button)

        self.no_button = Button(text="No")
        self.no_button.bind(on_press=self.answer_no)
        self.layout.add_widget(self.no_button)

        return self.layout

    def answer_yes(self, instance):
        self.score += 1
        self.next_question()

    def answer_no(self, instance):
        self.next_question()

    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index < len(self.assessment_questions):
            self.question_label.text = self.assessment_questions[self.current_question_index]
        else:
            self.display_results()

    def display_results(self):
        result_popup = Popup(title="Assessment Results",
                             content=Label(text=self.get_assessment_result()),
                             size_hint=(None, None), size=(400, 200))
        result_popup.open()

    def get_assessment_result(self):
        if self.score <= 3:
            return "Based on your responses, your mental health appears to be in a good state."
        elif self.score <= 6:
            return "Based on your responses, you may be experiencing some mild mental health concerns. It's important to take care of yourself and seek support if needed."
        else:
            return "Based on your responses, it seems like you may be facing some significant mental health challenges. It's crucial to reach out for professional help and support."

if __name__ == '__main__':
    MentalHealthAssessmentApp().run()
