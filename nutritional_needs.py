import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.scrollview import ScrollView

kivy.require("1.11.1")

# Your analyze_financial_situation function
def analyze_financial_situation(answers):
    if len(answers) != 6:
        return "Invalid input"

    q1, q2, q3, q4, q5, q6 = answers

    if q1 == "Yes" and q3 == "Yes" and q5 == "Yes":
        return "Scenario 1: Overall Positive Financial Situation\nConclusion: You are satisfied with your current salary, believe it aligns with your qualifications, and feel financially secure. This is a positive financial scenario."

    if q1 == "No" and q3 == "No" and q5 == "No":
        return "Scenario 2: Overall Dissatisfaction with Financial Situation\nConclusion: You are dissatisfied with your current financial situation, including your salary, and feel it's not commensurate with your qualifications. Financial stress may be a concern."

    if q1 == "Yes" and q2 == "Yes" and q3 == "No" and q4 == "No" and q5 == "No" and q6 == "No":
        return "Scenario 3: Satisfied but Stressed\nConclusion: Your salary meets your financial needs, but financial stress has negatively affected your mental health. You're dissatisfied with your compensation and may have made personal sacrifices. Seeking financial advice could be helpful."

    if q1 == "Yes" and q3 == "Yes" and q6 == "Yes" and q2 == "No" and q4 == "No" and q5 == "No":
        return "Scenario 4: Proactive Financial Management\nConclusion: Your salary meets your financial needs, and you are satisfied with your compensation. Seeking financial counseling or advice indicates responsible financial management."

    if q1 == "Yes" and q2 == "No" and q3 == "No" and q4 == "No" and q5 == "No" and q6 == "No":
        return "Scenario 5: Meeting Needs but Unsatisfied\nConclusion: Your current salary meets your financial needs, but you're dissatisfied with your compensation and haven't sought financial advice. There's room for improvement in your financial satisfaction."

    if q1 == "No" and q2 == "Yes" and q3 == "Yes" and q4 == "Yes" and q5 == "Yes" and q6 == "Yes":
        return "Scenario 6: Seeking Help due to Financial Stress\nConclusion: Your current salary doesn't meet your financial needs, and financial stress has negatively impacted your mental health. You're actively seeking financial advice to address these challenges."

    return "Scenario 7: Neutrality in Financial Situation\nConclusion: Your financial situation seems to be neither exceptionally good nor bad. It's important to assess your specific concerns and consider seeking advice if needed."

class MentalHealthQuestionsApp(App):
    def build(self):
        self.title = "Mental Health Questions"
        self.questions = [
            "Have you experienced any significant changes in your sleep patterns, such as difficulty falling asleep or staying asleep?",
            "Are you finding it challenging to concentrate or make decisions?",
            "Have you lost interest in activities you used to enjoy?",
            "Are you feeling unusually fatigued or lacking in energy?",
            "Have you noticed changes in your appetite or weight recently?",
            "Have you had any thoughts of self-harm or suicide? (If the answer is yes, seek immediate help.)",
            "Do you experience physical symptoms like headaches or stomachaches that don't have a clear medical cause?",
            "Are you avoiding social interactions or withdrawing from friends and family?",
            "Have you experienced any traumatic events or significant life changes recently?",
            "Are you using substances (e.g., alcohol or drugs) as a way to cope with your feelings?",
            "How would you describe your support system? Do you have people you can confide in?",
            "Have you noticed any recurring negative thoughts or beliefs about yourself?",
            "Do you engage in self-care activities like exercise, meditation, or relaxation techniques?",
            "Are there specific triggers or situations that seem to worsen your mental health symptoms?",
            "How would you rate your overall quality of life right now on a scale from 1 to 10?"
        ]

        self.answers = [None] * len(self.questions)

        self.layout = BoxLayout(orientation="vertical")

        self.scroll_view = ScrollView()
        self.questions_layout = BoxLayout(orientation="vertical", spacing=10, padding=10)

        for i, question in enumerate(self.questions):
            question_label = Label(text=f"{i + 1}. {question}", font_size=16)
            self.questions_layout.add_widget(question_label)

            # Add a spacer (empty BoxLayout) for spacing
            spacer = BoxLayout()
            self.questions_layout.add_widget(spacer)

            options_layout = BoxLayout(spacing=10)
            yes_button = ToggleButton(text="Yes", group=f"q{i}")
            no_button = ToggleButton(text="No", group=f"q{i}")
            neutral_button = ToggleButton(text="Neutral", group=f"q{i}")

            yes_button.bind(on_release=lambda instance, i=i: self.on_option_selected(i, "Yes"))
            no_button.bind(on_release=lambda instance, i=i: self.on_option_selected(i, "No"))
            neutral_button.bind(on_release=lambda instance, i=i: self.on_option_selected(i, "Neutral"))

            options_layout.add_widget(yes_button)
            options_layout.add_widget(no_button)
            options_layout.add_widget(neutral_button)
            self.questions_layout.add_widget(options_layout)

        self.submit_button = Button(text="Submit", size_hint_y=None, height=50)
        self.submit_button.bind(on_release=self.calculate_and_display_results)

        self.scroll_view.add_widget(self.questions_layout)
        self.layout.add_widget(self.scroll_view)
        self.layout.add_widget(self.submit_button)

        return self.layout

    def on_option_selected(self, question_index, option):
        self.answers[question_index] = option

    def calculate_and_display_results(self, instance):
        # Call the analyze_financial_situation function with the financial questions
        financial_answers = self.answers[-6:]
        financial_results = analyze_financial_situation(financial_answers)

        # Create a label for displaying the financial results
        result_label = Label(
            text=financial_results,
            font_size=16,
            size_hint=(1, None),
            height=100,  # Adjust the height as needed
        )

        # Add a spacer (empty BoxLayout) for spacing
        spacer = BoxLayout()
        self.questions_layout.add_widget(spacer)

        # Display the financial results
        self.questions_layout.add_widget(result_label)

if __name__ == "__main__":
    MentalHealthQuestionsApp().run()