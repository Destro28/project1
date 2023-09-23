from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk

# Initialize a dictionary to store mood data
mood_data = {}

# Define a list of days of the week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Initialize variables to track the maximum mood
max_mood = None
max_day = None

# Function to update mood data for the current day
def update_mood():
    day = days_of_week[len(mood_data)]  # Get the day based on the number of mood entries
    mood = mood_var.get()

    if mood in [1, 2, 3]:
        mood_data[day] = mood
        mood_var.set(0)  # Clear the mood input field
        update_image(mood)
        check_max_mood()

# Function to update the mood image
def update_image(mood):
    mood_images = {
        1: "unknown.png",
        2: "unknown.png",
        3: "unknown.png"
    }

    mood_image_path = mood_images.get(mood, "unknown.png")
    mood_image = Image.open(mood_image_path)
    #mood_image = mood_image.resize((100, 100), Image.ANTIALIAS)
    mood_photo = ImageTk.PhotoImage(mood_image)
    mood_label.config(image=mood_photo)
    mood_label.image = mood_photo

# Function to check and display the maximum mood
def check_max_mood():
    global max_mood, max_day
    if not mood_data:
        return
    max_mood = max(mood_data.values())
    max_day = [day for day, mood in mood_data.items() if mood == max_mood][0]
    max_mood_label.config(text=f"Max Mood: {max_mood} ({max_day})")

# Create the main window
root = tk.Tk()
root.title('Mood Tracker')

# Create GUI elements
mood_label = tk.Label(root, text='Select Mood:')
mood_var = tk.IntVar()
mood_combobox = ttk.Combobox(root, textvariable=mood_var, values=[1, 2, 3])
update_button = tk.Button(root, text='Update Mood', command=update_mood)

mood_image = Image.open("unknown.png")  # Default image
#mood_image = mood_image.resize((100, 100), Image.ANTIALIAS)
mood_photo = ImageTk.PhotoImage(mood_image)
mood_label = tk.Label(root, image=mood_photo)
mood_label.image = mood_photo

max_mood_label = tk.Label(root, text="Max Mood: N/A")

# Grid layout
mood_label.grid(row=0, column=0, padx=10, pady=10)
mood_combobox.grid(row=0, column=1, padx=10, pady=10)
update_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
mood_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
max_mood_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI main loop
root.mainloop()
