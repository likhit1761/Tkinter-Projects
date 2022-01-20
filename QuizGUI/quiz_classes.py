from tkinter import Tk, Canvas, StringVar, Label, Radiobutton, Button, messagebox
import requests

THEME_COLOR = "#375362"

parameters = {
    "amount": 10,
    "type": "multiple"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
question_data = response.json()["results"]

"""
Sample Response

[
    {
        'category': 'Sports', 
        'type': 'multiple', 
        'difficulty': 'medium', 
        'question': 'Which Formula One driver was nicknamed &#039;The Professor&#039;?',
        'correct_answer': 'Alain Prost', 
        'incorrect_answers': [
            'Ayrton Senna', 
            'Niki Lauda', 
            'Emerson Fittipaldi'
            ]
    }, 
    {
        'category': 'Entertainment: Music', 
        'type': 'multiple', 
        'difficulty': 'medium', 
        'question': 'In which city did American rap producer DJ Khaled originate from?',
        'correct_answer': 'Miami', 
        'incorrect_answers': [
            'New York', 
            'Detroit', 
            'Atlanta'
            ]
        }
]
"""


class Question:
    def __init__(self, question: str, correct_answer: str, choices: list):
        self.question_text = question
        self.correct_answer = correct_answer
        self.choices = choices


class Quiz_brain:

    def __init__(self, questions):
        self.question_no = 0
        self.score = 0
        self.questions = questions
        self.current_question = None

    def has_more_questions(self):
        return self.question_no < len(self.questions)

    def next_question(self):
        self.current_question = self.questions[self.question_no]
        self.question_no += 1
        q_text = self.current_question.question_text
        return f"Q.{self.question_no}: {q_text}"

    def check_answer(self, user_answer):
        correct_answer = self.current_question.correct_answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

    def get_score(self):
        wrong = self.question_no - self.score
        score_percent = int(self.score / self.question_no * 100)
        return (self.score, wrong, score_percent)


class Quiz_interface:
    def __init__(self, quiz_brain: Quiz_brain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("iQuiz App")
        self.window.geometry("850x530")

        self.display_title()

        self.canvas = Canvas(width=800, height=250)
        self.question_text = self.canvas.create_text(400, 125, text="Question", width=680, fill=THEME_COLOR,
                                                     font=('Ariel', 15, 'italic'))
        self.canvas.grid(row=2, column=0, columnspan=2, pady=50)
        self.display_question()

        self.user_answer = StringVar()

        self.opts = self.radio_buttons()
        self.display_options()

        self.feedback = Label(self.window, pady=10, font=("ariel", 15, "bold"))
        self.feedback.place(x=300, y=380)

        self.buttons()

        self.window.mainloop()

    def display_title(self):
        title = Label(self.window, text="iQuiz Application", width=50, bg="green", fg="white",
                      font=("ariel", 20, "bold"))
        title.place(x=0, y=2)

    def display_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def radio_buttons(self):
        choice_list = []
        y_pos = 220
        while len(choice_list) < 4:
            radio_btn = Radiobutton(self.window, text="", variable=self.user_answer, value='', font=("ariel", 14))
            choice_list.append(radio_btn)
            radio_btn.place(x=200, y=y_pos)
            y_pos += 40
        return choice_list

    def display_options(self):
        val = 0
        self.user_answer.set(None)
        for option in self.quiz.current_question.choices:
            self.opts[val]['text'] = option
            self.opts[val]['value'] = option
            val += 1

    def next_btn(self):
        if self.quiz.check_answer(self.user_answer.get()):
            self.feedback["fg"] = "green"
            self.feedback["text"] = 'Correct answer! \U0001F44D'
        else:
            self.feedback['fg'] = 'red'
            self.feedback['text'] = ('\u274E Oops! \n'
                                     f'The right answer is: {self.quiz.current_question.correct_answer}')

        if self.quiz.has_more_questions():
            self.display_question()
            self.display_options()
        else:
            self.display_result()
            self.window.destroy()

    def buttons(self):
        next_button = Button(self.window, text="Next", command=self.next_btn,
                             width=10, bg="green", fg="white", font=("ariel", 16, "bold"))
        next_button.place(x=350, y=460)
        quit_button = Button(self.window, text="Quit", command=self.window.destroy,
                             width=5, bg="red", fg="white", font=("ariel", 16, " bold"))
        quit_button.place(x=700, y=50)

    def display_result(self):
        correct, wrong, score_percent = self.quiz.get_score()
        correct = f"Correct: {correct}"
        wrong = f"Wrong: {wrong}"
        result = f"Score: {score_percent}%"
        messagebox.showinfo("Result", f"{result}\n{correct}\n{wrong}")
