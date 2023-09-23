from turtle import *
import colorsys
import math
import turtle
import tkinter as tk
import random
from playsound import playsound
import json
import pygame

print("Welcome to Mind Buddy!")
print("I'm here to assist you with mental health support and information.")
print("How can I help you today?")
print("Hope your day is good.")
print("Together, we explore.")
print(" case 1 on to find how you feel")
print("case 2 to know more about mentel disorders and how to deal with them")
print("case 3  meditation music ")
print("case 4 to watch the making of mathematically symmetric patterns ")
print("case 5 to express and store your opinion ")
print("case 6 play stress bursting games")


def case_1():
    def get_user_input(prompt):
        while True:
            user_input = input(prompt).strip().lower()
            if user_input in ['yes', 'no']:
                return user_input
            print("Please enter 'yes' or 'no'.")

    def analyze_results(score):
        if score <= 3:
            print("Based on your responses, your mental health appears to be in a good state.")
        elif score <= 6:
            print(
                "Based on your responses, you may be experiencing some mild mental health concerns. It's important to take care of yourself and seek support if needed.")
        else:
            print(
                "Based on your responses, it seems like you may be facing some significant mental health challenges. It's crucial to reach out for professional help and support.")

    def mental_health_check():
        print("Welcome to the Mental Health Self-Assessment!")
        print("Please answer the following questions with 'yes' or 'no'.")
        print()

        score = 0

        questions = [
            "Do you often feel overwhelmed or excessively stressed?",
            "Have you been experiencing persistent feelings of sadness or hopelessness?",
            "Do you have difficulty concentrating or making decisions?",
            "Have you noticed a significant change in your appetite or weight?",
            "Are you having trouble sleeping or experiencing changes in your sleep patterns?",
            "Do you often feel anxious or experience panic attacks?",
            "Have you lost interest or pleasure in activities you used to enjoy?",
            "Do you find it challenging to manage your emotions or control your anger?",
            "Have you been isolating yourself or withdrawing from social interactions?",
            "Do you have thoughts of self-harm or suicide?"
        ]

        for question in questions:
            answer = get_user_input(question + " (yes/no): ")
            if answer == "yes":
                score += 1

        print()
        analyze_results(score)

    mental_health_check()


