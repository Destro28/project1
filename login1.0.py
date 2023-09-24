import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.image import Image
from kivy.uix.carousel import Carousel 
import moodtracker  # Import the MoodTrackerApp class from moodtracker.py
import os

class myboxlayout(BoxLayout):
    def __init__(self, **kwargs):
        super(myboxlayout, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # Set the background color to #78D6C6
        self.background_color = (0.47, 0.84, 0.78, 1.0)  # RGB + Alpha (opacity)

        # Name input
        name_layout = BoxLayout(orientation='horizontal')
        name_label = Label(text="Name: ", color=(0.9, 0.9, 0.8, 1.0))  # Cream color text
        self.name = TextInput(multiline=False, background_color=(0.9, 0.9, 0.8, 1.0))  # Cream color background
        name_layout.add_widget(name_label)
        name_layout.add_widget(self.name)
        self.add_widget(name_layout)

        # Email input
        email_layout = BoxLayout(orientation='horizontal')
        email_label = Label(text="Email: ", color=(0.9, 0.9, 0.8, 1.0))  # Cream color text
        self.email = TextInput(multiline=False, background_color=(0.9, 0.9, 0.8, 1.0))  # Cream color background
        email_layout.add_widget(email_label)
        email_layout.add_widget(self.email)
        self.add_widget(email_layout)

        # Mobile No input
        mobile_layout = BoxLayout(orientation='horizontal')
        mobile_label = Label(text="Mobile No: ", color=(0.9, 0.9, 0.8, 1.0))  # Cream color text
        self.mobile = TextInput(multiline=False, background_color=(0.9, 0.9, 0.8, 1.0))  # Cream color background
        mobile_layout.add_widget(mobile_label)
        mobile_layout.add_widget(self.mobile)
        self.add_widget(mobile_layout)

        # Submit button with light blue color
        self.submit = Button(text="Submit", font_size=50, background_color=(0.4, 0.7, 1.0, 1.0))  # Light blue color
        self.submit.bind(on_press=self.retrieve)
        self.add_widget(self.submit)

        # Label to display a message to the user
        self.message_label = Label(text="", halign="center")
        self.add_widget(self.message_label)

    def is_file_empty(self, file1):
        return os.path.getsize(file1) == 0

    def retrieve(self, temp):
        name = self.name.text
        email = self.email.text
        mobile = self.mobile.text
        file1 = "user_details.txt"
        with open(file1, 'a') as file:
            if self.is_file_empty(file1):
                file.write("Name\t\tEmail\t\tMobile\n")
            file.write(f"{name}\t\t{email}\t\t{mobile}\n")

        # Update the message label to inform the user
        self.message_label.text = "Data saved successfully!"

class MyApp(App):
    def build(self):
        return myboxlayout()

if __name__ == "__main__":
    MyApp().run()
