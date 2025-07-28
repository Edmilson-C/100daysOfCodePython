from random import randint


def is_answer_correct(right_answer, user_answer):
    if right_answer.lower() == user_answer.lower():
        return True
    elif right_answer[0].lower() == user_answer.lower():
        return True

    return False


def choose_answer(questions_list):
    return randint(1, len(questions_list) - 1)
