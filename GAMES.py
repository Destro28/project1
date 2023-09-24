import tkinter as tk
import random


class BubbleWrapPopperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bubble Wrap Popper")
        self.root.geometry("400x400")
        self.score = 0

        self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 16))
        self.score_label.pack(pady=10)

        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack()

        self.create_buttons()

    def create_buttons(self):
        rows, cols = 4, 4  # You can change the dimensions as needed

        self.buttons = [[None for _ in range(cols)] for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                button = tk.Button(self.buttons_frame, text="O", font=("Arial", 16),
                                   command=lambda r=row, c=col: self.pop_bubble(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def pop_bubble(self, row, col):
        if self.buttons[row][col]["text"] == "O":
            self.score += 1
            self.score_label.config(text="Score: " + str(self.score))
            self.buttons[row][col]["text"] = "X"


def main():
    root = tk.Tk()
    app = BubbleWrapPopperApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
