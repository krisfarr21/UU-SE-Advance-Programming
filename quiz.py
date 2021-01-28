import random
import regex as re


class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.wrong_answers = []

    def add_wrong(self, wrong_answer):
        self.wrong_answers.append(wrong_answer)

    def ask(self):
        all_answers = self.wrong_answers.copy()
        all_answers.append(self.answer)
        random.shuffle(all_answers)
        correct_answer = all_answers.index(self.answer) + 1
        print(self.question)
        for i, answer in enumerate(all_answers):
            print(str(i + 1) + " :  " + answer)
        x = int(input("What is your answer? "))
        return x, correct_answer


# examples
q = Question('Capital of Sweden', 'Stockholm')
q.add_wrong('Uppsala')
q.add_wrong('Oslo')
q1 = Question('Capital of Malta', 'Valletta')
q1.add_wrong('Zurrieq')
q1.add_wrong('Msida')


class Quiz:
    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def do(self):
        counter = 0
        print(self.name)
        print("=" * len(self.name))
        for question in self.questions:
            result = question.ask()
            if result[0] == result[1]:
                counter += 1
                print("Correct!")
                print()
            else:
                print("Incorrect! Correct answers is: " + str(result[1]))
                print()
        print("You answered " + str(counter) + " correct out of " + str(len(self.questions)))
        return counter == len(self.questions)

    def do_until_right(self):
        while not self.do():
            continue
        else:
            print("You completed the quiz, well done! :)")


# examples
quiz = Quiz('Capital Cities')
quiz.add_question(q)
quiz.add_question(q1)


class IntQuestion(Question):
    def __init__(self, question, answer):
        Question.__init__(self, question, answer)

    def ask(self):
        print(self.question)
        x = (int(input("What is your answer? ")))
        return x, self.answer


def create_quiz_from_file(filename):
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            command, data = line.split(' ', 1)
            data = data.strip()
            if command == 'name':
                quiz = Quiz(data)
            elif command == 'q' or command == 'iq':
                text = data
            elif command == 'a':
                if bool(re.search(r'\d', data)):
                    print(bool(re.search(r'\d', data)))
                    question = IntQuestion(text, int(data))
                    quiz.add_question(question)
                else:
                    question = Question(text, data)
                    quiz.add_question(question)
            elif command == 'w':
                question.add_wrong(data)
    return quiz


disney_quiz = create_quiz_from_file('C:/Users/Kris/Desktop/Uppsala HLT'
                                    '/Second Semester Modules/Advanced Programming/'
                                    'Object-Oriented Programming/Assignment 1/disney.quiz')
disney_quiz.do_until_right()

q2 = IntQuestion("When was Malta granted independence?", 1964)
quiz.add_question(q2)
quiz.do_until_right()
