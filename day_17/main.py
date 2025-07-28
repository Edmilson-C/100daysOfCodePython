from question_model import QuestionModel
from data import question_data
from quiz_brain import is_answer_correct, choose_answer

questions_list = []
asked_questions = 1
points = 0
wants_to_continue = True

for question in question_data:
    questions_list.append(QuestionModel(question["text"], question["answer"]))

while wants_to_continue:
    if len(questions_list) > 0:
        current_question_position = choose_answer(questions_list)
        current_question = questions_list[current_question_position]

        users_answer = input(f"Q.{asked_questions}.: {current_question.question} True/False ")

        if is_answer_correct(current_question.answer, users_answer):
            points += 1
            questions_list.pop(current_question_position)
            print("Correct!")
        else:
            print("Wrong!")

        asked_questions += 1
        answer = input("Do you want to continue? Yes/No ")
        if answer.lower() == "no" or answer.lower() == "n":
            wants_to_continue = False
    else:
        print("You have answered all the questions")
        wants_to_continue = False

print(f"You earned {points} points")