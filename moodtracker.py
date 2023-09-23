from tkinter import Tk, Label, Button, StringVar, Toplevel
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
from collections import Counter
import matplotlib.pyplot as plt

# Initialize a dictionary to store mood data
mood_data = {}

# Define a list of days of the week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Create a function to update mood data
def update_mood():
    mood = mood_var.get()
    if mood:
        mood_data[current_day] = mood
        update_most_prominent_mood()
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
            show_summary()

    day_label.config(text=f"Select Mood for {current_day}:")
    mood_var.set("")

# Create a function to display the mood summary in a separate window
def show_summary():
    summary_window = Toplevel(root)
    summary_window.title("Mood Summary")

    # Create a Label for each day's mood
    for day, mood in mood_data.items():
        mood_label = Label(summary_window, text=f"{day}: {mood}")
        mood_label.pack()

    # Create a Label for the max mood of the week
    max_mood = max(mood_data.values(), key=lambda x: int(x))
    max_mood_label = Label(summary_window, text=f"Max Mood of the Week: {max_mood}")
    max_mood_label.pack()

    summary_window.mainloop()

# Create a function to update the most prominent mood of the week
def update_most_prominent_mood():
    if mood_data:
        mood_counter = Counter(mood_data.values())
        most_common_mood = mood_counter.most_common(1)[0][0]
        most_prominent_mood_label.config(text=f"Most Prominent Mood of the Week: {most_common_mood}")

# Create a function to get the mood message based on the most prominent mood
def get_mood_message(mood):
    mood_messages = {
        1: "1=A great week!",
        2: "2=Could have been better.",
        3: "3=It will get better."
    }
    return mood_messages.get(int(mood), "N/A")

# Create a function to plot the mood line graph in a separate window
def show_line_graph():
    if mood_data:
        line_graph_window = Toplevel(root)
        line_graph_window.title("Mood Line Graph")

        moods = list(mood_data.keys())
        mood_values = [int(value) for value in mood_data.values()]

        plt.plot(moods, mood_values, marker='o', linestyle='-')
        plt.xlabel("Days of the Week")
        plt.ylabel("Mood")
        plt.title("Mood Progression for the Week")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.show()

# Create the main window
root = Tk()
root.title('Mood Tracker')

# Create GUI elements
current_day = days_of_week[0]

day_label = Label(root, text=f"Select Mood for {current_day}:")
mood_var = StringVar()
mood_combobox = Combobox(root, textvariable=mood_var, values=["1 - Happy", "2 - Okay", "3 - Sad"])
update_button = Button(root, text='Update Mood', command=update_mood)

# Load the default "unknown.png" image for mood selection
default_mood_image = Image.open("unknown.png")
default_mood_image = ImageTk.PhotoImage(default_mood_image)
mood_image_label = Label(root, image=default_mood_image)

# Create a label for the most prominent mood
most_prominent_mood_label = Label(root, text="Most Prominent Mood of the Week: N/A")

# Create buttons to show summary and line graph
summary_button = Button(root, text="Show Summary", command=show_summary)
line_graph_button = Button(root, text="Show Line Graph", command=show_line_graph)

# Grid layout
day_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
mood_combobox.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
update_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
mood_image_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
most_prominent_mood_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
summary_button.grid(row=5, column=0, padx=10, pady=10)
line_graph_button.grid(row=5, column=1, padx=10, pady=10)

root.mainloop()
