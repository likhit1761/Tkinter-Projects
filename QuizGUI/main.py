from quiz_classes import Question, Quiz_brain, Quiz_interface, question_data
from random import shuffle
import html


question_book = []
for question in question_data:
    choices = []
    question_text = html.unescape(question["question"])
    correct_answer = html.unescape(question["correct_answer"])
    incorrect_answers = question["incorrect_answers"]
    for ans in incorrect_answers:
        choices.append(html.unescape(ans))
    choices.append(correct_answer)
    shuffle(choices)
    new_question = Question(question_text, correct_answer, choices)
    question_book.append(new_question)

quiz = Quiz_brain(question_book)

quiz_ui = Quiz_interface(quiz)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_no}")
