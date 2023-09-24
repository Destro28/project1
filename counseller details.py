from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Rectangle

class CounselorApp(App):
    counselors = [
        ["Anusree Menon", "9673470495", "anusree2000@gmail.com", "Bangalore University",
         "Therapeutic work with young adults"],
        ["Chandani Chopra Kapoor", "9870586865", "chandani_kapoor@hotmail.com",
         "National Institute of Education(NIE), NCERT, New Delhi", "Counseling, career guidance, workshops and EQ"],
        ["Dhananjay Parkar", "9960504406", "parksoham@gmail.com",
         "Regional Institute of Education (RIE), Bhopal, NCERT", "Career and personal social Counselling"],
        ["Godavari Shivaji Ugale", "9420367233", "godavariugale8@gmail.com",
         "Regional Institute of Education (RIE), Bhopal, NCERT",
         "Career counseling and assessment, Parenting Expert"],
        ["Iti Bajaj", "9910313329", "bajajiti@gmail.com", "National Institute of Education(NIE), NCERT, New Delhi",
         "Child counseling and guidance"],
        ["Leena Vasudeo Chaudhari", "9503087116", "chaudhari.lee2@gmail.com",
         "Regional Institute of Education (RIE), Bhopal, NCERT",
         "Career Counselling, Educational Counseling, Learning disabilities, peer counseling"],
        ["Madhubala Prasad", "7588960240", "prasadmadhu85@gmail.com",
         "Regional Institute of Education (RIE), Bhopal, NCERT",
         "Innovation in teaching, mental health of students with the support of parental counseling"],
        ["Mugdha Kanage", "9422571373", "mugdhakanage@gmail.com",
         "Regional Institute Of Education (RIE), Bhopal, NCERT",
         "Adolescent Counseling, Parenting Coach, Special Educator"],
        ["Preeti Singh Misal", "8007776249", "preetisinghmisal@gmail.com", "Pune university",
         "Family and child counseling"],
        ["Shweta Mathur", "9867992510", "mathurshveta225@gmail.com",
         "National Institute of Education(NIE), NCERT, New Delhi", "Preventive, crisis counseling"],
        ["Smita Shipurkar", "9819016270", "smitashipurkar27@gmail.com",
         "Regional Institute of Education (RIE), Bhopal, NCERT", "Educational /Career Counsellor"],
        ["Surabhi Pranav", "7387000120", "surabhi.jdcoem@gmail.com",
         "National Institute of Education(NIE), NCERT, New Delhi",
         "Cognitive intervention and emotional intelligence"],
    ]

    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10)

        specializations = set([counselor[4] for counselor in self.counselors])

        self.selected_counselors = []
        self.counselor_labels = []

        specialization_buttons = []
        for specialization in specializations:
            specialization_button = Button(text=specialization, size_hint=(None, None), size=(400, 44))
            specialization_button.bind(on_press=self.update_counselors)

            # Set the button background color suitable for mental health
            if specialization == "Calming Green":
                specialization_button.background_color = (69/255, 255/255, 202/255, 1)  # #45FFCA (Light Green)
            elif specialization == "Light Yellow":
                specialization_button.background_color = (254/255, 255/255, 172/255, 1)  # #FEFFAC (Light Yellow)
            else:
                specialization_button.background_color = (255/255, 182/255, 217/255, 1)  # #FFB6D9 (Light Pink)

            specialization_buttons.append(specialization_button)

        for counselor in self.counselors:
            label = Label(text=counselor[4], opacity=0, halign="center", color=(20/255, 30/255, 70/255, 1))  # #141E46 (Navy Blue)
            self.counselor_labels.append(label)

        scrollview = ScrollView(size_hint=(None, None), size=(400, 300))
        content_layout = BoxLayout(orientation='vertical')

        for button in specialization_buttons:
            content_layout.add_widget(button)

        scrollview.add_widget(content_layout)

        for label in self.counselor_labels:
            layout.add_widget(label)

        layout.add_widget(scrollview)

        # Set the background color of the root layout
        with layout.canvas.before:
            Color(69/255, 255/255, 202/255, 1)  # #45FFCA (Light Green)
            Rectangle(size=(2000, 3000), pos=layout.pos)

        return layout

    def update_counselors(self, instance):
        specialization = instance.text
        for i, label in enumerate(self.counselor_labels):
            if specialization == 'All' or specialization == self.counselors[i][4]:
                label.text = f"Name: {self.counselors[i][0]}\nEmail: {self.counselors[i][2]}\nPhone: {self.counselors[i][1]}\nAddress: {self.counselors[i][3]}"
                label.opacity = 1
            else:
                label.opacity = 0

if __name__ == '__main__':
    CounselorApp().run()
