import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
import threading
import cv2
import pygame
import sys

kivy.require('1.11.1')

# Initialize pygame for sound
pygame.mixer.init()

# Define the file paths to your video and sound files
video_paths = [
    r'C:\Users\TEST\PycharmProjects\minndbuddies\5 Minute Meditation Music - Beautiful Healing Relaxing Meditation Music Timer.mp4',
    r'C:\Users\TEST\PycharmProjects\minndbuddies\5 Minute Meditation Music - with Earth Resonance Frequency for Deeper Relaxation.mp4',
    r'C:\Users\TEST\PycharmProjects\minndbuddies\5 minute meditation music for positive energy,relax,meditation music for positive energy 5 minutes.mp4',
    r'C:\Users\TEST\PycharmProjects\minndbuddies\5 Minute Timer - Relaxing Music with Ocean Waves.mp4'
]

sound_paths = [
    r'C:\Users\TEST\PycharmProjects\minndbuddies\5 Minute Meditation Music - Beautiful Healing Relaxing Meditation Music Timer.mp3',
    r'C:\Users\TEST\PycharmProjects\minndbuddies\5 Minute Meditation Music - with Earth Resonance Frequency for Deeper Relaxation.mp3',
    r'C:\Users\TEST\PycharmProjects\minndbuddies\5 minute meditation music for positive energy,relax,meditation music for positive energy 5 minutes.mp3',
    r'C:\Users\TEST\PycharmProjects\minndbuddies\5 Minute Timer - Relaxing Music with Ocean Waves.mp3'
]

# Create a flag to track if video is playing
video_playing = False
video_stop_event = None  # Initialize to None

# Function to play sound
def play_sound(sound_file):
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

# Function to stop sound
def stop_sound():
    pygame.mixer.music.stop()

# Function to display video
def display_video(video_file):
    global video_playing, video_stop_event
    cap = cv2.VideoCapture(video_file)

    while cap.isopened() and not video_stop_event.is_set():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    video_playing = False

class ColorButton(ButtonBehavior, Label):
    pass

class SoundVideoApp(App):

    def build(self):
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        self.title = "Sound and Video Player"

        # Set the background color of the layout to light blue
        with self.layout.canvas.before:
            Color(0.678, 0.847, 0.902, 1)  # Light blue color
            self.rect = Rectangle(size=(800,800), pos=self.layout.pos)

        self.case_label = Label(text="Choose a meditation")
        self.layout.add_widget(self.case_label)

        philosophical_cases = {
            "Journey to Serenity: Guided Meditation": (0.2, 0.2, 0.8, 1),  # Blue
            "Harmony of Mind and Nature": (0.9, 0.2, 0.7, 1),  # Pink
            "Meditation on Inner Peace": (0.9, 0.9, 0.2, 1),  # Yellow
            "Deep Reflection: Ocean of Tranquility": (0.2, 0.8, 0.2, 1)   # Green
        }

        self.case_buttons = []

        for case_name, color in philosophical_cases.items():
            case_button = ColorButton(text=case_name, color=color)
            case_button.bind(on_press=self.play_selected_case)
            self.layout.add_widget(case_button)
            self.case_buttons.append(case_button)

        # Add a "Back" button to go back to the main screen
        back_button = Button(text="Back", size_hint=(None, None))
        back_button.bind(on_press=self.back_to_main_screen)
        self.layout.add_widget(back_button)

        # Add a "Quit" button to terminate the program
        quit_button = Button(text="Quit", size_hint=(None, None))
        quit_button.bind(on_press=self.quit_app)
        self.layout.add_widget(quit_button)

        return self.layout

    def back_to_main_screen(self, instance):
        global video_playing, video_stop_event
        if video_playing:
            video_stop_event.set()
            cv2.destroyAllWindows()
            stop_sound()
            video_playing = False

    def quit_app(self, instance):
        sys.exit()

    def play_selected_case(self, instance):
        global video_playing, video_stop_event
        if video_playing:
            return  # Don't start a new video if one is already playing

        case_map = {
            "Journey to Serenity: Guided Meditation": 0,
            "Harmony of Mind and Nature": 1,
            "Meditation on Inner Peace": 2,
            "Deep Reflection: Ocean of Tranquility": 3
        }
        selected_case = case_map.get(instance.text)

        if selected_case is not None:
            sound_path, video_path = sound_paths[selected_case], video_paths[selected_case]
            play_sound(sound_path)
            video_playing = True  # Set the flag to True before playing video
            video_stop_event = threading.Event()  # Create an event to stop the video thread
            video_thread = threading.Thread(target=display_video, args=(video_path,))
            video_thread.start()
        else:
            invalid_case_popup = Popup(title="Invalid Case", content=Label(text="Please select a valid meditation"), size=(300, 150))
            invalid_case_popup.open()

    def on_stop(self):
        global video_playing, video_stop_event
        if video_playing:
            video_stop_event.set()  # Set the stop event to stop the video
            cv2.destroyAllWindows()
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        sys.exit()

if __name__ == '__main__':
    SoundVideoApp().run()
