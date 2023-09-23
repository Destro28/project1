import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.scrollview import ScrollView

kivy.require("1.11.1")

class MentalHealthQuestionsApp(App):
    def build(self):
        self.title = "Mental Health and Nutrition Questions"
        self.questions = [
            "Do you often find yourself craving specific foods when you are stressed or anxious?",
            "Do you experience changes in your appetite (either increased or decreased) when you are feeling down or depressed?",
            "Do you feel guilty or ashamed about your eating habits or food choices?",
            "Do you skip meals frequently due to a lack of interest in food or eating?",
            "Do you often turn to comfort foods when you are in a low mood or experiencing emotional distress?",
            "Do you have a regular and balanced eating schedule, with meals and snacks spaced throughout the day?",
            "Do you feel that your mental health and mood are positively influenced by maintaining a healthy and balanced diet?",
            "Do you use food as a way to cope with stress, boredom, or other emotional challenges?",
            "Do you pay attention to your body's hunger and fullness cues when deciding when and what to eat?",
            "Do you seek professional help or support when you notice that your mental health and appetite are negatively impacting each other?"
        ]

        self.answers = [None] * len(self.questions)
        self.current_question_index = 0  # Track the current question index

        self.layout = BoxLayout(orientation="vertical")

        self.scroll_view = ScrollView()
        self.questions_layout = BoxLayout(orientation="vertical", spacing=10, padding=10)

        # Increase the font_size for the question label
        self.question_label = Label(text=self.questions[0], font_size=20)  # Increased font size to 20
        self.questions_layout.add_widget(self.question_label)

        options_layout = BoxLayout(spacing=10)
        yes_button = ToggleButton(text="Yes", group="question_options")
        no_button = ToggleButton(text="No", group="question_options")
        neutral_button = ToggleButton(text="Neutral", group="question_options")

        yes_button.bind(on_release=lambda instance: self.on_option_selected("Yes"))
        no_button.bind(on_release=lambda instance: self.on_option_selected("No"))
        neutral_button.bind(on_release=lambda instance: self.on_option_selected("Neutral"))

        options_layout.add_widget(yes_button)
        options_layout.add_widget(no_button)
        options_layout.add_widget(neutral_button)
        self.questions_layout.add_widget(options_layout)

        self.submit_button = Button(text="Next", size_hint_y=None, height=50)
        self.submit_button.bind(on_release=self.next_question)

        self.scroll_view.add_widget(self.questions_layout)
        self.layout.add_widget(self.scroll_view)
        self.layout.add_widget(self.submit_button)

        return self.layout

    def on_option_selected(self, option):
        self.answers[self.current_question_index] = option

    def next_question(self, instance):
        # Update the current question index
        self.current_question_index += 1

        if self.current_question_index < len(self.questions):
            # Display the next question and reset options
            self.question_label.text = self.questions[self.current_question_index]
            for button in ToggleButton.get_widgets("question_options"):
                button.state = "normal"  # Reset option buttons
        else:
            # If all questions are answered, calculate and display results
            self.calculate_and_display_results()

    def calculate_and_display_results(self):
        # Determine the scenario based on user responses
        scenario = self.determine_scenario(self.answers)

        # Create a label for displaying the scenario
        result_label = Label(
            text=scenario,
            font_size=16,  # Adjust the font size for result display as needed
            size_hint=(1, None),
            height=200,  # Adjust the height as needed
        )
        self.questions_layout.add_widget(result_label)
        self.submit_button.disabled = True  # Disable the "Next" button

    def determine_scenario(self, responses):
        # Implement logic to determine the scenario based on user responses
        # Placeholder scenarios based on your descriptions
        if responses[5] == "Yes" and responses[8] == "Yes":
            return "Scenario 1 - Positive Mental Health and Nutrition"

        if responses[0] == "Yes" or responses[2] == "Yes" or responses[4] == "Yes" or responses[7] == "Yes":
            return "Scenario 2 - Emotional Eating Challenges"

        if responses[2] == "No" and responses[3] == "No" and responses[4] == "No" and responses[6] == "No" and responses[7] == "No" and responses[9] == "No":
            return "Scenario 3 - Stable Appetite and Positive Mental Health Awareness"

        # For simplicity, return a placeholder scenario if none of the above conditions are met
        return "Scenario 4 - Complex and Variable Relationship"

if __name__ == "__main__":
    MentalHealthQuestionsApp().run()