def case_2():
    def get_user_choice(prompt, options):
        while True:
            print(prompt)
            for i, option in enumerate(options):
                print(f"{i + 1}. {option}")
            choice = input("Enter the number corresponding to your choice: ")
            if choice.isdigit() and int(choice) in range(1, len(options) + 1):
                return int(choice)
            print("Invalid input. Please enter the number corresponding to your choice.")

    def display_disorder_info(disorder):
        disorder_info = {
            "depression": {
                "description": "Depression is a mood disorder that causes a persistent feeling of sadness and loss of interest.",
                "points": [
                    "Depression affects people of all ages and backgrounds.",
                    "It can be triggered by various factors, including genetics, life events, and chemical imbalances in the brain.",
                    "Common symptoms of depression include feelings of hopelessness, fatigue, changes in appetite, and difficulty concentrating.",
                    "Depression can coexist with other mental health conditions, such as anxiety.",
                    "It is important to seek professional help for an accurate diagnosis and appropriate treatment.",
                    "Treatment for depression may involve a combination of therapy, medication, lifestyle changes, and support from loved ones.",
                    "Support from friends and family plays a crucial role in recovery from depression.",
                    "Self-care activities, such as exercise, practicing relaxation techniques, and engaging in hobbies, can help alleviate symptoms.",
                    "Depression is treatable, and with the right support, individuals can experience improvement in their mental health.",
                    "It is essential to reach out to a mental health professional or helpline if you or someone you know is struggling with depression."
                ],
                "solutions": [
                    "Seek therapy with a licensed mental health professional.",
                    "Consider medication prescribed by a psychiatrist.",
                    "Engage in regular exercise, as it can boost mood and reduce symptoms.",
                    "Create a support system by reaching out to friends and family.",
                    "Practice self-care activities such as relaxation techniques and hobbies."
                ]
            },
            "anxiety": {
                "description": "Anxiety disorders are characterized by excessive and persistent worrying, fear, and uneasiness.",
                "points": [
                    "Anxiety disorders are among the most common mental health conditions worldwide.",
                    "They can manifest in different forms, such as generalized anxiety disorder (GAD), panic disorder, and social anxiety disorder.",
                    "Symptoms of anxiety may include restlessness, irritability, racing thoughts, physical tension, and avoidance of certain situations.",
                    "Anxiety can significantly impact daily functioning and quality of life.",
                    "It is important to seek professional help for a proper diagnosis and treatment plan.",
                    "Therapy, such as cognitive-behavioral therapy (CBT), is effective in managing anxiety disorders.",
                    "Medications, such as selective serotonin reuptake inhibitors (SSRIs), may be prescribed in some cases.",
                    "Practicing relaxation techniques, such as deep breathing and mindfulness, can help reduce anxiety symptoms.",
                    "Engaging in regular physical activity and maintaining a healthy lifestyle can contribute to managing anxiety.",
                    "Building a strong support system and communicating openly about anxiety can provide valuable support."
                ],
                "solutions": [
                    "Try cognitive-behavioral therapy to identify and manage anxious thoughts.",
                    "Consider medication options, such as selective serotonin reuptake inhibitors (SSRIs).",
                    "Practice deep breathing exercises and mindfulness techniques.",
                    "Engage in regular physical activity to reduce anxiety symptoms.",
                    "Avoid excessive caffeine and alcohol consumption, as they can worsen anxiety.",
                    "Seek support from a therapist, support groups, or trusted individuals in your life.",
                    "Learn and implement stress management techniques, such as time management and relaxation techniques.",
                    "Consider incorporating complementary therapies like yoga or meditation.",
                    "Challenge negative thoughts and practice positive affirmations.",
                    "Develop a self-care routine and prioritize activities that promote relaxation and well-being."
                ]
            },
            "bipolar disorder": {
                "description": "Bipolar disorder is a mental health condition that causes extreme mood swings, including periods of mania and depression.",
                "points": [
                    "Bipolar disorder affects individuals of all ages and can have a significant impact on their daily lives.",
                    "It is characterized by two distinct mood episodes: mania and depression.",
                    "During manic episodes, individuals may experience increased energy, euphoria, impulsivity, and decreased need for sleep.",
                    "Depressive episodes are characterized by feelings of sadness, hopelessness, low energy, and loss of interest.",
                    "The severity and duration of mood episodes can vary among individuals.",
                    "Bipolar disorder is often treated with a combination of medication, such as mood stabilizers, and therapy.",
                    "Psychoeducation and self-management strategies are essential for individuals with bipolar disorder.",
                    "Maintaining a regular sleep schedule and practicing stress management techniques can help stabilize mood.",
                    "Building a support network and involving loved ones in the treatment process is important.",
                    "Individuals with bipolar disorder can lead fulfilling lives with proper treatment, support, and self-care."
                ],
                "solutions": [
                    "Consult with a psychiatrist to develop an appropriate medication plan.",
                    "Engage in therapy, such as cognitive-behavioral therapy (CBT) or interpersonal and social rhythm therapy (IPSRT).",
                    "Create a daily routine to help maintain stability and manage mood swings.",
                    "Implement stress reduction techniques, such as mindfulness and relaxation exercises.",
                    "Stay connected with a support system of family, friends, or support groups.",
                    "Educate yourself and loved ones about bipolar disorder to better understand the condition.",
                    "Track and monitor mood changes using a mood diary or smartphone applications.",
                    "Ensure regular sleep patterns and practice good sleep hygiene.",
                    "Avoid alcohol and recreational drugs, as they can worsen symptoms.",
                    "Engage in regular exercise and maintain a healthy lifestyle."
                ]
            },
            "schizophrenia": {
                "description": "Schizophrenia is a chronic and severe mental disorder characterized by distorted thoughts, hallucinations, and delusions.",
                "points": [
                    "Schizophrenia affects how a person thinks, feels, and behaves.",
                    "It typically emerges in late adolescence or early adulthood and can be a lifelong condition.",
                    "Common symptoms include hallucinations, delusions, disorganized speech, and reduced emotional expression.",
                    "Schizophrenia can cause significant impairment in daily functioning and interpersonal relationships.",
                    "Treatment often involves a combination of antipsychotic medication, therapy, and psychosocial support.",
                    "Psychoeducation and family involvement are crucial in managing schizophrenia.",
                    "Supportive services, such as vocational training and housing assistance, can enhance the quality of life for individuals with schizophrenia.",
                    "Regular medication adherence and follow-up with mental health professionals are essential for managing symptoms.",
                    "Peer support groups can provide a sense of community and understanding for individuals with schizophrenia and their families.",
                    "Early intervention and access to comprehensive care can improve long-term outcomes for individuals with schizophrenia."
                ],
                "solutions": [
                    "Work closely with a psychiatrist to find the most effective antipsychotic medication and dosage.",
                    "Engage in therapy, such as cognitive-behavioral therapy for psychosis (CBTp) or family therapy.",
                    "Create a supportive and structured environment to minimize stress and triggers.",
                    "Develop coping strategies to manage hallucinations or delusions, such as reality testing techniques.",
                    "Establish a consistent routine and prioritize self-care activities.",
                    "Participate in psychosocial programs, vocational training, or supported employment opportunities.",
                    "Encourage family involvement and seek their support in the treatment process.",
                    "Connect with peer support groups or online communities to share experiences and gain support.",
                    "Monitor and manage medication side effects with the help of a healthcare professional.",
                    "Stay informed about new treatment options and advancements in schizophrenia management."
                ]
            },
            "obsessive-compulsive disorder (OCD)": {
                "description": "Obsessive-Compulsive Disorder (OCD) is a mental health condition characterized by recurring thoughts (obsessions) and repetitive behaviors (compulsions).",
                "points": [
                    "OCD can manifest in various forms, such as checking, washing, hoarding, or intrusive thoughts.",
                    "It often causes distress and interferes with daily functioning and relationships.",
                    "Common obsessions include fears of contamination, doubt, and intrusive or unwanted thoughts.",
                    "Compulsions are repetitive behaviors or mental acts aimed at reducing anxiety or preventing perceived harm.",
                    "Cognitive-behavioral therapy (CBT) and exposure and response prevention (ERP) are evidence-based treatments for OCD.",
                    "Medication, such as selective serotonin reuptake inhibitors (SSRIs), may be prescribed in combination with therapy.",
                    "Engaging in mindfulness and acceptance-based practices can help individuals manage obsessions and compulsions.",
                    "Support from loved ones and participating in support groups can provide understanding and encouragement.",
                    "Learning healthy coping strategies and stress management techniques is beneficial for individuals with OCD.",
                    "Recovery from OCD is possible with proper treatment, support, and dedication to therapy."
                ],
                "solutions": [
                    "Engage in cognitive-behavioral therapy (CBT) or exposure and response prevention (ERP) therapy.",
                    "Consider medication options, such as selective serotonin reuptake inhibitors (SSRIs).",
                    "Practice mindfulness and acceptance-based techniques to manage intrusive thoughts and anxiety.",
                    "Gradually expose yourself to feared situations or triggers to reduce avoidance behaviors.",
                    "Develop healthy coping mechanisms, such as engaging in hobbies or practicing relaxation techniques.",
                    "Maintain a structured daily routine to provide a sense of stability and reduce uncertainty.",
                    "Seek support from family, friends, or support groups who understand OCD.",
                    "Educate yourself about OCD to better understand its nature and treatment options.",
                    "Set realistic goals and celebrate small achievements in managing symptoms.",
                    "Stay committed to therapy and treatment, even during challenging times."
                ]
            },
            # Add more disorders and their information here
        }

        if disorder in disorder_info:
            info = disorder_info[disorder]
            print(f"\n{disorder.capitalize()}:\n")
            print("Description:", info["description"])
            print("Points:")
            for i, point in enumerate(info["points"]):
                print(f"{i + 1}. {point}")
            print("\nSolutions:")
            for i, solution in enumerate(info["solutions"]):
                print(f"{i + 1}. {solution}")
        else:
            print("Sorry, information about that disorder is not available.")

    def psychological_disorder_information():
        print("Welcome to the Psychological Disorder Information Center!")
        print("Please select a psychological disorder to learn more about it.")
        print()

        disorders = [
            "depression",
            "anxiety",
            "bipolar disorder",
            "schizophrenia",
            "obsessive-compulsive disorder (OCD)"
            # Add more disorders here
        ]

        choice = get_user_choice("Select a disorder:", disorders)
        selected_disorder = disorders[choice - 1]

        display_disorder_info(selected_disorder)

    psychological_disorder_information()


