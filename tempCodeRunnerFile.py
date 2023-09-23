from tkinter import Tk, Label, Button, StringVar, font
from PIL import Image, ImageTk
from collections import Counter
import matplotlib.pyplot as plt

# Initialize a dictionary to store mood data
mood_data = {}

# Define a list of days of the week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Initialize selected_mood as a global variable
selected_mood = None

# Create a function to update mood data and display mood messages
def update_mood(mood):
    global selected_mood
    selected_mood = mood
    if selected_mood:
        mood_data[current_day] = selected_mood
        update_most_prominent_mood()
        update_mood_message()
        next_day()

# Create a function to switch to the next day
def next_day():
    global current_day
    if not current_day:
        current_day = days_of_week[0]
    else:
        current_day_index = days_of_week.index(current_day)
        if current_day_index < len(days_of_week) - 1:
            current_day = days_of_week[current_day_index + 1]
        else:
            current_day = None
            show_line_graph()

    day_label.config(text=f"Select Mood for {current_day}:")

# Create a function to update the most prominent mood of the week
def update_most_prominent_mood():
    if mood_data:
        mood_counter = Counter(mood_data.values())
        most_common_mood = mood_counter.most_common(1)[0][0]
        most_prominent_mood_label.config(text=f"Most Prominent Mood of the Week: {most_common_mood}", font=("Arial", 16))

# Create a function to get the mood message based on the selected mood
def get_mood_message(mood):
    mood_messages = {
        1: "1=A great week!",
        2: "2=Could have been better.",
        3: "3=It will get better."
    }
    return mood_messages.get(int(mood), "N/A")

# Create a function to update the mood message label
def update_mood_message():
    if selected_mood:
        mood_message = get_mood_message(selected_mood)
        mood_message_label.config(text=mood_message, font=("Arial", 16))

# Create a function to plot the mood line graph
def show_line_graph():
    if mood_data:
        moods = list(mood_data.keys())
        mood_values = [int(value) for value in mood_data.values()]

        plt.plot(moods, mood_values, marker='o', linestyle='-')
        plt.xlabel("Days of the Week", fontsize=16)
        plt.ylabel("Mood", fontsize=16)
        plt.title("Mood Progression for the Week", fontsize=20)
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.show()

# Create the main window
root = Tk()
root.title('Mood Tracker')

# Create GUI elements
current_day = days_of_week[0]

day_label = Label(root, text=f"Select Mood for {current_day}:", font=("Arial", 20))
mood_var = StringVar()

# Create larger buttons for mood options (1, 2, 3) with increased font size
button_font = font.Font(size=20)
button_mood_1 = Button(root, text="1", command=lambda: update_mood(1), width=5, font=button_font)
button_mood_2 = Button(root, text="2", command=lambda: update_mood(2), width=5, font=button_font)
button_mood_3 = Button(root, text="3", command=lambda: update_mood(3), width=5, font=button_font)

update_button = Button(root, text='Next Day', command=next_day, font=("Arial", 20))

# Load the default "unknown.png" image for mood selection
default_mood_image = Image.open("unknown.png")
default_mood_image = ImageTk.PhotoImage(default_mood_image)
mood_image_label = Label(root, image=default_mood_image)

# Create a label for the most prominent mood
most_prominent_mood_label = Label(root, text="Most Prominent Mood of the Week: N/A", font=("Arial", 16))

# Create a button to show the line graph
line_graph_button = Button(root, text="Show Line Graph", command=show_line_graph, font=("Arial", 16))

# Create a Label for mood messages
mood_message_label = Label(root, text="", font=("Arial", 16))

# Grid layout
day_label.grid(row=0, column=0, padx=10, pady=10, columnspan=3)
button_mood_1.grid(row=1, column=0, padx=10, pady=10)
button_mood_2.grid(row=1, column=1, padx=10, pady=10)
button_mood_3.grid(row=1, column=2, padx=10, pady=10)
update_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
mood_image_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10)
most_prominent_mood_label.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
line_graph_button.grid(row=5, column=0, columnspan=3, padx=10, pady=10)
mood_message_label.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
