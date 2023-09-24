from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

class SymmetricPatternsApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical', spacing=10)

        # Set the background color for the main layout
        with main_layout.canvas.before:
            Color(0.3, 0.3, 0.3, 1)  # Background color (gray)
            Rectangle(pos=main_layout.pos, size=main_layout.size)

        button_layout = GridLayout(cols=6, padding=10, spacing=10)
        disorders = {
            "Depression": {
                "description": "Depression is a mood disorder that causes a persistent feeling of sadness and loss of interest.",
                "points": [
                    "Depression affects people of all ages and backgrounds.",
                    "It can be triggered by various factors, including genetics, life events, and chemical imbalances in the brain.",
                    "Common symptoms of depression include feelings of hopelessness, fatigue, changes in appetite, and difficulty concentrating.",
                    "Depression can coexist with other mental health conditions, such as anxiety.",
                    "It is important to seek professional help for an accurate diagnosis and appropriate treatment.",
                ],
                "solutions": [
                    "Seek therapy with a licensed mental health professional.",
                    "Consider medication prescribed by a psychiatrist.",
                    "Engage in regular exercise, as it can boost mood and reduce symptoms.",
                    "Create a support system by reaching out to friends and family.",
                ]
            },
            "Anxiety": {
                "description": "Anxiety disorders are characterized by excessive and persistent worrying, fear, and uneasiness.",
                "points": [
                    "Anxiety disorders are among the most common mental health conditions worldwide.",
                    "They can manifest in different forms, such as generalized anxiety disorder (GAD), panic disorder, and social anxiety disorder.",
                    "Symptoms of anxiety may include restlessness, irritability, racing thoughts, physical tension, and avoidance of certain situations.",
                    "Anxiety can significantly impact daily functioning and quality of life.",
                ],
                "solutions": [
                    "Try cognitive-behavioral therapy to identify and manage anxious thoughts.",
                    "Consider medication options, such as selective serotonin reuptake inhibitors (SSRIs).",
                    "Practice deep breathing exercises and mindfulness techniques.",
                    "Engage in regular physical activity to reduce anxiety symptoms.",
                ]
            },
            "Bipolar Disorder": {
                "description": "Bipolar disorder is a mental health condition that causes extreme mood swings, including periods of mania and depression.",
                "points": [
                    "Bipolar disorder affects individuals of all ages and can have a significant impact on their daily lives.",
                    "It is characterized by two distinct mood episodes: mania and depression.",
                    "During manic episodes, individuals may experience increased energy, euphoria, impulsivity, and decreased need for sleep.",
                    "Depressive episodes are characterized by feelings of sadness, hopelessness, low energy, and loss of interest.",
                ],
                "solutions": [
                    "Consult with a psychiatrist to develop an appropriate medication plan.",
                    "Engage in therapy, such as cognitive-behavioral therapy (CBT) or interpersonal and social rhythm therapy (IPSRT).",
                    "Create a daily routine to help maintain stability and manage mood swings.",
                    "Implement stress reduction techniques, such as mindfulness and relaxation exercises.",
                ]
            },
            "Schizophrenia": {
                "description": "Schizophrenia is a chronic and severe mental disorder characterized by distorted thoughts, hallucinations, and delusions.",
                "points": [
                    "Schizophrenia affects how a person thinks, feels, and behaves.",
                    "It typically emerges in late adolescence or early adulthood and can be a lifelong condition.",
                    "Common symptoms include hallucinations, delusions, disorganized speech, and reduced emotional expression.",
                    "Schizophrenia can cause significant impairment in daily functioning and interpersonal relationships.",
                ],
                "solutions": [
                    "Work closely with a psychiatrist to find the most effective antipsychotic medication and dosage.",
                    "Engage in therapy, such as cognitive-behavioral therapy for psychosis (CBTp) or family therapy.",
                    "Create a supportive and structured environment to minimize stress and triggers.",
                    "Develop coping strategies to manage hallucinations or delusions, such as reality testing techniques.",
                ]
            },
            "(OCD)": {
                "description": "Obsessive-Compulsive Disorder (OCD) is a mental health condition characterized by recurring thoughts (obsessions) and repetitive behaviors (compulsions).",
                "points": [
                    "OCD can manifest in various forms, such as checking, washing, hoarding, or intrusive thoughts.",
                    "It often causes distress and interferes with daily functioning and relationships.",
                    "Common obsessions include fears of contamination, doubt, and intrusive or unwanted thoughts.",
                    "Compulsions are repetitive behaviors or mental acts aimed at reducing anxiety or preventing perceived harm.",
                ],
                "solutions": [
                    "Engage in cognitive-behavioral therapy (CBT) or exposure and response prevention (ERP) therapy.",
                    "Consider medication options, such as selective serotonin reuptake inhibitors (SSRIs).",
                    "Practice mindfulness and acceptance-based techniques to manage intrusive thoughts and anxiety.",
                    "Gradually expose yourself to feared situations or triggers to reduce avoidance behaviors.",
                ]
            },
            # Add more disorders and their information here
        }

        # Set different colors for buttons
        button_colors = [(0.6, 0.4, 0.8, 1), (0, 0, 1, 1), (0, 0.6, 0.4, 1), (1, 1, 0, 1), (1, 0.5, 0, 1)]

        for i, disorder in enumerate(disorders):
            disorder_button = Button(
                text=disorder,
                size_hint=(None, None),
                background_color=button_colors[i % 5]  # Set button background color
            )
            disorder_button.bind(
                on_release=lambda button, name=disorder: self.show_disorder_info(name, disorders[name])
            )
            button_layout.add_widget(disorder_button)

        main_layout.add_widget(button_layout)

        self.description_label = Label(
            text='',
            size_hint=(1, None),
            height=300.3,
            markup=True,
            text_size=(400, None),
            color=(1, 1, 1, 1)  # Text color (white)
        )
        main_layout.add_widget(self.description_label)

        self.solution_label = Label(
            text='',
            size_hint=(1, None),
            height=300.2,
            markup=True,
            text_size=(400, None),
            color=(1, 1, 1, 1)  # Text color (white)
        )
        main_layout.add_widget(self.solution_label)

        return main_layout

    def show_disorder_info(self, disorder_name, disorder_info):
        # Format text with markup for font and color
        description_text = f"[font=Arial][color=#FFFF00]Description for {disorder_name}[/color][/font]:\n[font=Arial]{disorder_info['description']}[/font]"
        solutions_text = "\n".join([f"[font=Arial]{i + 1}. {solution}[/font]" for i, solution in enumerate(disorder_info['solutions'])])
        self.description_label.text = description_text
        self.solution_label.text = f"[color=#FFFF00]Solutions for {disorder_name}[/color]:\n{solutions_text}"

if __name__ == '__main__':
    SymmetricPatternsApp().run()