def case_3():
    def case_1():
        playsound("C:\\Users\\Acer\\Downloads\\mp3pproject\\fifteenmin.mp3")

    def case_2():
        playsound("C:\\Users\\Acer\\Downloads\\mp3pproject\\10min.mp3")

    def case_3():
        playsound("C:\\Users\\Acer\\Downloads\\mp3pproject\\fivemin.mp3")

    def switch_case(case):
        switch = {
            1: case_1,
            2: case_2,
            3: case_3
        }

        selected_case = switch.get(case)
        if selected_case:
            selected_case()
        else:
            print("Invalid case selected.")

    # Display options and get user input
    print("Meditation Duration Options:")
    print("1. 15 minutes")
    print("2. 10 minutes")
    print("3. 5 minutes")

    case_number = int(input("Choose an option (1-3): "))
    switch_case(case_number)


def case_4():
    def case_1():
        bgcolor('black')
        hue = 0.0
        hideturtle()
        pensize(5)
        speed(-15)
        for i in range(300):
            col = colorsys.hsv_to_rgb(hue, 1, 1)
            pencolor(col)
            hue += 0.005
            fd(i)
            rt(20 * 2 + 1)
            circle(50)

        done()

    def case_2():
        t = turtle.Turtle()
        t.speed(150)
        turtle.bgcolor('black')
        for i in range(250):
            t.color('green')
            t.forward(i)
            t.left(5)
        turtle.done()

    def case_3():
        colors = ['red', 'purple', 'white', 'yellow', 'green', 'pink']
        bgcolor('black')
        for x in range(360):
            pencolor(colors[x % 6])
            width(x / 100 + 1)
            forward(x)
            left(59)
            speed(500)

    def case_4():
        f = turtle.Turtle()
        f.speed(14)
        f.color('blue')
        turtle.bgcolor('black')
        for i in range(100):
            f.circle(80)
            f.right(50)

    def case_5():
        t = turtle.Turtle()
        s = turtle.Screen()
        s.bgcolor("black")
        t.pencolor("cyan")
        a = 0
        b = 0
        t.speed(0)
        t.penup()
        t.goto(0, 200)
        t.pendown()
        while True:
            t.forward(a)
            t.right(b)
            a += 3
            b += 1
            if b == 210:
                break
            t.hideturtle()

        turtle.done()

    def case_6():
        def hearta(k):
            return 15 * math.sin(k) ** 3

        def heartb(k):
            return 12 * math.cos(k) - 5 * \
                math.cos(2 * k) - 2 * \
                math.cos(3 * k) - \
                math.cos(4 * k)

        speed(0)
        bgcolor("black")
        for i in range(10000):
            goto(hearta(i) * 20, heartb(i) * 20)
            for j in range(5):
                color("#f73487")
                goto(0, 0)

        done()

    def case_7():
        hr = turtle.Turtle()
        hr.left(90)
        hr.speed(150)

        def tree(i):
            if (i >= 20):
                hr.forward(i)
                hr.left(30)
                tree(3 * i / 4)
                hr.right(30)
                tree(3 * i / 4)
                hr.right(30)
                tree(3 * i / 4)
                hr.left(30)
                hr.backward(i)

        tree(100)
        turtle.done()

    def switch_case(case):
        switch = {
            1: case_1,
            2: case_2,
            3: case_3,
            4: case_4,
            5: case_5,
            6: case_6,
            7: case_7
        }

        selected_case = switch.get(case)
        if selected_case:
            selected_case()
        else:
            print("Invalid case selected.")

    # Example usage
    case_number = int(input("Enter a case number (1-7): "))
    switch_case(case_number)


