from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.carousel import Carousel
from kivy.properties import StringProperty
from collections import Counter
import matplotlib.pyplot as plt

class MoodTrackerApp(App):
    def build(self):
        self.title = 'Mood Tracker'
        self.current_day_index = 0
        self.mood_data = {}
        self.days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.selected_mood = None

        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.day_label = Label(text=f"Select Mood for {self.days_of_week[self.current_day_index]}:", font_size=20)
        self.layout.add_widget(self.day_label)

        # Create a BoxLayout for mood buttons, centered horizontally
        mood_buttons_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=100)
        self.button_mood_1 = Button(text="1", on_press=lambda x: self.update_mood("1"), font_size=20)
        self.button_mood_2 = Button(text="2", on_press=lambda x: self.update_mood("2"), font_size=20)
        self.button_mood_3 = Button(text="3", on_press=lambda x: self.update_mood("3"), font_size=20)
        mood_buttons_layout.add_widget(self.button_mood_1)
        mood_buttons_layout.add_widget(self.button_mood_2)
        mood_buttons_layout.add_widget(self.button_mood_3)
        self.layout.add_widget(mood_buttons_layout)

        self.image_carousel = Carousel(direction='right', loop=True)
        self.default_image = Image(source='unknown.png', allow_stretch=True)
        self.image_carousel.add_widget(self.default_image)
        self.layout.add_widget(self.image_carousel)

        self.most_prominent_mood_label = Label(text="Most Prominent Mood of the Week: N/A", font_size=16)
        self.layout.add_widget(self.most_prominent_mood_label)

        self.line_graph_button = Button(text="Show Line Graph", on_press=self.show_line_graph, font_size=16)
        self.layout.add_widget(self.line_graph_button)

        self.mood_message_label = Label(text="", font_size=16)
        self.layout.add_widget(self.mood_message_label)

        self.popup = None

        return self.layout

    def update_mood(self, mood):
        self.selected_mood = mood
        if self.selected_mood:
            self.mood_data[self.days_of_week[self.current_day_index]] = self.selected_mood
            self.update_most_prominent_mood()
            self.update_mood_message()
            self.next_day()

    def next_day(self):
        self.current_day_index = (self.current_day_index + 1) % len(self.days_of_week)
        self.day_label.text = f"Select Mood for {self.days_of_week[self.current_day_index]}:"

    def update_most_prominent_mood(self):
        if self.mood_data:
            mood_counter = Counter(self.mood_data.values())
            most_common_mood = mood_counter.most_common(1)[0][0]
            self.most_prominent_mood_label.text = f"Most Prominent Mood of the Week: {most_common_mood}"

    def update_mood_message(self):
        if self.selected_mood:
            mood_message = self.get_mood_message(self.selected_mood)
            self.mood_message_label.text = mood_message

    @staticmethod
    def get_mood_message(mood):
        mood_messages = {
            '1': "1=A great week!",
            '2': "2=Could have been better.",
            '3': "3=It will get better."
        }
        return mood_messages.get(mood, "N/A")

    def show_line_graph(self, instance):
        if self.mood_data:
            moods = list(self.mood_data.keys())
            mood_values = [int(value) for value in self.mood_data.values()]

            plt.plot(moods, mood_values, marker='o', linestyle='-')
            plt.xlabel("Days of the Week", fontsize=16)
            plt.ylabel("Mood", fontsize=16)
            plt.title("Mood Progression for the Week", fontsize=20)
            plt.xticks(rotation=45)
            plt.grid(True)
            plt.show()

if __name__ == '__main__':
    MoodTrackerApp().run()
