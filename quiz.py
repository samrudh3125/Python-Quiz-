from quetsions import question_data

class Question:
    def __init__(self,q_text,q_answer):
        self.text=q_text
        self.answer=q_answer

question_bank=[
    Question(question_data[0]["text"],question_data[0]["answer"]),
    Question(question_data[1]["text"],question_data[1]["answer"]),
    Question(question_data[2]["text"],question_data[2]["answer"]),
    Question(question_data[3]["text"],question_data[3]["answer"]),
    Question(question_data[4]["text"],question_data[4]["answer"]),
    Question(question_data[5]["text"],question_data[5]["answer"]),
    Question(question_data[6]["text"],question_data[6]["answer"]),
    Question(question_data[7]["text"],question_data[7]["answer"]),
    Question(question_data[8]["text"],question_data[8]["answer"]),
    Question(question_data[9]["text"],question_data[9]["answer"]),
    Question(question_data[10]["text"],question_data[10]["answer"]),
    Question(question_data[11]["text"],question_data[11]["answer"]),
]

class Quizbrain:
    def __init__(self,questions_list):
        self.question_number=0
        self.q_list=questions_list

Quizbrain(question_bank)
user_answer=input(question_bank)