def case_5():
    class Community:
        def __init__(self):
            self.posts = []

        def create_post(self, post):
            self.posts.append(post)

        def view_posts(self):
            for post in self.posts:
                print(f"Author: {post['author']}")
                print(f"Opinion: {post['opinion']}")
                print("---")

        def save_posts(self, file_name):
            with open(file_name, 'w') as file:
                json.dump(self.posts, file)

        def load_posts(self, file_name):
            try:
                with open(file_name, 'r') as file:
                    self.posts = json.load(file)
            except FileNotFoundError:
                print("No previous history found.")

    # Create a new community
    my_community = Community()

    # Load previous posts from file
    my_community.load_posts("community_posts.json")

    # Main program loop
    while True:
        print("Community Menu:")
        print("1. Create a new post")
        print("2. View posts")
        print("3. Save and Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            author = input("Enter your name: ")
            opinion = input("Enter your opinion: ")
            post = {"author": author, "opinion": opinion}
            my_community.create_post(post)
            print("Post created successfully!")

        elif choice == "2":
            print("Community Posts:")
            my_community.view_posts()

        elif choice == "3":
            print("Saving community posts...")
            my_community.save_posts("community_posts.json")
            print("Exiting the community...")
            break

        else:
            print("Invalid choice. Please try again.")


def case_6():
    # Bubble Wrap Popper Game
    def bubble_wrap_popper():
        def pop_bubble(event):
            event.widget.destroy()

        root = tk.Tk()
        root.title("Bubble Wrap Popper")
        root.geometry("400x400")

        for i in range(20):
            for j in range(20):
                bubble = tk.Label(root, relief="solid", width=2, height=1)
                bubble.grid(row=i, column=j, padx=2, pady=2)
                bubble.bind("<Button-1>", pop_bubble)

        root.mainloop()

    # Ping Pong Game
    def ping_pong_game():
        pygame.init()

        # Set up the game window
        win_width, win_height = 800, 400
        win = pygame.display.set_mode((win_width, win_height))
        pygame.display.set_caption("Ping Pong")

        # Game variables
        paddle_width, paddle_height = 10, 80
        paddle_velocity = 5
        ball_radius = 10
        ball_velocity_x = 3
        ball_velocity_y = 3
        paddle_left_pos = win_height // 2 - paddle_height // 2
        paddle_right_pos = win_height // 2 - paddle_height // 2
        ball_pos_x = win_width // 2
        ball_pos_y = win_height // 2

        def move_paddle_up():
            nonlocal paddle_left_pos, paddle_right_pos
            if paddle_left_pos > 0:
                paddle_left_pos -= paddle_velocity
            if paddle_right_pos > 0:
                paddle_right_pos -= paddle_velocity

        def move_paddle_down():
            nonlocal paddle_left_pos, paddle_right_pos
            if paddle_left_pos < win_height - paddle_height:
                paddle_left_pos += paddle_velocity
            if paddle_right_pos < win_height - paddle_height:
                paddle_right_pos += paddle_velocity

        def move_ball():
            nonlocal ball_pos_x, ball_pos_y, ball_velocity_x, ball_velocity_y, paddle_left_pos, paddle_right_pos
            ball_pos_x += ball_velocity_x
            ball_pos_y += ball_velocity_y

            if ball_pos_y <= 0 or ball_pos_y >= win_height - ball_radius:
                ball_velocity_y *= -1

            if ball_pos_x <= paddle_width and paddle_left_pos <= ball_pos_y <= paddle_left_pos + paddle_height:
                ball_velocity_x *= -1

            if ball_pos_x >= win_width - paddle_width - ball_radius and paddle_right_pos <= ball_pos_y <= paddle_right_pos + paddle_height:
                ball_velocity_x *= -1

        # Game loop
        running = True
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        move_paddle_up()
                    elif event.key == pygame.K_s:
                        move_paddle_down()

            move_ball()

            win.fill((0, 0, 0))
            pygame.draw.rect(win, (255, 255, 255), (paddle_width, paddle_left_pos, paddle_width, paddle_height))
            pygame.draw.rect(win, (255, 255, 255),
                             (win_width - 2 * paddle_width, paddle_right_pos, paddle_width, paddle_height))
            pygame.draw.circle(win, (255, 255, 255), (ball_pos_x, ball_pos_y), ball_radius)

            pygame.display.update()
            clock.tick(60)

        pygame.quit()

    # Whack-a-Mole Game
    def whack_a_mole_game():
        def mole_hit(event):
            score_label.config(text="Score: " + str(int(score_label["text"].split()[1]) + 1))
            event.widget.destroy()

        root = tk.Tk()
        root.title("Whack-a-Mole")
        root.geometry("400x400")

        score_label = tk.Label(root, text="Score: 0", font=("Arial", 16))
        score_label.pack(pady=10)

        for _ in range(10):
            mole = tk.Label(root, text="O", font=("Arial", 24), bg="brown", fg="white")
            mole.place(x=random.randint(50, 350), y=random.randint(50, 350))
            mole.bind("<Button-1>", mole_hit)

        root.mainloop()

    def play_game(game):
        game_func = {
            "1": bubble_wrap_popper,
            "2": ping_pong_game,
            "3": whack_a_mole_game,
        }
        selected_game = game_func.get(game)
        if selected_game:
            selected_game()
        else:
            print("Invalid game selection!")

    # Main program
    while True:
        print("1. Bubble Wrap Popper")
        print("2. Ping Pong Game")
        print("3. Whack-a-Mole Game")
        print("4. Exit")
        choice = input("Select a game (1-3) or enter '4' to exit: ")
        if choice == "4":
            break
        play_game(choice)


def case_7():
    print("plese re-enter your choice")
    case_number = int(input("Enter a case number (1-7): "))
    switch_case(case_number)


def switch_case(case):
    switch = {
        1: case_1,
        2: case_2,
        3: case_3,
        4: case_4,
        5: case_5,
        6: case_6,
        7: case_7
    }

    selected_case = switch.get(case)
    if selected_case:
        selected_case()
    else:
        print("Invalid case selected.")


# Example usage
case_number = int(input("Enter a case number (1-7): "))
switch_case(case_number)
